try:
    from ujson import dumps
except ImportError:
    from json import dumps  # noqa
from flask import Blueprint, request  # noqa
from flask_restful import Resource, Api as API

from RanobeHonyaku import app
from RanobeHonyaku.database import db  # noqa
from RanobeHonyaku.models.user import User  # noqa
from RanobeHonyaku.models.part import Part  # noqa
from RanobeHonyaku.models.author import Author  # noqa
from RanobeHonyaku.models.series import Series  # noqa
from RanobeHonyaku.models.volume import Volume  # noqa
from RanobeHonyaku.models.chapter import Chapter  # noqa
from RanobeHonyaku.models.illustrator import Illustrator  # noqa
from RanobeHonyaku.models.application import Application  # noqa

api_v1 = API(app)


class SeriesEndpoint(Resource):

    def get(self):
        return {}

    def post(self):
        return {}

    def delete(self):
        return {}

    def put(self):
        return {}

    def patch(self):
        return {}


class UserEndpoint(Resource):

    def get(self):
        return {}

    def post(self):
        return {}

    def delete(self):
        return {}

    def put(self):
        return {}

    def patch(self):
        return {}


"""
Old code we'll be phasing out
"""

# api_v1 = Blueprint("api", __name__, url_prefix="/api/v1")


# @api_v1.route("/authors", methods=["GET", "POST", "PUT", "DELETE"])
# def authors_route():
#     if request.method == "GET":
#         return dumps([{
#             "romanized": author.romanized_name,
#             "given_name": author.given_name,
#             "family_name": author.family_name
#         } for author in Author.query.all()])


# @api_v1.route("/series", methods=["GET", "POST", "PUT", "DELETE"])
# def series_route():
#     if request.method == "GET":
#         return dumps([{
#             "id": series.id,
#             "title": series.title,
#             "volumes": [
#                 {
#                     "id": volume.series_id,
#                     "title": volume.title,
#                     "series_id": volume.series_id,
#                     "chapters":  [{
#                         "id": chapter.id,
#                         "title": chapter.title,
#                         "volume_id": chapter.volume_id,
#                         "parts": [{
#                             "title": part.title,
#                             "body": part.body,
#                             "chapter_id": part.chapter_id,
#                             "position": part.position
#                         } for part in chapter.parts.order_by(Part.position).all()],
#                         "position": chapter.position
#                     } for chapter in volume.chapters.order_by(Chapter.position).all()],
#                     "position": volume.position
#                 } for volume in series.volumes.order_by(Volume.position).all()
#             ],
#             "teaser": series.is_teaser,
#             "status": series.translation_status,
#             "description": series.description,
#             "author": [{
#                 "romanized_name": author.romanized_name,
#                 "given_name": author.given_name,
#                 "family_name": author.family_name
#             } for author in Author.query.filter_by(id=series.author_id).all()],
#             "illustrator": [{
#                 "romanized_name": illustrator.romanized_name,
#                 "given_name": illustrator.given_name,
#                 "family_name": illustrator.family_name
#             } for illustrator in Illustrator.query.filter_by(id=series.illustrator_id).all()],
#             "original_title": series.original_title,
#             "one_shot": series.one_shot
#         } for series in Series.query.filter(Series.title.ilike("%{}%".format(request.args.get("q", "")))).all()])


# @api_v1.route("/applications", methods=["GET", "POST", "PUT", "DELETE"])
# def applications_rote():
#     if request.method == "GET":
#         return dumps([{
#             "id": app.id,
#             "name": app.name,
#             "url": app.url,
#             "source": app.source,
#             "owner": User.query.filter_by(id=app.owner_id).first().username,
#             "description": app.description
#         } for app in Application.query.all()])

#     elif request.method == "POST":
#         # Get all posted data
#         data = request.get_json()

#         # Return bad request if they send no data
#         if data is None:
#             return dumps({"error": "BAD REQUEST"}), 400

#         app = Application(name=data["name"],
#                           url=data["url"],
#                           source=data["source"],
#                           owner_id=data["owner_id"],
#                           description=data["description"])

#         db.session.add(app)
#         db.session.commit()

#         return dumps({
#             "id": app.id,
#             "name": app.name,
#             "url": app.url,
#             "source": app.source,
#             "owner": User.query.filter_by(id=app.owner_id).first().username,
#             "description": app.description
#         }), 201

#     elif request.method == "DELETE":
#         # Get all posted data
#         data = request.get_json()

#         # Return bad request if they send no data
#         if data is None:
#             return dumps({"error": "BAD REQUEST"}), 400

#         # Get the Application we want to remove from the database
#         to_remove = Application.query.filter_by(id=data["id"]).first()

#         # Remove it and commit the session
#         db.session.delete(to_remove)
#         db.session.commit()

#         removed = to_remove

#         # Return the removed object without an id as it no longer exists
#         return dumps({
#             "id": None,
#             "name": removed.name,
#             "url": removed.url,
#             "source": removed.source,
#             "owner": User.query.filter_by(id=removed.owner_id).first().username,
#             "description": removed.description
#         }), 200

#     elif request.method == "PATCH":
#         # Get all posted data
#         data = request.get_json()

#         # Return bad request if they send no data
#         if data is None:
#             return dumps({"error": "BAD REQUEST"}), 400

#         # Get application we want to update in the database
#         to_update = Application.query.filter_by(id=data["id"]).first()

#         # Ignore any errors that update raises

#         updated = to_update

#         return dumps({
#             "id": updated.id,
#             "name": updated.name,
#             "url": updated.url,
#             "source": updated.source,
#             "owner": User.query.filter_by(id=updated.owner_id).first().username,
#             "description": updated.description
#         })
