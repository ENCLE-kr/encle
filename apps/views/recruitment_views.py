from flask import Blueprint

bp = Blueprint('recruitment', __name__, url_prefix='/recruitment')

@bp.route('/')
def recruitment():
    return 'Recruitment'