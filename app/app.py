from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
import os
from dotenv import load_dotenv
from flask_cors import CORS
from app.models import db  # Import the `db` instance from models
from .auth_utils import get_logged_in_user_from_token

# Initialize extensions
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    # Load environment variables
    load_dotenv()

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Enable Cross-Origin Resource Sharing
    CORS(app, resources={r"/*": {
        "origins": "http://localhost:3000",  # Frontend origin
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }})

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    Swagger(app)

    # Register the before_request function to load user info
    @app.before_request
    def load_user():
        """
        Load the logged-in user before each request, if authenticated.
        """
        g.user = get_logged_in_user_from_token()  # Replace with your logic to get the user (e.g., from the request token)

    # Import blueprints after app and db initialization
    with app.app_context():
        from app.routes.auth_route import auth_routes
        from app.routes.batch_route import batch_routes
        from app.routes.topic_route import topic_routes
        from app.routes.course_route import course_routes
        from app.routes.student_route import student_routes

        # Register blueprints
        app.register_blueprint(auth_routes, url_prefix='/auth')
        app.register_blueprint(batch_routes, url_prefix='/users')
        app.register_blueprint(topic_routes, url_prefix='/topics')
        app.register_blueprint(course_routes, url_prefix='/courses')
        app.register_blueprint(student_routes, url_prefix='/students')

    return app


# Create the app instance globally accessible
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
