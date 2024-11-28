from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.routes import register_routes

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

    # Import and register models
    from app.models import Users, Batches, Courses, BatchStudents
    register_routes(app)

    # You can also register Blueprints here if you have any routes defined in `routes/`
    return app
