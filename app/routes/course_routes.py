from flask import Blueprint, request
from app.services.course_services import CourseService

course_routes = Blueprint('course_routes', __name__)

@course_routes.route('/courses', methods=['POST'])
def create_course():
    data = request.json
    return CourseService.create_course(data)

@course_routes.route('/courses', methods=['GET'])
def get_courses():
    return CourseService.get_courses()

@course_routes.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    return CourseService.get_course(course_id)

@course_routes.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    data = request.json
    return CourseService.update_course(course_id, data)

@course_routes.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    return CourseService.delete_course(course_id)
