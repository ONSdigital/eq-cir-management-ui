"""Configuration for the EQ CIR Management UI application."""

import os


class DefaultConfig:  # pylint: disable=too-few-public-methods
    """The default application config."""

    LOG_FORMAT = os.environ.get("LOG_FORMAT", "JSON")
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

    CDN_URL = os.getenv("CDN_URL", "https://cdn.ons.gov.uk")
    SESSION_COOKIE_SECURE = False


class DeployedConfig(DefaultConfig):  # pylint: disable=too-few-public-methods
    """Configuration for the STAGING environment.

    Extends DEFAULT Config.
    """

    LOG_FORMAT = "JSON"


# Set the config depending on the runtime environment.
match os.environ.get("RUNTIME_ENVIRONMENT", None):
    case _:
        config = DefaultConfig()
