from app.models import db

class Students(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    profile_picture = db.Column(db.String(255), nullable=True)
    placed = db.Column(db.Boolean, default=False)  # New field

    def __repr__(self):
        return f"<Student {self.name} (ID: {self.id})>"
