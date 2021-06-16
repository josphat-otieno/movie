from . import db
# from werkzeug.security import generate_password_hash,check_password_hash
# from flask_login import UserMixin
from datetime import datetime
from . import login_manager



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