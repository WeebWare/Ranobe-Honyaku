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
from RanobeHonyaku.models import Application, Series
from RanobeHonyaku.utils.decorators import anon_only, login_required


@app.before_request
def before_request():
    # We load this into our global so we don't have to pass CONFIG to every template.
    g.CONFIG = CONFIG
    try:
        # Because without actual users we might as well do nothing.
        g.user = User.query.filter_by(id=session["user_id"]).first()
    except KeyError:
        g.user = None


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/applications")
def applications():
    return render_template("applications.html", applications=Application.query.order_by(Application.name).all())


@app.route("/api")
def redirect_to_github():
    return redirect(CONFIG["SOCIAL"]["GITHUB"], 301)


@app.route("/main-projects")
def main():
    return render_template("projects.html", series=[])


@app.route("/teaser-projects")
def teasers():
    return render_template("projects.html", series=Series.query.filter_by())


@app.route("/login", methods=["GET", "POST"])
@anon_only
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        r = request.form
        # Get our users object
        user = User.query.filter(User.email == r["email"] or User.username == r["username"]).first()
        if user is None:
            flash("Account does not exist. Check your login information.")
            return redirect("login")
        try:
            # Try match their password to their user
            user.verify_pass(r["password"])
        except InvalidCredentials:
            # If it fails we redirect them to login to have them try again
            flash("Incorrect password.")
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
        return render_template("register.html")
    else:
        r = request.form
        # Checks if the username or email is taken
        if User.query.filter(User.email == r["username"] or User.username == r["username"]).first() is not None:
            flash("Desired username/email is already registered!")
            return redirect("register")
        # Create the User object
        user = User(email=r["email"], username=r["username"])
        # Encrypt their password
        user.encrypt_pass(password=r["password"])
        # If we haven't redirected them back to register, we add it to the database and commit
        db.session.add(user)
        db.session.commit()
        # Send them to the home page since everything went fine
        return redirect(url_for("index"), 200)
