from flask import jsonify
from app.models import db
from app.models import Courses
from app.auth_utils import token_required
from ..logging__config import init_logger

# Set up a logger for the module
logger = init_logger(__name__)

class CourseService:
    @staticmethod
    @token_required
    def create_course(data):
        try:
            logger.info("Attempting to create a new course with data: %s", data)
            new_course = Courses(
                name=data.get('name'),
                description=data.get('description', None)  # Optional
            )
            db.session.add(new_course)
            db.session.commit()
            logger.info("Course created successfully with ID: %s", new_course.id)
            return jsonify({"message": "Course created successfully", "course": {
                "id": new_course.id,
                "name": new_course.name,
                "description": new_course.description
            }}), 201
        except Exception as e:
            logger.error("Error creating course: %s", str(e), exc_info=True)
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @staticmethod
    @token_required
    def get_courses():
        try:
            logger.info("Fetching all courses")
            courses = Courses.query.all()
            course_list = [
                {"id": course.id, "name": course.name, "description": course.description}
                for course in courses
            ]
            logger.info("Fetched %d courses", len(course_list))
            return jsonify(course_list), 200
        except Exception as e:
            logger.error("Error fetching courses: %s", str(e), exc_info=True)
            return jsonify({"error": str(e)}), 400

    @staticmethod
    @token_required
    def get_course(course_id):
        try:
            logger.info("Fetching course with ID: %s", course_id)
            course = Courses.query.get_or_404(course_id)
            logger.info("Fetched course: %s", course_id)
            return jsonify({
                "id": course.id,
                "name": course.name,
                "description": course.description
            }), 200
        except Exception as e:
            logger.error("Error fetching course with ID %s: %s", course_id, str(e), exc_info=True)
            return jsonify({"error": str(e)}), 400

    @staticmethod
    @token_required
    def update_course(course_id, data):
        course = Courses.query.get_or_404(course_id)
        try:
            logger.info("Updating course with ID: %s with data: %s", course_id, data)
            course.name = data.get('name', course.name)
            course.description = data.get('description', course.description)
            db.session.commit()
            logger.info("Course updated successfully with ID: %s", course_id)
            return jsonify({"message": "Course updated successfully"}), 200
        except Exception as e:
            logger.error("Error updating course with ID %s: %s", course_id, str(e), exc_info=True)
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @staticmethod
    @token_required
    def delete_course(course_id):
        course = Courses.query.get_or_404(course_id)
        try:
            logger.info("Deleting course with ID: %s", course_id)
            db.session.delete(course)
            db.session.commit()
            logger.info("Course deleted successfully with ID: %s", course_id)
            return jsonify({"message": "Course deleted successfully"}), 200
        except Exception as e:
            logger.error("Error deleting course with ID %s: %s", course_id, str(e), exc_info=True)
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
