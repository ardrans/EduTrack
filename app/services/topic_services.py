from flask import jsonify
from app.app import db
from app.models import Topics
from app.auth_utils import token_required
from ..logging__config import init_logger

# Set up a logger for the module
logger = init_logger(__name__)

class TopicService:
    @staticmethod
    @token_required
    def create_topic(data):
        try:
            logger.info("Attempting to create a new topic with data: %s", data)
            new_topic = Topics(
                title=data.get('title'),
                content=data.get('content', None),
                course_id=data.get('course_id')
            )
            db.session.add(new_topic)
            db.session.commit()
            logger.info("Topic created successfully with ID: %s", new_topic.id)
            return jsonify({"message": "Topic created successfully", "topic": {
                "id": new_topic.id,
                "title": new_topic.title,
                "content": new_topic.content,
                "course_id": new_topic.course_id
            }}), 201
        except Exception as e:
            logger.error("Error creating topic: %s", str(e), exc_info=True)
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @staticmethod
    @token_required
    def get_topics():
        try:
            logger.info("Fetching all topics")
            topics = Topics.query.all()
            topic_list = [
                {"id": topic.id, "title": topic.title, "content": topic.content, "course_id": topic.course_id}
                for topic in topics
            ]
            logger.info("Fetched %d topics", len(topic_list))
            return jsonify(topic_list), 200
        except Exception as e:
            logger.error("Error fetching topics: %s", str(e), exc_info=True)
            return jsonify({"error": str(e)}), 400

    @staticmethod
    @token_required
    def get_topic(topic_id):
        try:
            logger.info("Fetching topic with ID: %s", topic_id)
            topic = Topics.query.get_or_404(topic_id)
            logger.info("Fetched topic: %s", topic_id)
            return jsonify({
                "id": topic.id,
                "title": topic.title,
                "content": topic.content,
                "course_id": topic.course_id
            }), 200
        except Exception as e:
            logger.error("Error fetching topic with ID %s: %s", topic_id, str(e), exc_info=True)
            return jsonify({"error": str(e)}), 400

    @staticmethod
    @token_required
    def update_topic(topic_id, data):
        topic = Topics.query.get_or_404(topic_id)
        try:
            logger.info("Updating topic with ID: %s with data: %s", topic_id, data)
            topic.title = data.get('title', topic.title)
            topic.content = data.get('content', topic.content)
            topic.course_id = data.get('course_id', topic.course_id)
            db.session.commit()
            logger.info("Topic updated successfully with ID: %s", topic_id)
            return jsonify({"message": "Topic updated successfully"}), 200
        except Exception as e:
            logger.error("Error updating topic with ID %s: %s", topic_id, str(e), exc_info=True)
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @staticmethod
    @token_required
    def delete_topic(topic_id):
        topic = Topics.query.get_or_404(topic_id)
        try:
            logger.info("Deleting topic with ID: %s", topic_id)
            db.session.delete(topic)
            db.session.commit()
            logger.info("Topic deleted successfully with ID: %s", topic_id)
            return jsonify({"message": "Topic deleted successfully"}), 200
        except Exception as e:
            logger.error("Error deleting topic with ID %s: %s", topic_id, str(e), exc_info=True)
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
