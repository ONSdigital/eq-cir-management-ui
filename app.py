"""Module providing basic configuration."""

import os

from eq_cir_management_ui import create_app
from eq_cir_management_ui.config.config import config


app = create_app(config)

if __name__ == "__main__":
    port = os.environ.get("PORT", 5100)
    app.run(host="0.0.0.0", port=port, debug=True)
