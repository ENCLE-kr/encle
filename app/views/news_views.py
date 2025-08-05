from flask import Blueprint

bp = Blueprint('news', __name__, url_prefix='/news')

@bp.route('/')
def news():
    return 'News'