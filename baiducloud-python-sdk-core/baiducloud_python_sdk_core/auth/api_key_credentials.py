"""
Provides ApiKeyCredentials for Baidu AI Platform API Key authentication.
Injects API Key as Bearer token in Authorization header.
"""
from baiducloud_python_sdk_core.auth import api_key_signer

class ApiKeyCredentials(object):
    """
    Credentials for Baidu AI Platform using API Key for authentication.
    Injects API Key as Bearer token in Authorization header.
    """

    def __init__(self, api_key):
        self.api_key = api_key

    def sign_function(self):
        """Return the API Key signer function used to authenticate requests for this credential."""
        return api_key_signer.sign
