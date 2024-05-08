from flask import render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from app.models import User
from extensions import db
from app.forms.auth_forms import LoginForm, RegistrationForm

# @auth.route('/login/admin', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user and user.check_password_hash(form.password.data):
#             login_user(user)
#             return redirect(url_for('main.dashboard'))
#         flash('Invalid username or password')
#     return render_template('admin/login.html', form=form)


@auth.route('/vendor/dashboard')
@login_required
def vendor_dashboard():
    return render_template('vendor_dashboard.html')

# Define other routes as necessary
@auth.route('/vendor/your-items')
@login_required
def your_items():
    # Logic to display items
    pass

@auth.route('/vendor/add-new-item')
@login_required
def add_new_item():
    # Logic to add a new item
    pass

@auth.route('/vendor/transactions')
@login_required
def transactions():
    # Logic to handle transactions
    pass

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# @auth.route('/login/vendor', methods=['GET', 'POST'])
# def login_vendor():
#     form = VendorLoginForm()
#     # Implement login logic specific to vendor
#     return render_template('auth/login_vendor.html', form=form)

# @auth.route('/login/user', methods=['GET', 'POST'])
# def login_user():
#     form = UserLoginForm()
#     # Implement login logic specific to user
#     return render_template('auth/login_user.html', form=form)