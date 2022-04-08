from app import db

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    display = db.Column(db.String(150))
    hospital = db.relationship("Hospital", backref="hospital", uselist=False)