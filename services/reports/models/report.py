from app import db
from sqlalchemy.sql import func
class Report(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    created = db.Column(db.DateTime, server_default=func.now())
    # c
    author = db.Column(db.String(150), unique=False)
    passport = db.Column(db.String(12), unique=False, nullable=False)
    email = db.Column(db.String(256), unique=False, nullable=False)
    # o
    organization = db.Column(db.String(256), unique=False, nullable=False)
    target = db.Column(db.String(256), unique=False, nullable=True)
    target_organization = db.Column(db.Boolean, default=True)
    # m
    tags = db.Column(db.Text, unique=False)
    group = db.Column(db.String(16), unique=False, nullable=False)

    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, default=1)
