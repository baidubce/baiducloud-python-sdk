"""
Signer for AIP access_token authentication.
Injects access_token into request params instead of signing headers.
"""


def sign(credentials, http_method, path, headers, params,
         timestamp=0, expiration_in_seconds=1800, headers_to_sign=None):
    """
    Access-token auth builds no signature header (the access_token is injected
    into query params by the caller); returns empty.

    Params: the unified signer signature, all unused here.
    Returns: an empty byte string ``b''`` (no Authorization header set).
    """
    return b''
