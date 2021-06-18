from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from app.models import *



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class Movie:
    '''
    Movie class to define Movie Objects
    '''
    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count


# class Review(db.Model):
#     __tablename__ = 'reviews'

#     id = db.Column(db.Integer,primary_key = True)
#     movie_id = db.Column(db.Integer)
#     movie_title = db.Column(db.String)
#     image_path = db.Column(db.String)
#     movie_review = db.Column(db.String)
#     posted = db.Column(db.DateTime,default=datetime.utcnow)
#     user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

#     def __init__(self,movie_id,title,imageurl,review):
#         self.movie_id = movie_id
#         self.title = title
#         self.imageurl = imageurl
#         self.review = review
#     all_reviews = []
#     def save_review(self):
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def clear_reviews(cls):
#         Review.all_reviews.clear()
#     @classmethod
#     def get_reviews(cls,id):
#         reviews = Review.query.filter_by(movie_id=id).all()
#         return reviews
# class User(UserMixin,db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer,primary_key = True)
#     username = db.Column(db.String(255),index = True)
#     email = db.Column(db.String(255),unique = True,index = True)
#     role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
#     bio = db.Column(db.String(255))
#     profile_pic_path = db.Column(db.String())
#     password_hash = db.Column(db.String(255))
#     reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")
#     @property
#     def password(self):
#         raise AttributeError('You cannnot read the password attribute')
#     @password.setter
#     def password(self, password):
#         self.password_hash = generate_password_hash(password)
#     def verify_password(self,password):
#         return check_password_hash(self.password_hash,password)
#     def __repr__(self):
#         return f'User {self.username}'
# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer,primary_key = True)
#     name = db.Column(db.String(255))
#     users = db.relationship('User',backref = 'role',lazy="dynamic")
#     def __repr__(self):
#         return f'User {self.name}'
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from time import time
# import jwt
# from app import app






                
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True, index =True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash=db.Column(db.String(255))
    bio = db.Column(db.String(255))
    age = db.Column(db.Integer)
    profile_pic_path = db.Column(db.String())
    subscription = db.relationship('Subscription', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):

        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'User {self.username}'

    # def get_reset_password_token(self, expires_in=600):
        # return jwt.encode(
            # {'reset_password': self.id, 'exp': time() + expires_in},
            # app.config['SECRET_KEY'], algorithm='HS256')

    # @staticmethod
    # def verify_reset_password_token(token):
        # try:
            # id = jwt.decode(token, app.config['SECRET_KEY'],
                            # algorithms=['HS256'])['reset_password']
        # except:
            # return
        # return User.query.get(id)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref = 'role', lazy = "dynamic")


    def __repr__(self):
        return f'User{self.name}' 

class Subscription(db.Model):
    __tablename__ = "subscription"
    id =db.Column(db.Integer, primary_key=True)
    email =db.Column(db.String(255))
    phone_number = db.Column(db.Integer)
    country = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


class Genres:
    def __init__(self,id,name):
        self.id = id
        self.name = name




