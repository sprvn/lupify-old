from flask import render_template, redirect, request, url_for
from flask_login import login_required, login_user

from lupify.forms import LoginForm
from lupify.models import User

from lupify import app, login_manager

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/host')
@login_required
def host():
    return render_template('host.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            login_user(user, form.remember.data)
            return redirect(request.args.get('next') or url_for('index'))
    return render_template("login.html", form=form)

#######
#######
# Error handlers
# TODO: Fix templates for 404 and server errors
#######
#######
#@app.errorhandler(404)
#def page_not_found(e):
#    return render_template('404.html'), 404
#
#@app.errorhandler(500)
#def server_error(e):
#    return render_template('500.html'), 500