"""Configuration for the EQ CIR Management UI application."""

import os


class DefaultConfig:  # pylint: disable=too-few-public-methods
    """The default application config."""

    # Default timeout for REST requests
    DEFAULT_TIMEOUT = 5

    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key-for-development-only")
    LOG_FORMAT = os.environ.get("LOG_FORMAT", "JSON")
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

    CDN_URL = os.getenv("CDN_URL", "https://cdn.ons.gov.uk")


class DeployedConfig(DefaultConfig):  # pylint: disable=too-few-public-methods
    """Configuration for the DEV and TEST environment.

    Extends DEFAULT Config.
    """

    LOG_FORMAT = "JSON"


class ProdConfig(DeployedConfig):  # pylint: disable=too-few-public-methods
    """Configuration for the UAT and PROD environment.

    Extends DEPLOYED Config.
    """


# Set the config depending on the runtime environment.
match os.environ.get("RUNTIME_ENVIRONMENT", None):
    case _:
        config = DefaultConfig()
