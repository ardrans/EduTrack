from flask import Blueprint, request
from app.services.couses_service import CourseService

course_routes = Blueprint('course_routes', __name__)

@course_routes.route('/courses', methods=['POST'])
def create_course():
    """
    Create a New Course
    ---
    tags:
      - Courses
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              example: Introduction to Python
            description:
              type: string
              example: A beginner-friendly Python course
            duration:
              type: integer
              example: 30
    responses:
      201:
        description: Course created successfully
      400:
        description: Bad request
    """
    data = request.json
    return CourseService.create_course(data)

@course_routes.route('/courses', methods=['GET'])
def get_courses():
    """
    Get All Courses
    ---
    tags:
      - Courses
    responses:
      200:
        description: List of courses
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              title:
                type: string
                example: Introduction to Python
              description:
                type: string
                example: A beginner-friendly Python course
              duration:
                type: integer
                example: 30
      500:
        description: Internal server error
    """
    return CourseService.get_courses()

@course_routes.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Get Course by ID
    ---
    tags:
      - Courses
    parameters:
      - name: course_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Course details
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            title:
              type: string
              example: Introduction to Python
            description:
              type: string
              example: A beginner-friendly Python course
            duration:
              type: integer
              example: 30
      404:
        description: Course not found
    """
    return CourseService.get_course(course_id)

@course_routes.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    """
    Update Course by ID
    ---
    tags:
      - Courses
    parameters:
      - name: course_id
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
            title:
              type: string
              example: Advanced Python
            description:
              type: string
              example: An advanced course on Python
            duration:
              type: integer
              example: 45
    responses:
      200:
        description: Course updated successfully
      404:
        description: Course not found
    """
    data = request.json
    return CourseService.update_course(course_id, data)

@course_routes.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    """
    Delete Course by ID
    ---
    tags:
      - Courses
    parameters:
      - name: course_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Course deleted successfully
      404:
        description: Course not found
    """
    return CourseService.delete_course(course_id)
