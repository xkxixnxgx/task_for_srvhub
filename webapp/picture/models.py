from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comments = db.relationship('Comment', backref='picture')
    name = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    date_create = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Pictures {} {}>'.format(self.name, self.url)