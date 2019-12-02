from flask import render_template, url_for, flash, redirect, request, Blueprint
from app import app
from app.forms.users import LoginForm
from flask_login import current_user, login_user
from app.models.users import User

users = Blueprint('users',__name__)

@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.password == form.password.data:
            flash('Invalid username or password')
            return redirect(url_for('users.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.home'))
    return render_template('login.html', title='Sign In', form=form)



