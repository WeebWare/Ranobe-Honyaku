from RanobeHonyaku.database import db

user_projects = db.Table(
    "user_projects",
    db.Column("user_id", db.Integer(), db.ForeignKey("users.id")),
    db.Column("series_id", db.Integer(), db.ForeignKey("series.id"))
)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)

    # Identification
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(db.String(255), nullable=False, unique=True)

    # Hash of the password because plaintext is bad mmkay...
    password = db.Column(db.String(255), nullable=False)

    # Avatar
    avatar = db.Column(db.LargeBinary())

    # Applications they user has developed
    applications = db.relationship("Application", backref="users", lazy="dynamic")

    # Projects that the user is on
    projects = db.relationship("Series", secondary=user_projects,  backref=db.backref("series", lazy="dynamic"))

    # The users roles
    # roles = db.relationship("Role", backref="users", lazy="dynamic")

    def __repr__(self):
        return "<User ({0.username}) ({0.email}) ({0.id})>".format(self)
