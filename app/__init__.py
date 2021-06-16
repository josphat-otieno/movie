from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
from config import config_options

# creating instances
bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager =LoginManager()
photos = UploadSet('photos', IMAGES)
mail = Mail()

login_manager.session_protection='strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    # initialising flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # registering the blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    # configuring uploads
    configure_uploads(app,photos)
    
    # string configurations
    # from .requests import configure_request
    # configure_request_(app)

    return app