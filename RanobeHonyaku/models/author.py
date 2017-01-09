from RanobeHonyaku.database import db


class Author(db.Model):

    __tablename__ = "authors"

    id = db.Column(db.Integer(), primary_key=True)

    # Romanized version of given_name
    romanized_name = db.Column(db.String(200), nullable=False)

    # The authors given name (Japanese)
    given_name = db.Column(db.String(200), nullable=False)

    # The authors family name (Japanese)
    family_name = db.Column(db.String(200), nullable=False)

    # Series the author wrote
    series = db.relationship("Series", backref="authors", lazy="dynamic")

    def __repr__(self):
        return "<Author ({0.romanized_name}) ({0.id})>".format(self)
