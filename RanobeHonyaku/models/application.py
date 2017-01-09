from RanobeHonyaku.database import db


class Application(db.Model):

    __tablename__ = "applications"

    id = db.Column(db.Integer(), primary_key=True)

    # The name of the application
    name = db.Column(db.String(50), nullable=False)

    # The applications website
    url = db.Column(db.String(100))

    # The source code of the application
    source = db.Column(db.String(100))

    # The description of the application
    description = db.Column(db.String(500))

    # The id of the owner of the  application
    owner_id = db.Column(db.Integer(), db.ForeignKey("users.id"))

    def __repr__(self):
        return "<Application ({0.name}) ({0.source}) ({0.id})>".format(self)
