from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Vendor(db.Model):
    __tablename__ = 'vendor'  # Specify the table name explicitly
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))