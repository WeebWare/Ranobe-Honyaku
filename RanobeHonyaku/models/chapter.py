from RanobeHonyaku.database import db


class Chapter(db.Model):

    __tablename__ = "chapters"

    id = db.Column(db.Integer(), primary_key=True)

    # The title of the chapter
    title = db.Column(db.String(120))

    # The series id that the chapter is associated with
    volume_id = db.Column(db.Integer(), db.ForeignKey("volumes.id"))

    # The chapters associated with the series
    parts = db.relationship("Part", backref="chapters", lazy="dynamic")

    # The place the chapter comes in
    position = db.Column(db.Integer())

    def __repr__(self):
        return "<Chapter ({0.title}) ({0.id})>".format(self)
