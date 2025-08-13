from flask import Blueprint, render_template

bp = Blueprint('company', __name__, url_prefix='/company')

@bp.route('/')
def company():
    return render_template('company/company.html')