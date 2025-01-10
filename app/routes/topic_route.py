from flask import Blueprint, request
from app.services.topic_services import TopicService

topic_routes = Blueprint('topic_routes', __name__)

@topic_routes.route('/topics', methods=['POST'])
def create_topic():
    """
    Create a New Topic
    ---
    tags:
      - Topics
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: Python Basics
            description:
              type: string
              example: Introduction to Python programming
    responses:
      201:
        description: Topic created successfully
      400:
        description: Bad request
    """
    data = request.json
    return TopicService.create_topic(data)

@topic_routes.route('/topics', methods=['GET'])
def get_topics():
    """
    Get All Topics
    ---
    tags:
      - Topics
    responses:
      200:
        description: List of topics
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
                example: Python Basics
              description:
                type: string
                example: Introduction to Python programming
      500:
        description: Internal server error
    """
    return TopicService.get_topics()

@topic_routes.route('/topics/<int:topic_id>', methods=['GET'])
def get_topic(topic_id):
    """
    Get Topic by ID
    ---
    tags:
      - Topics
    parameters:
      - name: topic_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Topic details
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            name:
              type: string
              example: Python Basics
            description:
              type: string
              example: Introduction to Python programming
      404:
        description: Topic not found
    """
    return TopicService.get_topic(topic_id)

@topic_routes.route('/topics/<int:topic_id>', methods=['PUT'])
def update_topic(topic_id):
    """
    Update Topic by ID
    ---
    tags:
      - Topics
    parameters:
      - name: topic_id
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
              example: Advanced Python
            description:
              type: string
              example: Advanced topics in Python programming
    responses:
      200:
        description: Topic updated successfully
      404:
        description: Topic not found
    """
    data = request.json
    return TopicService.update_topic(topic_id, data)

@topic_routes.route('/topics/<int:topic_id>', methods=['DELETE'])
def delete_topic(topic_id):
    """
    Delete Topic by ID
    ---
    tags:
      - Topics
    parameters:
      - name: topic_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Topic deleted successfully
      404:
        description: Topic not found
    """
    return TopicService.delete_topic(topic_id)
