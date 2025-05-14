"""Routes for the EQ CIR Management UI."""

import logging

from flask import (
    Blueprint,
    render_template,
    request,
)

main_blueprint = Blueprint("main", __name__)

logger = logging.getLogger(__name__)


@main_blueprint.before_request
def before_request_func() -> None:
    """Log the request before it is processed."""
    if request.endpoint != "health-check":
        msg = "Request received"
        logger.info(msg)


@main_blueprint.route("/", methods=["GET"])
def home() -> str:
    """UI homepage.

    :return: 200 home page.
    """
    return render_template("home.html")


@main_blueprint.route("/health-check")
def health() -> tuple[str, int]:
    """Health check endpoint.

    :return: Empty 200 response.
    """
    return "", 200
