from flask import jsonify
from app import db
from app.models import Students

class StudentService:
    @staticmethod
    def create_student(data):
        try:
            new_student = Students(
                name=data.get('name'),
                email=data.get('email'),
                phone=data.get('phone'),
                profile_picture=data.get('profile_picture', None)  # Optional
            )
            db.session.add(new_student)
            db.session.commit()
            return jsonify({"message": "Student created successfully", "student": {
                "id": new_student.id,
                "name": new_student.name,
                "email": new_student.email,
                "phone": new_student.phone,
                "profile_picture": new_student.profile_picture
            }}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def get_students():
        students = Students.query.all()
        student_list = [
            {"id": student.id, "name": student.name, "email": student.email, "phone": student.phone,
             "profile_picture": student.profile_picture}
            for student in students
        ]
        return jsonify(student_list), 200

    @staticmethod
    def get_student(student_id):
        student = Students.query.get_or_404(student_id)
        return jsonify({
            "id": student.id,
            "name": student.name,
            "email": student.email,
            "phone": student.phone,
            "profile_picture": student.profile_picture
        }), 200

    @staticmethod
    def update_student(student_id, data):
        student = Students.query.get_or_404(student_id)
        try:
            student.name = data.get('name', student.name)
            student.email = data.get('email', student.email)
            student.phone = data.get('phone', student.phone)
            student.profile_picture = data.get('profile_picture', student.profile_picture)
            db.session.commit()
            return jsonify({"message": "Student updated successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def delete_student(student_id):
        student = Students.query.get_or_404(student_id)
        try:
            db.session.delete(student)
            db.session.commit()
            return jsonify({"message": "Student deleted successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
