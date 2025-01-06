from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger



# Initialize SQLAlchemy and Flask-Migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # MySQL Database Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Mysql%40root4@localhost/edutrack'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    swagger = Swagger(app)
    # Import your route blueprints

    from app.routes.auth_route import auth_routes
    from app.routes.batch_route import batch_routes
    from app.routes.topic_route import topic_routes
    from app.routes.course_route import course_routes
    from app.routes.student_route import student_routes


    # Register route blueprints directly with prefixes
    app.register_blueprint(auth_routes, url_prefix='/auth')  # Auth routes
    app.register_blueprint(batch_routes, url_prefix='/users')  # Batch routes
    app.register_blueprint(topic_routes, url_prefix='/topics')  # Topic routes
    app.register_blueprint(course_routes, url_prefix='/courses')  # Course routes
    app.register_blueprint(student_routes, url_prefix='/students')  # Student routes

    return app

if __name__ == "__main__":
    app = create_app()  # Create the Flask app instance
    app.run(debug=True)  # Run the app in debug mode

