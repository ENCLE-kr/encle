from flask import Blueprint, render_template

bp = Blueprint('solution', __name__, url_prefix='/solution')

@bp.route('/')
def solution():
    return render_template('solution/solution.html')