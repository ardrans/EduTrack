from app import db

class Batches(db.Model):
    __tablename__ = 'batches'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    trainer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    students = db.relationship('BatchStudents', back_populates='batch')
    trainer = db.relationship('Users', backref='batches_trained')
    course = db.relationship('Courses', backref='batches')

    def __repr__(self):
        return f"<Batch {self.name}>"
