from flask import Blueprint, request
from app.services.auth_services import user_service, role_service

auth_routes = Blueprint('auth', __name__)

# User routes
@auth_routes.route('/users', methods=['POST'])
def create_user():
    data = request.json
    return user_service.create_user(data)

@auth_routes.route('/users', methods=['GET'])
def get_users():
    return user_service.get_users()

@auth_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return user_service.get_user(user_id)

@auth_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    return user_service.update_user(user_id, data)

@auth_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return user_service.delete_user(user_id)

# Role routes
@auth_routes.route('/roles', methods=['POST'])
def create_role():
    data = request.json
    return role_service.create_role(data)

@auth_routes.route('/roles', methods=['GET'])
def get_roles():
    return role_service.get_roles()

@auth_routes.route('/roles/<int:role_id>', methods=['GET'])
def get_role(role_id):
    return role_service.get_role(role_id)

@auth_routes.route('/roles/<int:role_id>', methods=['PUT'])
def update_role(role_id):
    data = request.json
    return role_service.update_role(role_id, data)

@auth_routes.route('/roles/<int:role_id>', methods=['DELETE'])
def delete_role(role_id):
    return role_service.delete_role(role_id)
