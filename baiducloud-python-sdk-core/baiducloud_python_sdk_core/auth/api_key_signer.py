"""
Signer for API Key authentication.
Injects 'Authorization: Bearer <api_key>' into request headers.
"""

def sign(credentials, http_method, path, headers, params,
         timestamp=0, expiration_in_seconds=1800, headers_to_sign=None):
    return ('Bearer ' + credentials.api_key).encode('utf-8')
