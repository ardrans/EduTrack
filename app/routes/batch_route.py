from flask import Blueprint, request
from app.services.batch_services import BatchService

batch_routes = Blueprint('batch_routes', __name__)

@batch_routes.route('/batches', methods=['POST'])
def create_batch():
    """
    Create a New Batch
    ---
    tags:
      - Batches
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: Batch A
            start_date:
              type: string
              format: date
              example: 2025-01-01
            end_date:
              type: string
              format: date
              example: 2025-06-30
    responses:
      201:
        description: Batch created successfully
      400:
        description: Bad request
    """
    data = request.json
    return BatchService.create_batch(data)

@batch_routes.route('/batches', methods=['GET'])
def get_batches():
    """
    Get All Batches
    ---
    tags:
      - Batches
    responses:
      200:
        description: List of batches
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
                example: Batch A
              start_date:
                type: string
                format: date
                example: 2025-01-01
              end_date:
                type: string
                format: date
                example: 2025-06-30
      500:
        description: Internal server error
    """
    return BatchService.get_batches()

@batch_routes.route('/batches/<int:batch_id>', methods=['GET'])
def get_batch(batch_id):
    """
    Get Batch by ID
    ---
    tags:
      - Batches
    parameters:
      - name: batch_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Batch details
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            name:
              type: string
              example: Batch A
            start_date:
              type: string
              format: date
              example: 2025-01-01
            end_date:
              type: string
              format: date
              example: 2025-06-30
      404:
        description: Batch not found
    """
    return BatchService.get_batch(batch_id)

@batch_routes.route('/batches/<int:batch_id>', methods=['PUT'])
def update_batch(batch_id):
    """
    Update Batch by ID
    ---
    tags:
      - Batches
    parameters:
      - name: batch_id
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
              example: Batch A
            start_date:
              type: string
              format: date
              example: 2025-01-01
            end_date:
              type: string
              format: date
              example: 2025-06-30
    responses:
      200:
        description: Batch updated successfully
      404:
        description: Batch not found
    """
    data = request.json
    return BatchService.update_batch(batch_id, data)

@batch_routes.route('/batches/<int:batch_id>', methods=['DELETE'])
def delete_batch(batch_id):
    """
    Delete Batch by ID
    ---
    tags:
      - Batches
    parameters:
      - name: batch_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Batch deleted successfully
      404:
        description: Batch not found
    """
    return BatchService.delete_batch(batch_id)
