#from sqlalchemy.orm import backref
from Scrape import db,login_manager
from Scrape import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    pwdHash = db.Column(db.String(length=60), nullable=False)
    items = db.relationship('Item', backref="owned_user", lazy=True)

    def __repr__(self):
        return f"User {self.username}"

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_passsword):
        self.pwdHash = bcrypt.generate_password_hash(
            plain_text_passsword).decode('utf-8')
    
    def checkPassword(self,enteredPwd):
        return bcrypt.check_password_hash(self.pwdHash,enteredPwd)



class Item (db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    link = db.Column(nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(length=1024),
                            nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'
