from flask import (
    g,
    flash,
    request,
    session,
    url_for,
    redirect,
    render_template,
)

from RanobeHonyaku import app
from RanobeHonyaku.database import db
from RanobeHonyaku.models import User
from RanobeHonyaku.utils import CONFIG
from RanobeHonyaku.errors import InvalidCredentials
from RanobeHonyaku.utils.decorators import anon_only, login_required
from RanobeHonyaku.utils.security import encrypt_password, validate_password


@app.before_request
def before_request():
    g.CONFIG = CONFIG
    try:
        g.user = User.query.get(session["user_id"])
    except KeyError:
        g.user = None


@app.route("/")
def index():
    return


@app.route("/applications")
def applications():
    return


@app.route("/api")
def redirect_to_github():
    return redirect(CONFIG["SOCIAL"]["GITHUB"], 301)


@app.route("/main-projects")
def main():
    return


@app.route("/teaser-projects")
def teasers():
    return


@app.route("/login", methods=["GET", "POST"])
@anon_only
def login():
    if request.method == "GET":
        return
    else:
        r = request.form
        # Get our users object
        user = User.query.filter(User.email == r["email"] or User.username == r["username"]).first()
        if user is None:
            flash("Account does not exist. Check your login information.")
            return redirect("login")
        try:
            # Try match their password to their user
            validate_password(r["password"], user.password)
        except InvalidCredentials:
            # If it fails we redirect them to login to have them try again
            flash("Your username/email or password are incorrect.")
            return redirect("login")
        # If it doesn't fail we set the user this session
        session["user_id"] = user.id
        # Send them to the home page since everything went fine
        return redirect(url_for("index"), 200)


@app.route("/logout")
@login_required
def logout():
    if g.user:
        del session["user_id"]
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
@anon_only
def register():
    if request.method == "GET":
        return
    else:
        r = request.form
        # Checks if the username or email is taken
        if User.query.filter(User.email == r["username"] or User.username == r["username"]).first() is not None:
            flash("Desired username/email is already registered!")
            return redirect("register")
        # Create the User object
        user = User(email=r["email"], username=r["username"], password=encrypt_password(r["password"]))
        # If we haven't redirected them back to register, we add it to the database and commit
        db.session.add(user)
        db.session.commit()
        # Send them to the home page since everything went fine
        return redirect(url_for("index"), 200)
