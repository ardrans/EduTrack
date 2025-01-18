from flask import request, jsonify, g
import jwt
from functools import wraps

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
            g.user_id = decoded_token.get('user_id')  # Use Flask's g object to store user context
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token!"}), 401

        # Proceed to the wrapped function
        return f(*args, **kwargs)

    return decorated
