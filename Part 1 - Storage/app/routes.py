from flask import flash, redirect, render_template, request, url_for, Blueprint
from flask_login import login_required, login_user, logout_user

from .AuthManager import AuthManager
from .database import db
from .models import Users

site = Blueprint('simple_page', __name__, template_folder='templates')

auth_manager = AuthManager(db)


@site.route("/")
def index():
    return render_template("index.html")


@site.route("/home")
@login_required
def home():
    return render_template("home.html")


@site.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if auth_manager.register(email, password):
            flash("Account created for {}".format(email), "success")
            return redirect(url_for("simple_page.home"))
        else:
            flash("An error occured", "danger")
    return render_template("signup.html")


@site.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = Users.query.filter_by(email=email).first()
        if user and auth_manager.login(email, password):
            login_user(user)
            return redirect(url_for("simple_page.home"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("login.html")


@site.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("simple_page.home"))
