from flask import Blueprint
from flask import render_template
# from webapp.pictures.forms import PicturesForm

blueprint = Blueprint('pictures', __name__, url_prefix='/pictures')


@blueprint.route('/')
def pictures():
    title = "Pictures"
    return render_template('pictures.html', page_title=title)