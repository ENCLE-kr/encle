from apps import db

class Reference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    purpose = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    organization = db.Column(db.String(100), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    picture = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(100), nullable=False)