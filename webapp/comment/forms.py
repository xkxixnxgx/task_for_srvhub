from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class CommentsForm(FlaskForm):
    picture = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    name = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})