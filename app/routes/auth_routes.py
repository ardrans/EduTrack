from flask import Blueprint, request, jsonify
from app import db
from app.models import Users, Roles
auth_routes = Blueprint('auth', __name__)

# Route to create a new user
@auth_routes.route('/users', methods=['POST'])
def create_user():
    data = request.json
    try:
        new_user = Users(
            name=data.get('name'),
            email=data.get('email'),
            role_id=data.get('role_id')
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully", "user": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email,
            "role_id": new_user.role_id
        }}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to fetch all users
@auth_routes.route('/users', methods=['GET'])
def get_users():
    users = Users.query.all()
    users_list = [
        {"id": user.id, "name": user.name, "email": user.email, "role_id": user.role_id}
        for user in users
    ]
    return jsonify(users_list), 200

# Route to fetch a user by ID
@auth_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = Users.query.get_or_404(user_id)
    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role_id": user.role_id
    }), 200

# Route to update a user
@auth_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = Users.query.get_or_404(user_id)
    data = request.json
    try:
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)
        user.role_id = data.get('role_id', user.role_id)
        db.session.commit()
        return jsonify({"message": "User updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to delete a user
@auth_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = Users.query.get_or_404(user_id)
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to create a new role
@auth_routes.route('/roles', methods=['POST'])
def create_role():
    data = request.json
    try:
        new_role = Roles(
            name=data.get('name')
        )
        db.session.add(new_role)
        db.session.commit()
        return jsonify({"message": "Role created successfully", "role": {
            "id": new_role.id,
            "name": new_role.name
        }}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to fetch all roles
@auth_routes.route('/roles', methods=['GET'])
def get_roles():
    roles = Roles.query.all()
    roles_list = [{"id": role.id, "name": role.name} for role in roles]
    return jsonify(roles_list), 200

# Route to fetch a role by ID
@auth_routes.route('/roles/<int:role_id>', methods=['GET'])
def get_role(role_id):
    role = Roles.query.get_or_404(role_id)
    return jsonify({
        "id": role.id,
        "name": role.name
    }), 200

# Route to update a role
@auth_routes.route('/roles/<int:role_id>', methods=['PUT'])
def update_role(role_id):
    role = Roles.query.get_or_404(role_id)
    data = request.json
    try:
        role.name = data.get('name', role.name)
        db.session.commit()
        return jsonify({"message": "Role updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to delete a role
@auth_routes.route('/roles/<int:role_id>', methods=['DELETE'])
def delete_role(role_id):
    role = Roles.query.get_or_404(role_id)
    try:
        db.session.delete(role)
        db.session.commit()
        return jsonify({"message": "Role deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
