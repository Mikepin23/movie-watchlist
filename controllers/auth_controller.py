from flask import jsonify, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from models.user import User
from extensions import db, bcrypt
from forms.auth_forms import RegistrationForm, LoginForm
from flask_login import login_user

def handle_register(request):
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if User.query.filter_by(username=username).first():
            error = "Username already exists."
            return render_template('register.html', form=form, error=error)
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash('Registration successful! You are now logged in.', 'success')
        return redirect(url_for('movie.watchlist'))
    return render_template('register.html', form=form)

def handle_login():
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('movie.watchlist'))
        else:
            error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)

def handle_logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.home'))
