from flask import Blueprint, request, jsonify
from app.services.associations_service import BatchStudentService
from app.auth_utils import token_required
from ..logging__config import init_logger

logger = init_logger(__name__)

associations_routes = Blueprint('associations_routes', __name__)

@associations_routes.route('/associations', methods=['POST'])
def create_association():
    """Create a new batch-student association."""
    try:
        data = request.json
        return BatchStudentService.create_association(data)
    except Exception as e:
        logger.error(f"Error in create_association: {str(e)}")
        return jsonify({'error': str(e)}), 500

@associations_routes.route('/associations/<int:association_id>', methods=['DELETE'])
def delete_association(association_id):
    """Delete a batch-student association."""
    try:
        return BatchStudentService.delete_association(association_id)
    except Exception as e:
        logger.error(f"Error in delete_association: {str(e)}")
        return jsonify({'error': str(e)}), 500

@associations_routes.route('/associations/batch/<int:batch_id>', methods=['GET'])
def get_students_by_batch(batch_id):
    """Fetch all students in a given batch."""
    try:
        return BatchStudentService.get_students_by_batch(batch_id)
    except Exception as e:
        logger.error(f"Error in get_students_by_batch: {str(e)}")
        return jsonify({'error': str(e)}), 500

@associations_routes.route('/associations/student/<int:student_id>', methods=['GET'])
def get_batches_by_student(student_id):
    """Fetch all batches a student is enrolled in."""
    try:
        return BatchStudentService.get_batches_by_student(student_id)
    except Exception as e:
        logger.error(f"Error in get_batches_by_student: {str(e)}")
        return jsonify({'error': str(e)}), 500

@associations_routes.route('/associations/all', methods=['GET'])
def get_all_batches_with_students():
    """Fetch all batches along with their enrolled students."""
    try:
        return BatchStudentService.get_all_batches_with_students()
    except Exception as e:
        logger.error(f"Error in get_all_batches_with_students: {str(e)}")
        return jsonify({'error': str(e)}), 500