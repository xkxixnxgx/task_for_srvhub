from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    picture_id = db.Column(db.Integer(), db.ForeignKey('picture.id'))
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    date_create = db.Column(db.DateTime, default=datetime.utcnow)
    date_update = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    comment = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Comments {} {}>'.format(self.user, self.comment)