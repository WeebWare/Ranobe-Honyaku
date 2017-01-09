from RanobeHonyaku.database import db


class Series(db.Model):

    __tablename__ = "series"

    id = db.Column(db.Integer(), primary_key=True)

    # The title of the series
    title = db.Column(db.String(120), unique=True, nullable=False)

    # The chapters associated with the series
    volumes = db.relationship("Volume", backref="series", lazy="dynamic")

    # If not true the series gets displayed under main projects
    is_teaser = db.Column(db.Boolean(), nullable=False)

    # Can be any of ["N/A", "Completed", "Dropped", "Active", "Inactive", "On hold"]
    translation_status = db.Column(db.String(), nullable=False)

    # Description of the series
    description = db.Column(db.String(2500))

    # Japanese title
    original_title = db.Column(db.String(120), nullable=False)

    # One shot or not
    one_shot = db.Column(db.Boolean(), nullable=False)

    # The id of the author that wrote the series
    author_id = db.Column(db.Integer(), db.ForeignKey("authors.id"))

    # The id of the illustrator that worked on the series
    illustrator_id = db.Column(db.Integer(), db.ForeignKey("illustrators.id"))

    def __repr__(self):
        return "<Series ({0.title}) ({0.id})>".format(self)
