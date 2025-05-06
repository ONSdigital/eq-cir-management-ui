from flask import Blueprint

main_blueprint = Blueprint("main", __name__)

# Import post blueprint declaration to avoid circular dependencies.
from eq_cir_management_ui.main import routes  # noqa: F401
