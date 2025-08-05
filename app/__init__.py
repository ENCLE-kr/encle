from flask import Flask

def create_app():
    app = Flask(__name__)

    # Blueprint
    from .views import main_views, company_views, service_views, references_views, news_views, recruitment_views, contact_view
    app.register_blueprint(main_views.bp)
    app.register_blueprint(company_views.bp)
    app.register_blueprint(service_views.bp)
    app.register_blueprint(references_views.bp)
    app.register_blueprint(news_views.bp)
    app.register_blueprint(recruitment_views.bp)
    app.register_blueprint(contact_view.bp)

    return app