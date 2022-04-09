from app import db

class Hospital(db.Model):
    __tablename__ = 'hospital'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    display = db.Column(db.String(128), unique=True)
