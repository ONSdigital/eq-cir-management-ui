"""Module providing basic configuration."""

import os

from eq_cir_management_ui import create_app
from eq_cir_management_ui.config.config import config

app = create_app(config)

if __name__ == "__main__":
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", 5100))
    debug_mode = os.environ.get("FLASK_ENV") == "development"
    app.run(host=host, port=port, debug=debug_mode)
