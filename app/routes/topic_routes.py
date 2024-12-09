from flask import Blueprint, request
from app.services.topic_services import TopicService

topic_routes = Blueprint('topic_routes', __name__)

@topic_routes.route('/topics', methods=['POST'])
def create_topic():
    data = request.json
    return TopicService.create_topic(data)

@topic_routes.route('/topics', methods=['GET'])
def get_topics():
    return TopicService.get_topics()

@topic_routes.route('/topics/<int:topic_id>', methods=['GET'])
def get_topic(topic_id):
    return TopicService.get_topic(topic_id)

@topic_routes.route('/topics/<int:topic_id>', methods=['PUT'])
def update_topic(topic_id):
    data = request.json
    return TopicService.update_topic(topic_id, data)

@topic_routes.route('/topics/<int:topic_id>', methods=['DELETE'])
def delete_topic(topic_id):
    return TopicService.delete_topic(topic_id)
