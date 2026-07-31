"""
Provides ApiKeyCredentials for Baidu AI Platform API Key authentication.
Injects API Key as Bearer token in Authorization header.
"""
class ApiKeyCredentials(object):
    """
    Credentials for Baidu AI Platform using API Key for authentication.
    Injects API Key as Bearer token in Authorization header.
    """

    def __init__(self, api_key):
        self.api_key = api_key
