from flask_login import UserMixin
from extensions import db
import uuid

class User(db.Model, UserMixin):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    movies = db.relationship('Movie', backref='owner', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', ID: {self.id}')"
