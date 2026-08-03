"""
Signer for API Key authentication.
Injects 'Authorization: Bearer <api_key>' into request headers.
"""

def sign(credentials, http_method, path, headers, params,
         timestamp=0, expiration_in_seconds=1800, headers_to_sign=None):
    """
    Build the API Key authorization header ``Bearer <api_key>``.

    Params: ``credentials`` provides ``api_key``; the remaining params are the
    unified signer signature and are unused here.
    Returns: the ``Bearer <api_key>`` header as bytes.
    """
    return ('Bearer ' + credentials.api_key).encode('utf-8')
