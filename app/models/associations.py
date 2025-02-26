from app.models import db


class BatchStudents(db.Model):
    __tablename__ = 'batch_students'

    id = db.Column(db.Integer, primary_key=True)
    batch_id = db.Column(db.Integer, db.ForeignKey('batches.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)  # Fixed foreign key

    batch = db.relationship('Batches', back_populates='students')
    student = db.relationship('Students', backref='batch_students')  # Updated relationship

    def __repr__(self):
        return f"<BatchStudent Batch={self.batch_id} Student={self.student_id}>"

