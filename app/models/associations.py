from app import db

class BatchStudents(db.Model):
    __tablename__ = 'batch_students'

    id = db.Column(db.Integer, primary_key=True)
    batch_id = db.Column(db.Integer, db.ForeignKey('batches.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    batch = db.relationship('Batches', back_populates='students')
    student = db.relationship('Users', backref='batch_students')

    def __repr__(self):
        return f"<BatchStudent Batch={self.batch_id} Student={self.student_id}>"
