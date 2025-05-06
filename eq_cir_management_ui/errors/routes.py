import logging

from flask import render_template

from eq_cir_management_ui.errors import errors_blueprint

logger = logging.getLogger(__name__)


@errors_blueprint.app_errorhandler(401)
def unauthorized(e):
    """401 page.

    :return: Rendered HTML.
    """
    msg = "401 Unauthorized"
    logger.error(msg)
    return render_template("errors/401.html"), 401


@errors_blueprint.app_errorhandler(403)
def forbidden(e):
    """403 page.

    :return: Rendered HTML.
    """
    msg = "403 Forbidden"
    logger.error(msg)
    return render_template("errors/403.html"), 403


@errors_blueprint.app_errorhandler(404)
def page_not_found(e):
    """404 page.

    :return: Rendered HTML.
    """
    msg = "404 Not Found"
    logger.error(msg)
    return render_template("errors/404.html"), 404


@errors_blueprint.app_errorhandler(500)
def internal_server_error(e):
    """500 page.

    :return: Rendered HTML.
    """
    msg = "500 Internal Server Error"
    logger.error(msg)
    return render_template("errors/500.html"), 500
