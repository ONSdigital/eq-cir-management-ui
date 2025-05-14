"""Routes for the EQ CIR Management UI utils."""

from typing import NoReturn

from flask import Blueprint, abort

utils_blueprint = Blueprint("utils", __name__)


@utils_blueprint.route("/401")
def trigger_401() -> NoReturn:
    """Simulate an unauthorized error."""
    abort(401)


@utils_blueprint.route("/403")
def trigger_403() -> NoReturn:
    """Simulate a forbidden error."""
    abort(403)


@utils_blueprint.route("/500")
def trigger_500() -> NoReturn:
    """Simulate an internal server error."""
    abort(500)
