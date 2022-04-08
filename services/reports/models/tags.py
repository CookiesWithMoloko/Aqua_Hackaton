from app import db

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)

    display = db.Column(db.String(128), unique=True, nullable=False)
    short = db.Column(db.String(32))
    keywords = db.Column(db.Text)
