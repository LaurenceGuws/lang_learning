from flask import Flask, jsonify
from flask_apispec import FlaskApiSpec, doc, use_kwargs, marshal_with
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from marshmallow import Schema, fields
from rest import app as rest_app

# Initialize the App with API Specs
app = rest_app
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Pothole Tracker API',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0',
    ),
    'APISPEC_SWAGGER_URL': '/api/swagger/',
    'APISPEC_SWAGGER_UI_URL': '/api/swagger-ui/'
})

docs = FlaskApiSpec(app)

# Define Schemas
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    role = fields.Str()
    created_at = fields.DateTime(dump_only=True)

class PotholeSchema(Schema):
    id = fields.Int(dump_only=True)
    street_name = fields.Str(required=True)
    reported_by = fields.Int(required=True)
    latitude = fields.Float()
    longitude = fields.Float()
    diameter_cm = fields.Float()
    description = fields.Str()
    status = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

# Register endpoints
@app.route('/api/docs', methods=['GET'])
def get_docs():
    """Get API documentation links."""
    return jsonify({
        'swagger_json': '/api/swagger/',
        'swagger_ui': '/api/swagger-ui/'
    })

# Register view functions with apispec by registering with Flask-apispec
@doc(tags=['Users'])
@app.route('/api/users', methods=['GET'])
def get_users():
    """Get all users."""
    pass

@doc(tags=['Users'])
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get a user by ID."""
    pass

@doc(tags=['Users'])
@app.route('/api/users', methods=['POST'])
def create_user():
    """Create a new user."""
    pass

@doc(tags=['Users'])
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update an existing user."""
    pass

@doc(tags=['Users'])
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user."""
    pass

@doc(tags=['Potholes'])
@app.route('/api/potholes', methods=['GET'])
def get_potholes():
    """Get all potholes."""
    pass

@doc(tags=['Potholes'])
@app.route('/api/potholes/<int:pothole_id>', methods=['GET'])
def get_pothole(pothole_id):
    """Get a pothole by ID."""
    pass

@doc(tags=['Potholes'])
@app.route('/api/potholes', methods=['POST'])
def create_pothole():
    """Create a new pothole report."""
    pass

@doc(tags=['Potholes'])
@app.route('/api/potholes/<int:pothole_id>', methods=['PUT'])
def update_pothole(pothole_id):
    """Update an existing pothole."""
    pass

@doc(tags=['Potholes'])
@app.route('/api/potholes/<int:pothole_id>', methods=['DELETE'])
def delete_pothole(pothole_id):
    """Delete a pothole."""
    pass

# Register documented endpoints with apispec
docs.register(get_users)
docs.register(get_user)
docs.register(create_user)
docs.register(update_user)
docs.register(delete_user)
docs.register(get_potholes)
docs.register(get_pothole)
docs.register(create_pothole)
docs.register(update_pothole)
docs.register(delete_pothole)

if __name__ == '__main__':
    app.run(debug=True) 