from flask import jsonify
from app import db
from app.models import Users, Roles

# User services
class UserService:
    @staticmethod
    def create_user(data):
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

    @staticmethod
    def get_users():
        users = Users.query.all()
        users_list = [
            {"id": user.id, "name": user.name, "email": user.email, "role_id": user.role_id}
            for user in users
        ]
        return jsonify(users_list), 200

    @staticmethod
    def get_user(user_id):
        user = Users.query.get_or_404(user_id)
        return jsonify({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role_id": user.role_id
        }), 200

    @staticmethod
    def update_user(user_id, data):
        user = Users.query.get_or_404(user_id)
        try:
            user.name = data.get('name', user.name)
            user.email = data.get('email', user.email)
            user.role_id = data.get('role_id', user.role_id)
            db.session.commit()
            return jsonify({"message": "User updated successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def delete_user(user_id):
        user = Users.query.get_or_404(user_id)
        try:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": "User deleted successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400


# Role services
class RoleService:
    @staticmethod
    def create_role(data):
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

    @staticmethod
    def get_roles():
        roles = Roles.query.all()
        roles_list = [{"id": role.id, "name": role.name} for role in roles]
        return jsonify(roles_list), 200

    @staticmethod
    def get_role(role_id):
        role = Roles.query.get_or_404(role_id)
        return jsonify({
            "id": role.id,
            "name": role.name
        }), 200

    @staticmethod
    def update_role(role_id, data):
        role = Roles.query.get_or_404(role_id)
        try:
            role.name = data.get('name', role.name)
            db.session.commit()
            return jsonify({"message": "Role updated successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def delete_role(role_id):
        role = Roles.query.get_or_404(role_id)
        try:
            db.session.delete(role)
            db.session.commit()
            return jsonify({"message": "Role deleted successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400


# Expose services
user_service = UserService()
role_service = RoleService()
