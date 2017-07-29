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
