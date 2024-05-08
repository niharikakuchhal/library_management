from app import db
from datetime import datetime

class Membership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    duration_months = db.Column(db.Integer, default=6)  # Default duration 6 months

    user = db.relationship('User', backref='memberships')
