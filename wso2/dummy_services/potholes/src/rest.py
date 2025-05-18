from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from entities.user import User
from entities.pothole import Pothole
from typing import Dict, List, Any

app = Flask(__name__)
api = Api(app)

class UserResource(Resource):
    def get(self, user_id=None):
        """Get a single user or all users."""
        if user_id:
            user = User.get_by_id(user_id)
            if not user:
                return {"error": "User not found"}, 404
            return user.to_dict(), 200
        else:
            users = User.get_all()
            return [user.to_dict() for user in users], 200

    def post(self):
        """Create a new user."""
        data = request.get_json()
        
        if not data or not all(k in data for k in ["name", "email"]):
            return {"error": "Missing required fields"}, 400
            
        user = User(
            name=data["name"],
            email=data["email"],
            role=data.get("role", "citizen")
        )
        user_id = user.save()
        
        return {"id": user_id, "message": "User created successfully"}, 201

    def put(self, user_id):
        """Update an existing user."""
        if not user_id:
            return {"error": "User ID is required"}, 400
            
        user = User.get_by_id(user_id)
        if not user:
            return {"error": "User not found"}, 404
            
        data = request.get_json()
        if "name" in data:
            user.name = data["name"]
        if "email" in data:
            user.email = data["email"]
        if "role" in data:
            user.role = data["role"]
            
        user.save()
        return user.to_dict(), 200

    def delete(self, user_id):
        """Delete a user."""
        if not user_id:
            return {"error": "User ID is required"}, 400
            
        user = User.get_by_id(user_id)
        if not user:
            return {"error": "User not found"}, 404
            
        user.delete()
        return {"message": "User deleted successfully"}, 200


class PotholeResource(Resource):
    def get(self, pothole_id=None):
        """Get a single pothole or all potholes."""
        if pothole_id:
            pothole = Pothole.get_by_id(pothole_id)
            if not pothole:
                return {"error": "Pothole not found"}, 404
            return pothole.to_dict(), 200
        else:
            status = request.args.get("status")
            reported_by = request.args.get("reported_by")
            
            if status:
                potholes = Pothole.get_by_status(status)
            elif reported_by:
                potholes = Pothole.get_by_reporter(int(reported_by))
            else:
                potholes = Pothole.get_all()
                
            return [pothole.to_dict() for pothole in potholes], 200

    def post(self):
        """Create a new pothole report."""
        data = request.get_json()
        
        if not data or not all(k in data for k in ["street_name", "reported_by"]):
            return {"error": "Missing required fields"}, 400
            
        # Verify the reporter exists
        reporter = User.get_by_id(data["reported_by"])
        if not reporter:
            return {"error": "Reporter not found"}, 404
            
        pothole = Pothole(
            street_name=data["street_name"],
            reported_by=data["reported_by"],
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
            diameter_cm=data.get("diameter_cm"),
            description=data.get("description"),
            status=data.get("status", "open")
        )
        pothole_id = pothole.save()
        
        return {"id": pothole_id, "message": "Pothole reported successfully"}, 201

    def put(self, pothole_id):
        """Update an existing pothole."""
        if not pothole_id:
            return {"error": "Pothole ID is required"}, 400
            
        pothole = Pothole.get_by_id(pothole_id)
        if not pothole:
            return {"error": "Pothole not found"}, 404
            
        data = request.get_json()
        
        if "street_name" in data:
            pothole.street_name = data["street_name"]
        if "reported_by" in data:
            # Verify the reporter exists
            reporter = User.get_by_id(data["reported_by"])
            if not reporter:
                return {"error": "Reporter not found"}, 404
            pothole.reported_by = data["reported_by"]
        if "latitude" in data:
            pothole.latitude = data["latitude"]
        if "longitude" in data:
            pothole.longitude = data["longitude"]
        if "diameter_cm" in data:
            pothole.diameter_cm = data["diameter_cm"]
        if "description" in data:
            pothole.description = data["description"]
        if "status" in data:
            pothole.status = data["status"]
            
        pothole.save()
        return pothole.to_dict(), 200

    def delete(self, pothole_id):
        """Delete a pothole."""
        if not pothole_id:
            return {"error": "Pothole ID is required"}, 400
            
        pothole = Pothole.get_by_id(pothole_id)
        if not pothole:
            return {"error": "Pothole not found"}, 404
            
        pothole.delete()
        return {"message": "Pothole deleted successfully"}, 200


# Add endpoints
api.add_resource(UserResource, '/api/users', '/api/users/<int:user_id>')
api.add_resource(PotholeResource, '/api/potholes', '/api/potholes/<int:pothole_id>')

# Add a health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "service": "pothole-tracker-rest"})
