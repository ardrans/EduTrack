from flask import jsonify
from app import db
from app.models import Batches

class BatchService:
    @staticmethod
    def create_batch(data):
        try:
            new_batch = Batches(
                name=data.get('name'),
                start_date=data.get('start_date'),
                end_date=data.get('end_date')
            )
            db.session.add(new_batch)
            db.session.commit()
            return jsonify({"message": "Batch created successfully", "batch": {
                "id": new_batch.id,
                "name": new_batch.name,
                "start_date": new_batch.start_date,
                "end_date": new_batch.end_date
            }}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def get_batches():
        batches = Batches.query.all()
        batches_list = [
            {"id": batch.id, "name": batch.name, "start_date": batch.start_date, "end_date": batch.end_date}
            for batch in batches
        ]
        return jsonify(batches_list), 200

    @staticmethod
    def get_batch(batch_id):
        batch = Batches.query.get_or_404(batch_id)
        return jsonify({
            "id": batch.id,
            "name": batch.name,
            "start_date": batch.start_date,
            "end_date": batch.end_date
        }), 200

    @staticmethod
    def update_batch(batch_id, data):
        batch = Batches.query.get_or_404(batch_id)
        try:
            batch.name = data.get('name', batch.name)
            batch.start_date = data.get('start_date', batch.start_date)
            batch.end_date = data.get('end_date', batch.end_date)
            db.session.commit()
            return jsonify({"message": "Batch updated successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def delete_batch(batch_id):
        batch = Batches.query.get_or_404(batch_id)
        try:
            db.session.delete(batch)
            db.session.commit()
            return jsonify({"message": "Batch deleted successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
