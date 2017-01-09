from RanobeHonyaku.database import db


class Volume(db.Model):

    __tablename__ = "volumes"

    id = db.Column(db.Integer(), primary_key=True)

    # The title of the volume
    title = db.Column(db.String(120))

    # The series id that the volume is associated with
    series_id = db.Column(db.Integer(), db.ForeignKey("series.id"))

    # The volumes associated with the series
    chapters = db.relationship("Chapter", backref="volumes", lazy="dynamic")

    # The place the volume comes in
    position = db.Column(db.Integer())

    def __repr__(self):
        return "<Volume ({0.title}) ({0.id})>".format(self)
