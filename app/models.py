from app import db

class Reference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    purpose = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    organization = db.Column(db.String(100), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)