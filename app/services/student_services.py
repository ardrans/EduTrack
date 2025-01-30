from flask import jsonify
from app.models import db
from app.models import Students
from app.auth_utils import token_required
from ..logging__config import init_logger

# Set up logger for this module
logger = init_logger(__name__)

class StudentService:
    @staticmethod
    @token_required
    def create_student(data):
        try:
            logger.info("Attempting to create a new student with data: %s", data)
            new_student = Students(
                name=data.get('name'),
                email=data.get('email'),
                phone=data.get('phone'),
                profile_picture=data.get('profile_picture', None)  # Optional
            )
            db.session.add(new_student)
            db.session.commit()
            logger.info("Student created successfully with ID: %s", new_student.id)
            return jsonify({"message": "Student created successfully", "student": {
                "id": new_student.id,
                "name": new_student.name,
                "email": new_student.email,
                "phone": new_student.phone,
                "profile_picture": new_student.profile_picture
            }}), 201
        except Exception as e:
            logger.error("Error creating student: %s", str(e), exc_info=True)
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    @staticmethod
    @token_required
    def get_students():
        try:
            logger.info("Fetching all students")
            students = Students.query.all()
            total_students = len(students)  # Get the total count of students
            student_list = [
                {"id": student.id, "name": student.name, "email": student.email, "phone": student.phone,
                 "profile_picture": student.profile_picture}
                for student in students
            ]
            logger.info("Fetched %d students", total_students)
            return jsonify({"total_students": total_students, "students": student_list}), 200
        except Exception as e:
            logger.error("Error fetching students: %s", str(e), exc_info=True)
            return jsonify({"error": str(e)}), 400

    @staticmethod
    @token_required
    def get_student(student_id):
        try:
            logger.info("Fetching student with ID: %s", student_id)
            student = Students.query.get_or_404(student_id)
            return jsonify({
                "id": student.id,
                "name": student.name,
                "email": student.email,
                "phone": student.phone,
                "profile_picture": student.profile_picture
            }), 200
        except Exception as e:
            logger.error("Error fetching student with ID %s: %s", student_id, str(e), exc_info=True)
            return jsonify({"error": str(e)}), 400

    @staticmethod
    @token_required
    def update_student(student_id, data):
        student = Students.query.get_or_404(student_id)
        try:
            logger.info("Updating student with ID: %s with data: %s", student_id, data)
            student.name = data.get('name', student.name)
            student.email = data.get('email', student.email)
            student.phone = data.get('phone', student.phone)
            student.profile_picture = data.get('profile_picture', student.profile_picture)
            db.session.commit()
            logger.info("Student updated successfully with ID: %s", student_id)
            return jsonify({"message": "Student updated successfully"}), 200
        except Exception as e:
            logger.error("Error updating student with ID %s: %s", student_id, str(e), exc_info=True)
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @staticmethod
    @token_required
    def delete_student(student_id):
        student = Students.query.get_or_404(student_id)
        try:
            logger.info("Deleting student with ID: %s", student_id)
            db.session.delete(student)
            db.session.commit()
            logger.info("Student deleted successfully with ID: %s", student_id)
            return jsonify({"message": "Student deleted successfully"}), 200
        except Exception as e:
            logger.error("Error deleting student with ID %s: %s", student_id, str(e), exc_info=True)
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
