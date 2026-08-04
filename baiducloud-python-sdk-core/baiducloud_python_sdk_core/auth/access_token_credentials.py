"""
Provides AccessTokenCredentials for AIP (AI Platform) authentication.
Uses api_key/secret_key to obtain and cache access_token from OAuth endpoint.
"""
import json
import time
from http.client import HTTPSConnection
from urllib.parse import urlencode
from baiducloud_python_sdk_core.auth import access_token_signer


class AccessTokenCredentials(object):
    """
    Credentials for Baidu AI Platform using api_key/secret_key to obtain access_token.
    Token is cached and auto-refreshed before expiry.
    """

    TOKEN_HOST = "aip.baidubce.com"
    TOKEN_PATH = "/oauth/2.0/token"

    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        self._token = None
        self._expire_at = 0

    def get_access_token(self):
        """Return cached token, fetching a new one if expired or missing."""
        if self._token is None or time.time() >= self._expire_at - 24 * 3600:
            self._refresh_token()
        return self._token

    def sign_function(self):
        """Return the access-token signer function used to authenticate requests for this credential."""
        return access_token_signer.sign

    def _refresh_token(self):
        path = self.TOKEN_PATH + '?' + urlencode({
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.secret_key,
        })
        max_retry = 3
        for attempt in range(max_retry):
            conn = HTTPSConnection(self.TOKEN_HOST, timeout=30)
            try:
                conn.request('GET', path)
                response = conn.getresponse()
                status = response.status
                body = response.read()
            finally:
                conn.close()
            if status == 500 and attempt < max_retry - 1:
                continue
            if status != 200:
                raise Exception('Failed to get access token, status code: %d' % status)
            data = json.loads(body)
            self._token = data['access_token']
            expires_in = int(data.get('expires_in', 2592000))
            self._expire_at = time.time() + expires_in
            return
        raise Exception('Failed to refresh access token after %d retries.' % max_retry)
