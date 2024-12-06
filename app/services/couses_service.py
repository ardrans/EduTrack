from flask import jsonify
from app import db
from app.models import Courses

class CourseService:
    @staticmethod
    def create_course(data):
        try:
            new_course = Courses(
                name=data.get('name'),
                description=data.get('description', None)  # Optional
            )
            db.session.add(new_course)
            db.session.commit()
            return jsonify({"message": "Course created successfully", "course": {
                "id": new_course.id,
                "name": new_course.name,
                "description": new_course.description
            }}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def get_courses():
        courses = Courses.query.all()
        course_list = [
            {"id": course.id, "name": course.name, "description": course.description}
            for course in courses
        ]
        return jsonify(course_list), 200

    @staticmethod
    def get_course(course_id):
        course = Courses.query.get_or_404(course_id)
        return jsonify({
            "id": course.id,
            "name": course.name,
            "description": course.description
        }), 200

    @staticmethod
    def update_course(course_id, data):
        course = Courses.query.get_or_404(course_id)
        try:
            course.name = data.get('name', course.name)
            course.description = data.get('description', course.description)
            db.session.commit()
            return jsonify({"message": "Course updated successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def delete_course(course_id):
        course = Courses.query.get_or_404(course_id)
        try:
            db.session.delete(course)
            db.session.commit()
            return jsonify({"message": "Course deleted successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
