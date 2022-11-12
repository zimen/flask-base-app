from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask_login import login_manager
from .forms import AddUser, Login 
from .models import Users 
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def homepage():
    return render_template("home.html")

@main.route('/add_user', methods= ['GET', 'POST'])
def add_user():
    form = AddUser()
    if form.validate_on_submit():
        if form.password_hash.data == form.password_hash2.data:
            check = Users.query.filter_by(email_address = form.email_address.data).first()
            if check : 
                flash('Email already exists', category='danger')
                return redirect(url_for('main.add_user'))
            else:
                Users(last_name = form.last_name.data, first_name = form.first_name.data, email_address = form.email_address.data, password_hash = generate_password_hash(form.password_hash.data, method='sha256')).save_to_db()
                flash('Nouvel utilisateur ajouté ', category='secondary')
                return redirect(url_for('main.login'))
        else:
            flash('Please enter same password')
    return render_template('add_user.html', form=form)

@main.route("/login", methods=["GET","POST"])
def login():
    form = Login()
    if form.validate_on_submit():
        user = Users.query.filter_by(email_address=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash("Logged in with success", category="success")
            return redirect(url_for('main.homepage'))
        else:
            flash("Mail address or password invalid", category="danger")
    return render_template('login.html', form=form)

@main.route('/logout')
def logout_page():
    logout_user()
    flash('Vous êtes correctement déconnecté',category="success")
    return redirect(url_for('main.login'))

def compute_item(x):
    return x*2 