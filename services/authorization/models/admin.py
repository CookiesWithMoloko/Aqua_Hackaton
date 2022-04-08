from app import db

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    token = db.Column(db.String(128), unique=True, nullable=True)
    permissions = db.Column(db.Text, unique=False, nullable=True)
