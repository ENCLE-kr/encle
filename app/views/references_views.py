from flask import Blueprint, render_template

from app.models import Reference

bp = Blueprint('references', __name__, url_prefix='/references')

@bp.route('/')
def references():
    references_list = Reference.query.order_by(Reference.create_date.desc()).all()
    return render_template('references/references.html', references_list=references_list)

@bp.route('/<year>')
def references_by_year(year):
    references_list = Reference.query.filter(
        Reference.date.like(f'{year}%')
    ).order_by(Reference.create_date.desc()).all()
    return render_template('references/references.html', references_list=references_list, selected_year=year)