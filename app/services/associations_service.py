from flask import jsonify
from app.models import db, BatchStudents
from app.auth_utils import token_required
from ..logging__config import init_logger

logger = init_logger(__name__)

class AssociationsService:
    @staticmethod
    @token_required
    def create_association(data):
        try:
            logger.info("Creating a new association: %s", data)
            new_association = BatchStudents(
                name=data.get('name'),
                description=data.get('description')
            )
            db.session.add(new_association)
            db.session.commit()
            logger.info("Association created with ID: %s", new_association.id)
            return jsonify({"message": "Association created successfully", "association": {
                "id": new_association.id,
                "name": new_association.name,
                "description": new_association.description
            }}), 201
        except Exception as e:
            logger.error("Error creating association: %s", str(e), exc_info=True)
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @staticmethod
    @token_required
    def get_associations():
        try:
            logger.info("Fetching all associations")
            associations = BatchStudents.query.all()
            associations_list = [
                {"id": assoc.id, "name": assoc.name, "description": assoc.description}
                for assoc in associations
            ]
            logger.info("Fetched %d associations", len(associations_list))
            return jsonify(associations_list), 200
        except Exception as e:
            logger.error("Error fetching associations: %s", str(e), exc_info=True)
            return jsonify({"error": str(e)}), 400

    @staticmethod
    @token_required
    def get_association(association_id):
        try:
            logger.info("Fetching association with ID: %s", association_id)
            association = BatchStudents.query.get_or_404(association_id)
            return jsonify({
                "id": association.id,
                "name": association.name,
                "description": association.description
            }), 200
        except Exception as e:
            logger.error("Error fetching association with ID %s: %s", association_id, str(e), exc_info=True)
            return jsonify({"error": str(e)}), 400

    @staticmethod
    @token_required
    def update_association(association_id, data):
        association = BatchStudents.query.get_or_404(association_id)
        try:
            logger.info("Updating association ID: %s with data: %s", association_id, data)
            association.name = data.get('name', association.name)
            association.description = data.get('description', association.description)
            db.session.commit()
            return jsonify({"message": "Association updated successfully"}), 200
        except Exception as e:
            logger.error("Error updating association ID %s: %s", association_id, str(e), exc_info=True)
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @staticmethod
    @token_required
    def delete_association(association_id):
        association = BatchStudents.query.get_or_404(association_id)
        try:
            logger.info("Deleting association with ID: %s", association_id)
            db.session.delete(association)
            db.session.commit()
            return jsonify({"message": "Association deleted successfully"}), 200
        except Exception as e:
            logger.error("Error deleting association ID %s: %s", association_id, str(e), exc_info=True)
            db.session.rollback()
            return jsonify({"error": str(e)}), 400