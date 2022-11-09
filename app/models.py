from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True, nullable=False, unique=True)
    last_name = db.Column(db.String(length=30), nullable=False)
    first_name = db.Column(db.String(length=30), nullable=False)
    email_address = db.Column(db.String(length=50),nullable=False, unique=True)
    password_hash = db.Column(db.String(length=200), nullable=False)
    is_admin = db.Column(db.Boolean(), nullable=False, default=False)
    
    def json(self):
        return {
            'id': self.id, 
            'last_name': self.last_name, 
            'first_name': self.first_name,
            'email_address': self.email_address,
            'is_admin': self.is_admin
            }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

def init_db():
    db.create_all()
    Users(last_name="HADDOU", first_name= "ayoub1", email_address= "ayoub1@gmail.com", 
            password_hash= generate_password_hash("1234", method='sha256'), is_admin=True).save_to_db()
    