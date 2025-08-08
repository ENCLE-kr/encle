from flask import Blueprint

bp = Blueprint('service', __name__, url_prefix='/service')

@bp.route('/')
def service():
    return 'Service'