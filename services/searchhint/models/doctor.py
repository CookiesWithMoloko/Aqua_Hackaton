from app import db

class Doctor(db.Model):
    __tablename__ = 'doctor'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    display = db.Column(db.String(150))
    hospital = db.relationship("Hospital", backref="doctor", uselist=False)
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.id'), nullable=False)