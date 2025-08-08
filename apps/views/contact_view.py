from flask import Blueprint

bp = Blueprint('contact', __name__, url_prefix='/contact')

@bp.route('/')
def contact():
    return 'Contact'