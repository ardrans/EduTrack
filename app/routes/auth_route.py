from flask import Blueprint, request
from app.services.auth_services import user_service, role_service

auth_routes = Blueprint('auth', __name__)

# User routes
@auth_routes.route('/users', methods=['POST'])
def create_user():
    """
    Create a New User
    ---
    tags:
      - Users
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: John Doe
            email:
              type: string
              example: john.doe@example.com
            password:
              type: string
              example: mysecurepassword
    responses:
      201:
        description: User created successfully
      400:
        description: Bad request
    """
    data = request.json
    return user_service.create_user(data)

@auth_routes.route('/users', methods=['GET'])
def get_users():
    """
    Get All Users
    ---
    tags:
      - Users
    responses:
      200:
        description: List of users
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              name:
                type: string
                example: John Doe
              email:
                type: string
                example: john.doe@example.com
      500:
        description: Internal server error
    """
    return user_service.get_users()

@auth_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get User by ID
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: User details
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            name:
              type: string
              example: John Doe
            email:
              type: string
              example: john.doe@example.com
      404:
        description: User not found
    """
    return user_service.get_user(user_id)

@auth_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update User by ID
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        required: true
        type: integer
        example: 1
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: John Doe
            email:
              type: string
              example: john.doe@example.com
    responses:
      200:
        description: User updated successfully
      404:
        description: User not found
    """
    data = request.json
    return user_service.update_user(user_id, data)

@auth_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete User by ID
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: User deleted successfully
      404:
        description: User not found
    """
    return user_service.delete_user(user_id)

@auth_routes.route('/users/count', methods=['GET'])
def get_trainers_count():
    """
    Delete User by ID
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: User deleted successfully
      404:
        description: User not found
    """
    return user_service.get_trainers_count()

@auth_routes.route('/users/trainers', methods=['GET'])
def get_trainers():
    """
    Delete User by ID
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: User deleted successfully
      404:
        description: User not found
    """
    return user_service.get_trainers()

@auth_routes.route('/login', methods=['POST'])
def login():
    """
    User Login
    ---
    tags:
      - Authentication
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
              example: john.doe@example.com
            password:
              type: string
              example: mysecurepassword
    responses:
      200:
        description: Login successful
      401:
        description: Unauthorized
    """
    data = request.get_json()
    return user_service.login_user(data)


@auth_routes.route('/logout', methods=['POST'])
def logout():
    """
    User Logout
    ---
    tags:
      - Authentication
    responses:
      200:
        description: Logout successful
    """
    return user_service.logout_user()

# Role routes
@auth_routes.route('/roles', methods=['POST'])
def create_role():
    """
    Create a New Role
    ---
    tags:
      - Roles
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            role_name:
              type: string
              example: Admin
    responses:
      201:
        description: Role created successfully
      400:
        description: Bad request
    """
    data = request.json
    return role_service.create_role(data)

@auth_routes.route('/roles', methods=['GET'])
def get_roles():
    """
    Get All Roles
    ---
    tags:
      - Roles
    responses:
      200:
        description: List of roles
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              role_name:
                type: string
                example: Admin
      500:
        description: Internal server error
    """
    return role_service.get_roles()

@auth_routes.route('/roles/<int:role_id>', methods=['GET'])
def get_role(role_id):
    """
    Get Role by ID
    ---
    tags:
      - Roles
    parameters:
      - name: role_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Role details
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            role_name:
              type: string
              example: Admin
      404:
        description: Role not found
    """
    return role_service.get_role(role_id)

@auth_routes.route('/roles/<int:role_id>', methods=['PUT'])
def update_role(role_id):
    """
    Update Role by ID
    ---
    tags:
      - Roles
    parameters:
      - name: role_id
        in: path
        required: true
        type: integer
        example: 1
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            role_name:
              type: string
              example: Admin
    responses:
      200:
        description: Role updated successfully
      404:
        description: Role not found
    """
    data = request.json
    return role_service.update_role(role_id, data)

@auth_routes.route('/roles/<int:role_id>', methods=['DELETE'])
def delete_role(role_id):
    """
    Delete Role by ID
    ---
    tags:
      - Roles
    parameters:
      - name: role_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Role deleted successfully
      404:
        description: Role not found
    """
    return role_service.delete_role(role_id)

@auth_routes.route('/user-role', methods=['GET'])
def get_user_role():
    """
    Get the logged-in user's role
    ---
    tags:
      - Roles
    responses:
      200:
        description: Successfully retrieved the user's role
      403:
        description: Permission denied
    """
    return role_service.get_logged_in_user_role()




