"""
Signer for AIP access_token authentication.
Injects access_token into request params instead of signing headers.
"""


def sign(credentials, http_method, path, headers, params,
         timestamp=0, expiration_in_seconds=1800, headers_to_sign=None):
    return b''
