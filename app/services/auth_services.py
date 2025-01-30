import jwt
import datetime
from flask import jsonify, request, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import db
from app.models import Users, Roles
from ..logging__config import init_logger
from datetime import datetime, timedelta, timezone
from app.auth_utils import token_required
from app.middleware.permission import check_permission
from flask import jsonify, g
from functools import wraps

# Set up the logger for this module
logger = init_logger(__name__)

# Secret key for encoding/decoding JWTsa
SECRET_KEY = 'edutrack1234'

# User services
class UserService:
    @staticmethod
    def create_user(data):
        logger.info("Creating a new user with data: %s", data)
        try:
            # Initialize user and set hashed password
            new_user = Users(
                name=data.get('name'),
                email=data.get('email'),
                role_id=data.get('role_id')
            )
            password = data.get('password')
            if not password:
                return jsonify({"error": "Password is required"}), 400
            new_user.set_password(password)  # Hash the password

            db.session.add(new_user)
            db.session.commit()
            logger.info("User created successfully: %s", new_user)
            return jsonify({"message": "User created successfully", "user": {
                "id": new_user.id,
                "name": new_user.name,
                "email": new_user.email,
                "role_id": new_user.role_id
            }}), 201
        except Exception as e:
            db.session.rollback()
            logger.error("Error creating user: %s", str(e), exc_info=True)
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def get_users():
        logger.info("Fetching all users")
        users = Users.query.all()
        users_list = [
            {"id": user.id, "name": user.name, "email": user.email, "role_id": user.role_id}
            for user in users
        ]
        logger.info("Fetched %d users", len(users_list))
        return jsonify(users_list), 200

    @staticmethod
    def get_user(user_id):
        logger.info("Fetching user with ID: %d", user_id)
        user = Users.query.get_or_404(user_id)
        logger.info("Fetched user: %s", user)
        return jsonify({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role_id": user.role_id
        }), 200

    @staticmethod
    def update_user(user_id, data):
        logger.info("Updating user with ID: %d", user_id)
        user = Users.query.get_or_404(user_id)
        try:
            user.name = data.get('name', user.name)
            user.email = data.get('email', user.email)
            user.role_id = data.get('role_id', user.role_id)

            # Handle password update
            password = data.get('password')
            if password:
                user.set_password(password)  # Hash the password

            db.session.commit()
            logger.info("User updated successfully: %s", user)
            return jsonify({"message": "User updated successfully"}), 200
        except Exception as e:
            db.session.rollback()
            logger.error("Error updating user: %s", str(e), exc_info=True)
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def delete_user(user_id):
        logger.info("Deleting user with ID: %d", user_id)
        user = Users.query.get_or_404(user_id)
        try:
            db.session.delete(user)
            db.session.commit()
            logger.info("User deleted successfully: %s", user)
            return jsonify({"message": "User deleted successfully"}), 200
        except Exception as e:
            db.session.rollback()
            logger.error("Error deleting user: %s", str(e), exc_info=True)
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def get_trainers_count():
        logger.info("Fetching count of trainers")
        try:
            trainer_role = Roles.query.filter_by(name='Trainer').first()
            if not trainer_role:
                return jsonify({"error": "Trainer role not found"}), 404

            trainers_count = Users.query.filter_by(role_id=trainer_role.id).count()
            logger.info("Total trainers: %d", trainers_count)
            return jsonify({"trainers_count": trainers_count}), 200
        except Exception as e:
            logger.error("Error fetching trainers count: %s", str(e), exc_info=True)
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def get_trainers():
        try:
            trainer_role = Roles.query.filter_by(name='Trainer').first()
            if not trainer_role:
                return jsonify({"error": "Trainer role not found"}), 404

            trainers = Users.query.filter_by(role_id=trainer_role.id).all()
            trainer_list = [{"id": trainer.id, "name": trainer.name} for trainer in trainers]

            return jsonify(trainer_list), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def login_user(data):
        logger.info("Attempting to log in user with email: %s", data.get('email'))
        user = Users.query.filter_by(email=data.get('email')).first()

        if not user or not check_password_hash(user.password_hash, data.get('password')):
            logger.warning("Invalid credentials for user with email: %s", data.get('email'))
            return jsonify({"error": "Invalid email or password"}), 401

        token = UserService.generate_jwt(user)

        logger.info("User logged in successfully: %s", user)
        return jsonify({
            "message": "Login successful",
            "token": token
        }), 200

    @staticmethod
    def generate_jwt(user):
        payload = {
            'user_id': user.id,
            'exp': datetime.now(timezone.utc) + timedelta(hours=1)  # Use imported `datetime` directly
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token

    @staticmethod
    def logout_user():
        logger.info("Logging out user")
        return jsonify({"message": "Logged out successfully"}), 200


# Role services
class RoleService:
    @staticmethod
    @token_required
    def create_role(data):
        # Check if the user has permission to create roles
        permission_error = check_permission('manage_roles')  # 'manage_roles' should match the action in your permissions dictionary
        if permission_error:
            return permission_error  # Return the error response if the user lacks permission

        logger.info("Creating a new role with data: %s", data)
        try:
            new_role = Roles(
                name=data.get('name')
            )
            db.session.add(new_role)
            db.session.commit()
            logger.info("Role created successfully: %s", new_role)
            return jsonify({"message": "Role created successfully", "role": {
                "id": new_role.id,
                "name": new_role.name
            }}), 201
        except Exception as e:
            db.session.rollback()
            logger.error("Error creating role: %s", str(e), exc_info=True)
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def get_roles():
        logger.info("Fetching all roles")
        roles = Roles.query.all()
        roles_list = [{"id": role.id, "name": role.name} for role in roles]
        logger.info("Fetched %d roles", len(roles_list))
        return jsonify(roles_list), 200

    @staticmethod
    def get_role(role_id):
        logger.info("Fetching role with ID: %d", role_id)
        role = Roles.query.get_or_404(role_id)
        logger.info("Fetched role: %s", role)
        return jsonify({
            "id": role.id,
            "name": role.name
        }), 200

    @staticmethod
    def update_role(role_id, data):
        logger.info("Updating role with ID: %d", role_id)
        role = Roles.query.get_or_404(role_id)
        try:
            role.name = data.get('name', role.name)
            db.session.commit()
            logger.info("Role updated successfully: %s", role)
            return jsonify({"message": "Role updated successfully"}), 200
        except Exception as e:
            db.session.rollback()
            logger.error("Error updating role: %s", str(e), exc_info=True)
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def delete_role(role_id):
        logger.info("Deleting role with ID: %d", role_id)
        role = Roles.query.get_or_404(role_id)
        try:
            db.session.delete(role)
            db.session.commit()
            logger.info("Role deleted successfully: %s", role)
            return jsonify({"message": "Role deleted successfully"}), 200
        except Exception as e:
            db.session.rollback()
            logger.error("Error deleting role: %s", str(e), exc_info=True)
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def get_logged_in_user_role():
        """
        Retrieve the role of the logged-in user.
        """
        logger.info("Fetching logged-in user's role")
        try:
            # Check if the user is authenticated
            user = g.user
            if not user:
                return jsonify({"error": "User not authenticated"}), 403


            # Return the role of the user
            return jsonify({"role": user.role.name}), 200
        except Exception as e:
            logger.error("Error fetching logged-in user's role: %s", str(e), exc_info=True)
            return jsonify({"error": str(e)}), 400

# Expose services
user_service = UserService()
role_service = RoleService()