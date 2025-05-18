from spyne import Application, rpc, ServiceBase, Unicode, Integer, Float, Array, Boolean
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.model.complex import ComplexModel
from wsgiref.simple_server import make_server

from entities.user import User
from entities.pothole import Pothole

class UserModel(ComplexModel):
    """User model for SOAP service."""
    id = Integer
    name = Unicode
    email = Unicode
    role = Unicode
    created_at = Unicode

class PotholeModel(ComplexModel):
    """Pothole model for SOAP service."""
    id = Integer
    street_name = Unicode
    reported_by = Integer
    latitude = Float
    longitude = Float
    diameter_cm = Float
    description = Unicode
    status = Unicode
    created_at = Unicode
    updated_at = Unicode

def user_to_model(user):
    """Convert a User entity to a UserModel."""
    if not user:
        return None
    model = UserModel()
    model.id = user.id
    model.name = user.name
    model.email = user.email
    model.role = user.role
    model.created_at = user.created_at.isoformat() if user.created_at else None
    return model

def pothole_to_model(pothole):
    """Convert a Pothole entity to a PotholeModel."""
    if not pothole:
        return None
    model = PotholeModel()
    model.id = pothole.id
    model.street_name = pothole.street_name
    model.reported_by = pothole.reported_by
    model.latitude = pothole.latitude
    model.longitude = pothole.longitude
    model.diameter_cm = pothole.diameter_cm
    model.description = pothole.description
    model.status = pothole.status
    model.created_at = pothole.created_at.isoformat() if pothole.created_at else None
    model.updated_at = pothole.updated_at.isoformat() if pothole.updated_at else None
    return model

class UserService(ServiceBase):
    @rpc(Integer, _returns=UserModel)
    def get_user(ctx, user_id):
        """Get a user by ID."""
        user = User.get_by_id(user_id)
        return user_to_model(user)
    
    @rpc(_returns=Array(UserModel))
    def get_all_users(ctx):
        """Get all users."""
        users = User.get_all()
        return [user_to_model(user) for user in users]
    
    @rpc(Unicode, Unicode, Unicode, _returns=Integer)
    def create_user(ctx, name, email, role="citizen"):
        """Create a new user."""
        user = User(name=name, email=email, role=role)
        return user.save()
    
    @rpc(Integer, Unicode, Unicode, Unicode, _returns=UserModel)
    def update_user(ctx, user_id, name=None, email=None, role=None):
        """Update an existing user."""
        user = User.get_by_id(user_id)
        if not user:
            return None
            
        if name:
            user.name = name
        if email:
            user.email = email
        if role:
            user.role = role
            
        user.save()
        return user_to_model(user)
    
    @rpc(Integer, _returns=Boolean)
    def delete_user(ctx, user_id):
        """Delete a user."""
        user = User.get_by_id(user_id)
        if not user:
            return False
        return user.delete()

class PotholeService(ServiceBase):
    @rpc(Integer, _returns=PotholeModel)
    def get_pothole(ctx, pothole_id):
        """Get a pothole by ID."""
        pothole = Pothole.get_by_id(pothole_id)
        return pothole_to_model(pothole)
    
    @rpc(_returns=Array(PotholeModel))
    def get_all_potholes(ctx):
        """Get all potholes."""
        potholes = Pothole.get_all()
        return [pothole_to_model(pothole) for pothole in potholes]
    
    @rpc(Unicode, _returns=Array(PotholeModel))
    def get_potholes_by_status(ctx, status):
        """Get potholes by status."""
        potholes = Pothole.get_by_status(status)
        return [pothole_to_model(pothole) for pothole in potholes]
    
    @rpc(Integer, _returns=Array(PotholeModel))
    def get_potholes_by_reporter(ctx, user_id):
        """Get potholes reported by a specific user."""
        potholes = Pothole.get_by_reporter(user_id)
        return [pothole_to_model(pothole) for pothole in potholes]
    
    @rpc(Unicode, Integer, Float, Float, Float, Unicode, Unicode, _returns=Integer)
    def create_pothole(ctx, street_name, reported_by, latitude=None, longitude=None, 
                       diameter_cm=None, description=None, status="open"):
        """Create a new pothole report."""
        # Verify the reporter exists
        reporter = User.get_by_id(reported_by)
        if not reporter:
            return -1
            
        pothole = Pothole(
            street_name=street_name,
            reported_by=reported_by,
            latitude=latitude,
            longitude=longitude,
            diameter_cm=diameter_cm,
            description=description,
            status=status
        )
        return pothole.save()
    
    @rpc(Integer, Unicode, Integer, Float, Float, Float, Unicode, Unicode, _returns=PotholeModel)
    def update_pothole(ctx, pothole_id, street_name=None, reported_by=None, 
                       latitude=None, longitude=None, diameter_cm=None, 
                       description=None, status=None):
        """Update an existing pothole."""
        pothole = Pothole.get_by_id(pothole_id)
        if not pothole:
            return None
            
        if street_name:
            pothole.street_name = street_name
        if reported_by:
            # Verify the reporter exists
            reporter = User.get_by_id(reported_by)
            if not reporter:
                return None
            pothole.reported_by = reported_by
        if latitude is not None:
            pothole.latitude = latitude
        if longitude is not None:
            pothole.longitude = longitude
        if diameter_cm is not None:
            pothole.diameter_cm = diameter_cm
        if description:
            pothole.description = description
        if status:
            pothole.status = status
            
        pothole.save()
        return pothole_to_model(pothole)
    
    @rpc(Integer, _returns=Boolean)
    def delete_pothole(ctx, pothole_id):
        """Delete a pothole."""
        pothole = Pothole.get_by_id(pothole_id)
        if not pothole:
            return False
        return pothole.delete()

# Create application and expose services
application = Application([UserService, PotholeService],
                          tns='http://pothole.tracker.service',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

# Create the WSGI app
soap_app = WsgiApplication(application)

def get_wsgi_application():
    """Return the WSGI application for integration with other servers."""
    return soap_app

# For standalone serving
if __name__ == '__main__':
    # Standalone server for testing
    server = make_server('0.0.0.0', 8001, soap_app)
    print("SOAP service starting on port 8001...")
    server.serve_forever() 