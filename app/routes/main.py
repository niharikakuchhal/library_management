from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    print("Index route is being accessed.")
    return render_template('index.html')
