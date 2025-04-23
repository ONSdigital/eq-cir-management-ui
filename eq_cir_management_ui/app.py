"""Module providing a basic flask instance."""

from flask import Flask


def create_app() -> Flask:
    """Create and configure the Flask application.

    This function initializes a Flask application instance, sets up the
    necessary routes, and returns the configured app object.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)

    @app.route("/")
    def index() -> str:
        return "Hello, World!"

    return app
