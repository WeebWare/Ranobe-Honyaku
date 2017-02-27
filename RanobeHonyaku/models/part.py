from RanobeHonyaku.database import db


class Part(db.Model):

    __tablename__ = "parts"

    id = db.Column(db.Integer(), primary_key=True)

    # Title of the part, if any
    title = db.Column(db.String(120))

    # The text body of the series
    body = db.Column(db.String(5000), nullable=False)

    # id that the part belongs to
    chapter_id = db.Column(db.Integer(), db.ForeignKey("chapters.id"))

    # The place the part comes in
    position = db.Column(db.Integer())

    def __repr__(self):
        return "<Part ({0.title}) ({0.id})>".format(self)
