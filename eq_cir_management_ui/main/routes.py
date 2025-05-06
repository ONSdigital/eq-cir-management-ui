
import logging
import time

from flask import (
    render_template,
    request,
    redirect,
    url_for
)


from requests import HTTPError

from eq_cir_management_ui.config.config import config
from eq_cir_management_ui.main import main_blueprint
from eq_cir_management_ui.forms.validation_version_form import ValidationVersionForm

logger = logging.getLogger(__name__)


@main_blueprint.before_request
def before_request_func():
    if request.endpoint != "health-check":
        msg = "Request received"
        logger.info(msg)


@main_blueprint.route("/", methods=["GET", "POST"])
def home():
    """Common URL defaults.

    :return: 301 redirect to start page.
    """

    if request.method == "GET":
        return render_template("home.html")

    else:
        time.sleep(3)
        return redirect(
                        url_for(
                            "main.start_migration"
                        )
                    )


@main_blueprint.route("/start-migration", methods=["GET", "POST"])
def start_migration():
    """Common URL defaults.

    :return: 301 redirect to start page.
    """

    form = ValidationVersionForm()

    if form.validate_on_submit():  
        return redirect(
            url_for(
                "main.migrating"
            )
        )
    else:

        return render_template("start-migration.html", form=form)


@main_blueprint.route("/migrating", methods=["GET", "POST"])
def migrating():
    """Common URL defaults.

    :return: 301 redirect to start page.
    """

    return render_template("migrating.html")
        

@main_blueprint.route("/health-check")
def health():
    """Health check endpoint.

    :return: Empty 200 response.
    """

    return "", 200