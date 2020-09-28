from flask import Blueprint
from flask import render_template
from webapp.comment.forms import CommentsForm

blueprint = Blueprint('comment', __name__, url_prefix='/comment')


@blueprint.route('/')
def comment():
    title = 'Comment'
    comment_form = CommentsForm()
    return render_template('picture/picture.html', page_title=title, comment_form=comment_form)