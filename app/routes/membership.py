from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from app.models import Membership
from app.forms.membership_forms import MembershipForm
from app import db

membership_bp = Blueprint('membership', __name__)

@membership_bp.route('/add_membership', methods=['GET', 'POST'])
@login_required
def add_membership():
    form = MembershipForm()
    if form.validate_on_submit():
        membership = Membership(user_id=current_user.id, duration_months=form.duration_months.data)
        db.session.add(membership)
        db.session.commit()
        flash('Membership added successfully!')
        return redirect(url_for('main.index'))
    return render_template('add_membership.html', form=form)
