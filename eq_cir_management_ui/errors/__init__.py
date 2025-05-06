from flask import Blueprint

errors_blueprint = Blueprint("errors", __name__)

# Import post blueprint declaration to avoid circular dependencies.
from eq_cir_management_ui.errors import routes  # noqa: F401
