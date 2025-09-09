from flask import Blueprint, render_template, request, redirect, url_for, flash
from apps.models import News
from apps import db
import os
from werkzeug.utils import secure_filename

bp = Blueprint('news', __name__, url_prefix='/news')

# 파일 업로드 설정
UPLOAD_FOLDER = 'apps/static/assets/img/news'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/')
def news():
    page = request.args.get('page', 1, type=int)
    per_page = 9  # 3x3 그리드
    
    # 페이징 처리
    pagination = News.query.order_by(News.date.desc()).paginate(
        page=page, 
        per_page=per_page, 
        error_out=False
    )
    
    news_list = pagination.items
    
    return render_template('news/news.html', 
                         news_list=news_list,
                         pagination=pagination)

@bp.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        # 폼 데이터 가져오기
        date = request.form.get('date')
        title = request.form.get('title')
        content = request.form.get('content')
        link = request.form.get('link')
        
        # 파일 업로드 처리
        picture = request.files.get('picture')
        picture_filename = None
        
        if picture and allowed_file(picture.filename):
            filename = secure_filename(picture.filename)
            # 파일명에 타임스탬프 추가하여 중복 방지
            import datetime
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{timestamp}_{filename}"
            
            # 업로드 폴더가 없으면 생성
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)
            
            # 파일 저장
            picture_path = os.path.join(UPLOAD_FOLDER, filename)
            picture.save(picture_path)
            picture_filename = filename
        
        # 데이터베이스에 저장
        try:
            news_item = News(
                picture=picture_filename or 'default.jpg',
                date=date,
                title=title,
                content=content,
                link=link
            )
            db.session.add(news_item)
            db.session.commit()
            flash('뉴스가 성공적으로 추가되었습니다.', 'success')
            return redirect(url_for('news.news'))
        except Exception as e:
            db.session.rollback()
            flash('뉴스 추가 중 오류가 발생했습니다.', 'error')
            print(f"Error: {e}")
    
    return render_template('news/update.html')