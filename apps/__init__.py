from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # Blueprint
    from .views import main_views, company_views, solution_views, references_views, news_views, recruitment_views, contact_view
    app.register_blueprint(main_views.bp)
    app.register_blueprint(company_views.bp)
    app.register_blueprint(solution_views.bp)
    app.register_blueprint(references_views.bp)
    app.register_blueprint(news_views.bp)
    app.register_blueprint(recruitment_views.bp)
    app.register_blueprint(contact_view.bp)

    return app