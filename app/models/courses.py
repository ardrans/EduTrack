from app import db

class Courses(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    duration = db.Column(db.Integer)  # Duration in hours

    topics = db.relationship('Topics', back_populates='course')
    batches = db.relationship('Batches', backref='course')

    def __repr__(self):
        return f"<Course {self.name}>"

class Topics(db.Model):
    __tablename__ = 'topics'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    course = db.relationship('Courses', back_populates='topics')

    def __repr__(self):
        return f"<Topic {self.name}>"
