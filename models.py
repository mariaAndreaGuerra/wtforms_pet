from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DFLT_IMG = ''


def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    species = db.Column(db.String(255), nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Pet {self.name}>'
