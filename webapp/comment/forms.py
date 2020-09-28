from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField


class CommentsForm(FlaskForm):
    commit = StringField('Комментарии', render_kw={"class": "btn btn-primary"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})
