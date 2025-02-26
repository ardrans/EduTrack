from flask import jsonify
from app.models import db, Batches, Students, BatchStudents
from app.auth_utils import token_required
from ..logging__config import init_logger

logger = init_logger(__name__)


class BatchStudentService:
    @staticmethod
    @token_required
    def get_students_by_batch(batch_id):
        """Fetch all students in a given batch."""
        try:
            students = (
                db.session.query(Students)
                .join(BatchStudents, Students.id == BatchStudents.student_id)  # Explicit join condition
                .filter(BatchStudents.batch_id == batch_id)
                .all()
            )

            return jsonify({'students': [{'id': student.id, 'name': student.name, 'email': student.email} for student in
                                         students]}), 200
        except Exception as e:
            logger.error(f"Error fetching students for batch {batch_id}: {str(e)}")
            return jsonify({'error': str(e)}), 500

    @staticmethod
    @token_required
    def get_batches_by_student(student_id):
        """Fetch all batches a given student is enrolled in."""
        try:
            batches = db.session.query(Batches).join(BatchStudents).filter(BatchStudents.student_id == student_id).all()
            return jsonify({'batches': [{'id': batch.id, 'name': batch.name} for batch in batches]}), 200
        except Exception as e:
            logger.error(f"Error fetching batches for student {student_id}: {str(e)}")
            return jsonify({'error': str(e)}), 500

    @staticmethod
    @token_required
    def get_all_batches_with_students():
        """Fetch all batches along with their enrolled students."""
        try:
            batches = Batches.query.all()
            batch_data = {}

            for batch in batches:
                students = (
                    db.session.query(Students)
                    .join(BatchStudents, Students.id == BatchStudents.student_id)
                    .filter(BatchStudents.batch_id == batch.id)
                    .all()
                )

                batch_data[batch.name] = [{'id': student.id, 'name': student.name, 'email': student.email} for student
                                          in students]

            return jsonify({'batches': batch_data}), 200
        except Exception as e:
            logger.error(f"Error fetching all batches with students: {str(e)}")
            return jsonify({'error': str(e)}), 500

    @staticmethod
    @token_required
    def create_association(data):
        """Create a new batch-student association."""
        try:
            batch_name = data.get('batch_name')
            student_email = data.get('student_email')

            if not batch_name or not student_email:
                return jsonify({'error': 'batch_name and student_email are required'}), 400

            # Fetch batch and student using correct tables
            batch = Batches.query.filter_by(name=batch_name).first()
            student = Students.query.filter_by(email=student_email).first()

            if not batch:
                return jsonify({'error': 'Batch not found'}), 404
            if not student:
                return jsonify({'error': 'Student not found'}), 404

            # Check if association already exists
            existing_association = BatchStudents.query.filter_by(batch_id=batch.id, student_id=student.id).first()
            if existing_association:
                return jsonify({'error': 'Association already exists'}), 400

            # Create and commit new association
            new_association = BatchStudents(batch_id=batch.id, student_id=student.id)
            db.session.add(new_association)
            db.session.commit()

            return jsonify({
                'message': 'Association created successfully',
                'association': {
                    'id': new_association.id,
                    'batch_id': new_association.batch_id,
                    'student_id': new_association.student_id
                }
            }), 201

        except Exception as e:
            db.session.rollback()  # Rollback in case of an error
            logger.error(f"Error creating association: {str(e)}")
            return jsonify({'error': str(e)}), 500

    @staticmethod
    @token_required
    def delete_association(association_id):
        """Delete a batch-student association."""
        try:
            association = BatchStudents.query.get(association_id)

            if not association:
                return jsonify({'error': 'Association not found'}), 404

            # Delete and commit changes
            db.session.delete(association)
            db.session.commit()

            return jsonify({'message': 'Association deleted successfully'}), 200

        except Exception as e:
            db.session.rollback()  # Rollback in case of failure
            logger.error(f"Error deleting association {association_id}: {str(e)}")
            return jsonify({'error': str(e)}), 500