from flask import Flask, g, session

from .config import BaseConfig
from .core import core
from .extensions import ldap
from .foo import foo

DEFAULT_BLUEPRINTS = (core, foo)


def create_app(config=None, app_name=None, blueprints=None):
    if app_name is None:
        app_name = BaseConfig.PROJECT
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS
    app = Flask(app_name)
    configure_app(app, config)
    register_hooks(app)
    register_blueprints(app, blueprints)
    register_extensions(app)
    return app


def configure_app(app, config=None):
    if config:
        app.config.from_object(config)


def register_hooks(app):
    @app.before_request
    def before_request():
        g.user = None
        if "user_id" in session:
            # This is where you'd query your database to get the user info.
            g.user = {}
            # Create a global with the LDAP groups the user is a member of.
            g.ldap_groups = ldap.get_user_groups(user=session["user_id"])


def register_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def register_extensions(app):
    ldap.init_app(app)
