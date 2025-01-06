from flask import Blueprint, request
from app.services.student_services import StudentService

student_routes = Blueprint('student_routes', __name__)

@student_routes.route('/students', methods=['POST'])
def create_student():
    data = request.json
    return StudentService.create_student(data)

@student_routes.route('/students', methods=['GET'])
def get_students():
    return StudentService.get_students()

@student_routes.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    return StudentService.get_student(student_id)

@student_routes.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.json
    return StudentService.update_student(student_id, data)

@student_routes.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    return StudentService.delete_student(student_id)
