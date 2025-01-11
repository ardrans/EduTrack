from flask import Blueprint, request
from app.services.student_services import StudentService

student_routes = Blueprint('student_routes', __name__)

@student_routes.route('/students', methods=['POST'])
def create_student():
    """
    Create a New Student
    ---
    tags:
      - Students
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: John Doe
            age:
              type: integer
              example: 21
            email:
              type: string
              example: john.doe@example.com
            course_id:
              type: integer
              example: 1
    responses:
      201:
        description: Student created successfully
      400:
        description: Bad request
    """
    data = request.json
    return StudentService.create_student(data)

@student_routes.route('/students', methods=['GET'])
def get_students():
    """
    Get All Students
    ---
    tags:
      - Students
    responses:
      200:
        description: List of students
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              name:
                type: string
                example: John Doe
              age:
                type: integer
                example: 21
              email:
                type: string
                example: john.doe@example.com
              course_id:
                type: integer
                example: 1
      500:
        description: Internal server error
    """
    return StudentService.get_students()

@student_routes.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """
    Get Student by ID
    ---
    tags:
      - Students
    parameters:
      - name: student_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Student details
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            name:
              type: string
              example: John Doe
            age:
              type: integer
              example: 21
            email:
              type: string
              example: john.doe@example.com
            course_id:
              type: integer
              example: 1
      404:
        description: Student not found
    """
    return StudentService.get_student(student_id)

@student_routes.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """
    Update Student by ID
    ---
    tags:
      - Students
    parameters:
      - name: student_id
        in: path
        required: true
        type: integer
        example: 1
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: Jane Doe
            age:
              type: integer
              example: 22
            email:
              type: string
              example: jane.doe@example.com
            course_id:
              type: integer
              example: 2
    responses:
      200:
        description: Student updated successfully
      404:
        description: Student not found
    """
    data = request.json
    return StudentService.update_student(student_id, data)

@student_routes.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """
    Delete Student by ID
    ---
    tags:
      - Students
    parameters:
      - name: student_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Student deleted successfully
      404:
        description: Student not found
    """
    return StudentService.delete_student(student_id)
