from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from app.models import User
from app.forms.auth_forms import LoginForm, RegistrationForm,AdminSignupForm,UserSignupForm,VendorLoginForm
from app import db
from services import save_user


auth = Blueprint('auth', __name__)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return '<Admin {}>'.format(self.name)

@auth.route('/signup/user', methods=['GET', 'POST'])
def user_signup():
    form = UserSignupForm()  # Instantiate the form
    if form.validate_on_submit():
        # Process the form data, e.g., create a user instance
        user = User(name=form.name.data, email=form.email.data, password=form.password.data)
        # Save the user, assuming you have a function or method to handle that
        save_user(user)
        flash('Thanks for registering!')
        return redirect(url_for('login'))  # Redirect to the login page, or wherever appropriate
    return render_template('user/user_signup.html', form=form) 

# Admin dashboard access
@auth.route('/admin/dashboard')
@login_required
def admin_dashboard():
    return render_template('admin/dashboard.html')

# Admin login
@auth.route('/login/admin', methods=['GET', 'POST'])
def admin_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data, role='admin').first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('auth.admin_dashboard'))
        flash('Invalid username or password')
    return render_template('admin/login.html', form=form)

# Vendor login
@auth.route('/login/vendor', methods=['GET', 'POST'])
def vendor_login():
    if current_user.is_authenticated:
        return redirect(url_for('vendor_dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data, role='vendor').first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('vendor_dashboard'))
        flash('Invalid username or password')
    return render_template('vendor/login_vendor.html', form=form)





# User login
@auth.route('/login/user', methods=['GET', 'POST'])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data, role='user').first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('auth.user_dashboard'))
        flash('Invalid username or password')
    return render_template('user/login_user.html', form=form)

# Logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))  # Assuming 'main.index' is the home page

# Register
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash('Username already exists')
            return redirect(url_for('auth.register'))
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.route('/signup/admin', methods=['GET', 'POST'])
def admin_signup():
    form = AdminSignupForm()
    if form.validate_on_submit():
        # Process the valid form (e.g., save the user)
        hashed_password = generate_password_hash(form.password.data)
        admin = Admin(
            name=form.name.data,
            email=form.email.data,
            password_hash=hashed_password,
            category=form.category.data
        )
        db.session.add(admin)
        db.session.commit()
        flash('Admin account created successfully!')
        return redirect(url_for('auth.admin_login'))
    return render_template('admin/signup_admin.html', form=form)

@auth.route('/path-for-login-handler', methods=['POST'])
def login_handler():
    username = request.form['username']
    password = request.form['password']
    user = User.authenticate(username, password)
    return redirect(url_for('vendor_dashboard'))  # This method depends on your User model
    if user:
        login_user(user)  # Flask-Login function to log in the user
        return redirect(url_for('vendor_dashboard'))
    else:
        flash('Invalid username or password')
        return redirect(url_for('login_vendor'))  # Adjust as necessary

@auth.route('/login-dashboard')
@login_required  # Assuming you are using Flask-Login or similar for handling user sessions
def login_dashboard():
    return render_template('login_dashboard.html')
