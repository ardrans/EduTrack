from flask import request, g, jsonify
import jwt
from app.models import Users  # Import your user model
from functools import wraps

# Secret key for JWT
SECRET_KEY = "edutrack1234"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Extract token from Authorization header
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({"error": "Authorization header is missing!"}), 401

        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Invalid token format! Expected 'Bearer <token>'"}), 401

        token = auth_header.split(" ")[1]  # Extract the token part
        try:
            # Decode the token
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user_id = decoded_token.get('user_id')  # Extract user_id from the token

            # Fetch the user from the database
            user = Users.query.get(user_id)  # Replace with your ORM query
            if not user:
                return jsonify({"error": "User not found!"}), 404

            # Attach the user to the Flask `g` object
            g.user = user

        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token!"}), 401

        # Proceed to the wrapped function
        return f(*args, **kwargs)

    return decorated

def get_logged_in_user_from_token():
    """
    Extracts the user from the token in the Authorization header.
    Returns the user if valid, otherwise None.
    """
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith("Bearer "):
        return None

    token = auth_header.split(" ")[1]
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_id = decoded_token.get('user_id')
        user = Users.query.get(user_id)  # Replace with your ORM query
        return user
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, Exception):
        return None
