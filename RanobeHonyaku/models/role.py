from RanobeHonyaku.database import db


class Role(db.Model):

    __tablename__ = "roles"

    id = db.Column(db.Integer(), primary_key=True)

    # The name of the role
    name = db.Column(db.String(80), nullable=False, unique=True)

    def __str__(self):
        return "<Role ({0.name}) ({0.id})>".format(self)
