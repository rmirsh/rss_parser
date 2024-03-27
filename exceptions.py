import httpx


class EmptyResponseError(Exception):
    """Response is empty"""


class HTTPError(httpx.HTTPError):
    """HTTP error"""
