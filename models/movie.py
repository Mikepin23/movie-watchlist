from datetime import datetime
from extensions import db
import uuid

class Movie(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(100), nullable=False)
    watched = db.Column(db.Boolean, default=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    date_watched = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Movie('{self.title}', Watched: {self.watched}')"
