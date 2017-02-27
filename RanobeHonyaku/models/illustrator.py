from RanobeHonyaku.database import db


class Illustrator(db.Model):

    __tablename__ = "illustrators"

    id = db.Column(db.Integer(), primary_key=True)

    # Romanized version of given_name
    romanized_name = db.Column(db.String(200), nullable=False)

    # The authors given name (Japanese)
    given_name = db.Column(db.String(200), nullable=False)

    # The authors family name (Japanese)
    family_name = db.Column(db.String(200), nullable=False)

    # Series the illustrator worked on
    series = db.relationship("Series", backref="illustrators", lazy="dynamic")

    def __repr__(self):
        return "<Illustrator ({0.romanized_name}) ({0.id})>".format(self)
