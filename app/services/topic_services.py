from flask import jsonify
from app import db
from app.models import Topics

class TopicService:
    @staticmethod
    def create_topic(data):
        try:
            new_topic = Topics(
                title=data.get('title'),
                content=data.get('content', None),  # Optional
                course_id=data.get('course_id')  # Foreign Key
            )
            db.session.add(new_topic)
            db.session.commit()
            return jsonify({"message": "Topic created successfully", "topic": {
                "id": new_topic.id,
                "title": new_topic.title,
                "content": new_topic.content,
                "course_id": new_topic.course_id
            }}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def get_topics():
        topics = Topics.query.all()
        topic_list = [
            {"id": topic.id, "title": topic.title, "content": topic.content, "course_id": topic.course_id}
            for topic in topics
        ]
        return jsonify(topic_list), 200

    @staticmethod
    def get_topic(topic_id):
        topic = Topics.query.get_or_404(topic_id)
        return jsonify({
            "id": topic.id,
            "title": topic.title,
            "content": topic.content,
            "course_id": topic.course_id
        }), 200

    @staticmethod
    def update_topic(topic_id, data):
        topic = Topics.query.get_or_404(topic_id)
        try:
            topic.title = data.get('title', topic.title)
            topic.content = data.get('content', topic.content)
            topic.course_id = data.get('course_id', topic.course_id)
            db.session.commit()
            return jsonify({"message": "Topic updated successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def delete_topic(topic_id):
        topic = Topics.query.get_or_404(topic_id)
        try:
            db.session.delete(topic)
            db.session.commit()
            return jsonify({"message": "Topic deleted successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
