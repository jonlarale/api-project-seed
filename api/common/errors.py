class Error(Exception):
    """Base class for exceptions"""

    def __init__(self, message: str=None, error_code: str=None, data: dict=None) -> None:
        self.message = message


class ResourceNotFound(Error):
    """Exception raised when a requested resource doesn't exist."""


class InvalidPayload(Error):
    """Exception raised when a request has invalid headers, body or query parameters."""


class ThirdPartyError(Error):
    """Exception raised when a third party service fails."""