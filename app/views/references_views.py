from flask import Blueprint

bp = Blueprint('references', __name__, url_prefix='/references')

@bp.route('/')
def references():
    return 'References'