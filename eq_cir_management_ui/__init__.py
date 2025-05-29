"""Flask application factory for the EQ CIR Management UI."""

import json
import logging
import os
from pathlib import Path

from flask import Flask
from flask_talisman import Talisman
from jinja2 import ChainableUndefined, ChoiceLoader, FileSystemLoader

from eq_cir_management_ui.config.config import DefaultConfig
from eq_cir_management_ui.errors.routes import errors_blueprint
from eq_cir_management_ui.main.routes import main_blueprint
from eq_cir_management_ui.utils.routes import utils_blueprint

logger = logging.getLogger()

talisman = Talisman()


def create_app(app_config: type[DefaultConfig]) -> Flask:
    """Flask application factory, used to isolate the instance of the Flask application.
    See https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/ .
    """
    app = Flask(__name__)

    app.config.from_object(app_config)
    app.static_folder = str(Path("../static"))

    app.register_blueprint(main_blueprint)
    app.register_blueprint(errors_blueprint)
    app.register_blueprint(utils_blueprint)

    jinja_config(app)
    design_system_config(app)
    configure_secure_headers(app)

    return app


def jinja_config(app: Flask) -> None:
    """Configuration for the Flask Jinja2 component. Here we provide a customer loader,
    so we can load from an array of sources.

    :param app: The Flask application.
    """
    # loader for local templates and design system component templates
    file_system_loader = FileSystemLoader([Path("./node_modules/@ons/design-system"), Path("./templates")])

    app.jinja_loader = ChoiceLoader([file_system_loader])
    app.jinja_env.undefined = ChainableUndefined

    # Clean up white space.
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True


def design_system_config(app: Flask) -> None:
    """Set the version of the design system to an environment variable and add an
    environment variable filter so environment variables can be read from within
    Jinja. This enables the design system version to be defined once within the
    package.json file and then reused throughout the application. Primarily to
    declare the CSS version to use.

    :param app: The Flask application.
    """
    with open(Path("./package.json"), encoding="utf-8") as file:
        package_json = json.load(file)
        design_system_version = package_json["dependencies"]["@ons/design-system"]

        # Ensure version number only consists of numbers and fullstops.
        design_system_version = "".join(filter(lambda s: (s.isnumeric() or s == "."), design_system_version))

        os.environ["DESIGN_SYSTEM_VERSION"] = design_system_version

    # Add a custom filter to Jinja to retrieve environment variables.
    def env_override(value: str, key: str) -> str:
        return os.getenv(key, value)

    app.jinja_env.filters["env_override"] = env_override


def configure_secure_headers(app: Flask) -> None:
    """Use Flask-Talisman to configure secure headers for the application.

    :param app: The Flask application.
    """
    csp = {
        "default-src": ["'self'", app.config["CDN_URL"]],
        "font-src": ["'self'", app.config["CDN_URL"]],
        "script-src": [
            "'self'",
            app.config["CDN_URL"],
            "https://*.googletagmanager.com",
            "https://*.google-analytics.com",
        ],
        "style-src": ["'self'", app.config["CDN_URL"]],
        "connect-src": [
            "'self'",
            "https://*.googletagmanager.com",
            "https://*.google-analytics.com",
        ],
        "frame-src": [],
        "img-src": ["'self'", "data:"],
        "object-src": ["'none'"],
        "base-uri": ["'none'"],
        "manifest-src": ["'self'"],
    }
    talisman.init_app(
        app,
        force_https=False,  # HTTPS is managed by infrastructure
        content_security_policy=csp,
        frame_options="DENY",
        strict_transport_security=True,
        strict_transport_security_max_age=31536000,
        session_cookie_secure=app.config["SESSION_COOKIE_SECURE"],
    )
