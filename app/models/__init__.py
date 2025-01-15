from flask_sqlalchemy import SQLAlchemy

# Initialize the db here
db = SQLAlchemy()

# Import models inside a function or after db is initialized
from .users import Users, Roles
from .batches import Batches
from .courses import Courses, Topics
from .associations import BatchStudents
from .students import Students
