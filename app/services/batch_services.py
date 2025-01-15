from flask import jsonify
from app.models import db
from app.models import Batches
from app.auth_utils import token_required
from ..logging__config import init_logger
# Set up a logger for the module
logger = init_logger(__name__)

class BatchService:
    @staticmethod
    @token_required
    def create_batch(data):
        try:
            logger.info("Attempting to create a new batch with data: %s", data)
            new_batch = Batches(
                name=data.get('name'),
                start_date=data.get('start_date'),
                end_date=data.get('end_date')
            )
            db.session.add(new_batch)
            db.session.commit()
            logger.info("Batch created successfully with ID: %s", new_batch.id)
            return jsonify({"message": "Batch created successfully", "batch": {
                "id": new_batch.id,
                "name": new_batch.name,
                "start_date": new_batch.start_date,
                "end_date": new_batch.end_date
            }}), 201
        except Exception as e:
            logger.error("Error creating batch: %s", str(e), exc_info=True)
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @staticmethod
    @token_required
    def get_batches():
        try:
            logger.info("Fetching all batches")
            batches = Batches.query.all()
            batches_list = [
                {"id": batch.id, "name": batch.name, "start_date": batch.start_date, "end_date": batch.end_date}
                for batch in batches
            ]
            logger.info("Fetched %d batches", len(batches_list))
            return jsonify(batches_list), 200
        except Exception as e:
            logger.error("Error fetching batches: %s", str(e), exc_info=True)
            return jsonify({"error": str(e)}), 400

    @staticmethod
    @token_required
    def get_batch(batch_id):
        try:
            logger.info("Fetching batch with ID: %s", batch_id)
            batch = Batches.query.get_or_404(batch_id)
            logger.info("Fetched batch with ID: %s", batch_id)
            return jsonify({
                "id": batch.id,
                "name": batch.name,
                "start_date": batch.start_date,
                "end_date": batch.end_date
            }), 200
        except Exception as e:
            logger.error("Error fetching batch with ID %s: %s", batch_id, str(e), exc_info=True)
            return jsonify({"error": str(e)}), 400

    @staticmethod
    @token_required
    def update_batch(batch_id, data):
        batch = Batches.query.get_or_404(batch_id)
        try:
            logger.info("Updating batch with ID: %s with data: %s", batch_id, data)
            batch.name = data.get('name', batch.name)
            batch.start_date = data.get('start_date', batch.start_date)
            batch.end_date = data.get('end_date', batch.end_date)
            db.session.commit()
            logger.info("Batch updated successfully with ID: %s", batch_id)
            return jsonify({"message": "Batch updated successfully"}), 200
        except Exception as e:
            logger.error("Error updating batch with ID %s: %s", batch_id, str(e), exc_info=True)
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @staticmethod
    @token_required
    def delete_batch(batch_id):
        batch = Batches.query.get_or_404(batch_id)
        try:
            logger.info("Deleting batch with ID: %s", batch_id)
            db.session.delete(batch)
            db.session.commit()
            logger.info("Batch deleted successfully with ID: %s", batch_id)
            return jsonify({"message": "Batch deleted successfully"}), 200
        except Exception as e:
            logger.error("Error deleting batch with ID %s: %s", batch_id, str(e), exc_info=True)
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
