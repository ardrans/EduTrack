from flask import Blueprint, request
from app.services.associations_service import AssociationsService

associations_routes = Blueprint('associations_routes', __name__)

@associations_routes.route('/associations', methods=['POST'])
def create_association():
    """
    Create a New Association
    ---
    tags:
      - Associations
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: Association A
            description:
              type: string
              example: This is an example association
    responses:
      201:
        description: Association created successfully
      400:
        description: Bad request
    """
    data = request.json
    return AssociationsService.create_association(data)

@associations_routes.route('/associations', methods=['GET'])
def get_associations():
    """
    Get All Associations
    ---
    tags:
      - Associations
    responses:
      200:
        description: List of associations
    """
    return AssociationsService.get_associations()

@associations_routes.route('/associations/<int:association_id>', methods=['GET'])
def get_association(association_id):
    """
    Get Association by ID
    ---
    tags:
      - Associations
    """
    return AssociationsService.get_association(association_id)

@associations_routes.route('/associations/<int:association_id>', methods=['PUT'])
def update_association(association_id):
    """
    Update Association by ID
    ---
    tags:
      - Associations
    """
    data = request.json
    return AssociationsService.update_association(association_id, data)

@associations_routes.route('/associations/<int:association_id>', methods=['DELETE'])
def delete_association(association_id):
    """
    Delete Association by ID
    ---
    tags:
      - Associations
    """
    return AssociationsService.delete_association(association_id)