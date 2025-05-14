"""Errors routes."""

from flask import Blueprint, render_template, request
from structlog import get_logger
from werkzeug.exceptions import (
    Forbidden,
    InternalServerError,
    NotFound,
    Unauthorized,
)

logger = get_logger()

errors_blueprint = Blueprint("errors", __name__)


def log_exception(exception: Exception, status_code: int) -> None:
    """Log the exception with the appropriate log level based on the status code."""
    log = logger.warning if status_code < 500 else logger.error

    log(
        "an error has occurred",
        exc_info=exception,
        url=request.url,
        status_code=status_code,
    )


@errors_blueprint.app_errorhandler(401)
def unauthorized(exception: Unauthorized) -> tuple[str, int]:
    """401 page.
    :return: Rendered HTML.
    """
    log_exception(exception, 401)

    return render_template("errors/401.html"), 401


@errors_blueprint.app_errorhandler(403)
def forbidden(exception: Forbidden) -> tuple[str, int]:
    """403 page.
    :return: Rendered HTML.
    """
    log_exception(exception, 403)
    return render_template("errors/403.html"), 403


@errors_blueprint.app_errorhandler(404)
def page_not_found(exception: NotFound) -> tuple[str, int]:
    """404 page.
    :return: Rendered HTML.
    """
    log_exception(exception, 404)
    return render_template("errors/404.html"), 404


@errors_blueprint.app_errorhandler(500)
def internal_server_error(exception: InternalServerError) -> tuple[str, int]:
    """500 page.
    :return: Rendered HTML.
    """
    log_exception(exception, 500)
    return render_template("errors/500.html"), 500
