# from flask import Flask
# from flask_migrate import Migrate
# from extensions import db, login_manager
# from app.models import User
# from .auth import auth as auth_blueprint
# from app.routes import main

# def create_app(config_class='config.Config'):
#     app = Flask(__name__)
#     app.config.from_object(config_class)

#     db.init_app(app)
#     login_manager.init_app(app)
#     login_manager.login_view = 'auth.login'
#     migrate = Migrate(app, db)

#     from .models import User, Membership, Vendor, Transaction  # Ensuring models are loaded
#     from .routes.main import main as main_blueprint
#     from .routes.auth import auth as auth_blueprint

#     app.register_blueprint(main_blueprint)
#     app.register_blueprint(auth_blueprint, url_prefix='/auth')  # Register once with URL prefix

#     @login_manager.user_loader
#     def load_user(user_id):
#         return User.query.get(int(user_id))

#     return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from extensions import db, login_manager
from flask_login import LoginManager

login_manager = LoginManager()

def create_app(config_class='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .models import User, Membership, Vendor, Transaction
    from .routes.main import main as main_blueprint
    from .routes.auth import auth as auth_blueprint
    
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    @login_manager.user_loader
    def load_user(user_id):
        # return User.query.get(int(user_id))
        user_type, user_id = user_id.split('-')  # Assuming IDs are stored as 'vendor-1', 'user-2'
        if user_type == 'vendor':
            return Vendor.query.get(int(user_id))
        else:
            return User.query.get(int(user_id))

    return app