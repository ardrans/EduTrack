from flask import request, jsonify
import jwt
from functools import wraps

SECRET_KEY = "edutrack1234"


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({"error": "Token is missing!"}), 401

        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            request.user_id = decoded_token.get('user_id')
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token!"}), 401

        return f(*args, **kwargs)

    return decorated
