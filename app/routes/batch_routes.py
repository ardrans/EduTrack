from flask import Blueprint, request
from app.services.batch_services import BatchService

batch_routes = Blueprint('batch_routes', __name__)

@batch_routes.route('/batches', methods=['POST'])
def create_batch():
    data = request.json
    return BatchService.create_batch(data)

@batch_routes.route('/batches', methods=['GET'])
def get_batches():
    return BatchService.get_batches()

@batch_routes.route('/batches/<int:batch_id>', methods=['GET'])
def get_batch(batch_id):
    return BatchService.get_batch(batch_id)

@batch_routes.route('/batches/<int:batch_id>', methods=['PUT'])
def update_batch(batch_id):
    data = request.json
    return BatchService.update_batch(batch_id, data)

@batch_routes.route('/batches/<int:batch_id>', methods=['DELETE'])
def delete_batch(batch_id):
    return BatchService.delete_batch(batch_id)
