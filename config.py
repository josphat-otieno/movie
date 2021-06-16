import os

class Config:
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://jose:joseotis45@localhost/movie'
    SECRET_KEY= os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
     
    MAIL_SERVER= 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class TestConfig(Config):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://jose:joseotis45@localhost/movie'
   

    DEBBUG=True

config_options={
    'development':DevConfig,
    'production':ProdConfig, 
    'test':TestConfig
}
