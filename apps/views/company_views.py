from flask import Blueprint

bp = Blueprint('company', __name__, url_prefix='/company')

@bp.route('/')
def company():
    return 'Company'