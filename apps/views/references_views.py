from flask import Blueprint, render_template, request, jsonify

from apps.models import Reference

bp = Blueprint('references', __name__, url_prefix='/references')

@bp.route('/')
def references():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    # 전체 레퍼런스 쿼리 - 일자 기준 내림차순
    query = Reference.query.order_by(Reference.date.desc())
    
    # 페이징 처리
    pagination = query.paginate(
        page=page, 
        per_page=per_page, 
        error_out=False
    )
    
    references_list = pagination.items
    
    return render_template('references/references.html', 
                         references_list=references_list,
                         pagination=pagination)

@bp.route('/<year>')
def references_by_year(year):
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    # 연도별 레퍼런스 쿼리 - 일자 기준 내림차순
    query = Reference.query.filter(
        Reference.date.like(f'{year}%')
    ).order_by(Reference.date.desc())
    
    # 페이징 처리
    pagination = query.paginate(
        page=page, 
        per_page=per_page, 
        error_out=False
    )
    
    references_list = pagination.items
    
    return render_template('references/references.html', 
                         references_list=references_list, 
                         selected_year=year,
                         pagination=pagination)

@bp.route('/api/filter')
def filter_references():
    year = request.args.get('year')
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    if year and year != 'all':
        query = Reference.query.filter(
            Reference.date.like(f'{year}%')
        ).order_by(Reference.date.desc())
    else:
        query = Reference.query.order_by(Reference.date.desc())
    
    pagination = query.paginate(
        page=page, 
        per_page=per_page, 
        error_out=False
    )
    
    references_list = pagination.items
    
    # HTML 테이블 부분만 렌더링
    table_html = render_template('references/_references_table.html', 
                               references_list=references_list,
                               pagination=pagination,
                               selected_year=year)
    
    return jsonify({
        'table_html': table_html,
        'pagination': {
            'page': pagination.page,
            'pages': pagination.pages,
            'has_prev': pagination.has_prev,
            'has_next': pagination.has_next,
            'prev_num': pagination.prev_num,
            'next_num': pagination.next_num,
            'total': pagination.total,
            'first': pagination.first,
            'last': pagination.last
        }
    })