"""Errors routes."""

from flask import Blueprint, render_template, request
from structlog import get_logger
from werkzeug.exceptions import (
    BadRequest,
    Forbidden,
    InternalServerError,
    MethodNotAllowed,
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


@errors_blueprint.app_errorhandler(400)
def bad_request(exception: BadRequest) -> tuple[str, int]:
    """400 page.
    :return: Rendered HTML.
    This is deliberately returning the 500 page.
    """
    log_exception(exception, 400)
    page_title = "Internal Server Error"
    return render_template("errors/500.html", page_title=page_title), 400


@errors_blueprint.app_errorhandler(401)
def unauthorized(exception: Unauthorized) -> tuple[str, int]:
    """401 page.
    :return: Rendered HTML.
    """
    log_exception(exception, 401)
    page_title = "Unauthorised"
    return render_template("errors/401.html", page_title=page_title), 401


@errors_blueprint.app_errorhandler(403)
def forbidden(exception: Forbidden) -> tuple[str, int]:
    """403 page.
    :return: Rendered HTML.
    """
    log_exception(exception, 403)
    page_title = "Forbidden"
    return render_template("errors/403.html", page_title=page_title), 403


@errors_blueprint.app_errorhandler(404)
def page_not_found(exception: NotFound) -> tuple[str, int]:
    """404 page.
    :return: Rendered HTML.
    """
    log_exception(exception, 404)
    page_title = "Page not found"
    return render_template("errors/404.html", page_title=page_title), 404


@errors_blueprint.app_errorhandler(405)
def method_not_allowed(exception: MethodNotAllowed) -> tuple[str, int]:
    """405 page.
    :return: Rendered HTML.
    This is deliberately returning the 404 page.
    """
    log_exception(exception, 405)
    page_title = "Page not found"
    return render_template("errors/404.html", page_title=page_title), 405


@errors_blueprint.app_errorhandler(500)
def internal_server_error(exception: InternalServerError) -> tuple[str, int]:
    """500 page.
    :return: Rendered HTML.
    """
    log_exception(exception, 500)
    page_title = "Internal Server Error"
    return render_template("errors/500.html", page_title=page_title), 500
