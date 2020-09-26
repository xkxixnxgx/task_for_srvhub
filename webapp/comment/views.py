from flask import Blueprint
from flask import render_template
from webapp.comments.forms import CommentsForm

blueprint = Blueprint('comments', __name__, url_prefix='/comments')


@blueprint.route('/')
def pictures():
    title = "Авторизация"
    login_form = CommentsForm()
    return render_template('login.html', page_title=title, form=login_form)