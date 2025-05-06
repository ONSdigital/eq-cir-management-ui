import os


def get_env_or_fail(key):
    value = os.getenv(key)
    if value is None:
        raise Exception(f"Setting '{key}' Missing")

    return value


def parse_env_as_bool(var):
    if isinstance(var, str) and var.lower().strip() in ["false", "n"]:
        return False
    return bool(var)


class DefaultConfig:
    """The default application config."""

    # Default timeout for REST requests
    DEFAULT_TIMEOUT = 5

    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key-for-development-only")
    LOG_FORMAT = os.environ.get("LOG_FORMAT", "JSON")
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

    CDN_URL = os.getenv("CDN_URL", "https://cdn.ons.gov.uk")


class DeployedConfig(DefaultConfig):
    """Configuration for the DEV and TEST environment.

    Extends DEFAULT Config.
    """

    LOG_FORMAT = "JSON"


class ProdConfig(DeployedConfig):
    """Configuration for the UAT and PROD environment.

    Extends DEPLOYED Config.
    """


# Set the config depending on the runtime environment.
match os.environ.get("RUNTIME_ENVIRONMENT", None):
    case "dev" | "staging":
        config = DeployedConfig()
    case "prod":
        config = ProdConfig()
    case _:
        config = DefaultConfig()