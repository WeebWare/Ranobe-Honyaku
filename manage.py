#! /usr/bin/env python3

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from RanobeHonyaku import app
from RanobeHonyaku.database import db
from RanobeHonyaku.models.user import User

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("db", MigrateCommand)


@manager.command
def runserver():
    app.run(host="127.0.0.1", port=5000, debug=True)


@manager.command
def setup():
    with app.app_context():
        db.create_all()


@manager.command
def create_admin_user():
    with app.app_context():
        db.session.add(
            User(
                email="",
                username="",
                password="",
                avatar=None,
            )
        )
        db.session.commit()


if __name__ == "__main__":
    manager.run()
