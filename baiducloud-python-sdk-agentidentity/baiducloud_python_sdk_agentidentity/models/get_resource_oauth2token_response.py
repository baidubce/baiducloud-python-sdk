"""
Request entity for GetResourceOauth2tokenResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetResourceOauth2tokenResponse(BceResponse):
    """
    GetResourceOauth2tokenResponse
    """

    def __init__(self, access_token=None, authorization_url=None, session_uri=None, session_status=None):
        """
        Initialize GetResourceOauth2tokenResponse response.

        :param access_token: OAuth2 access token（token 就绪时返回，与 sessionStatus 互斥）
        :type access_token: str (optional)

        :param authorization_url: 授权 URL（仅首次发起时返回）
        :type authorization_url: str (optional)

        :param session_uri: 会话标识（轮询用）
        :type session_uri: str (optional)

        :param session_status: 会话状态：IN_PROGRESS / FAILED
        :type session_status: str (optional)
        """
        super().__init__()
        self.access_token = access_token
        self.authorization_url = authorization_url
        self.session_uri = session_uri
        self.session_status = session_status

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.access_token is not None:
            result['accessToken'] = self.access_token
        if self.authorization_url is not None:
            result['authorizationUrl'] = self.authorization_url
        if self.session_uri is not None:
            result['sessionUri'] = self.session_uri
        if self.session_status is not None:
            result['sessionStatus'] = self.session_status
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetResourceOauth2tokenResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accessToken') is not None:
            self.access_token = m.get('accessToken')
        if m.get('authorizationUrl') is not None:
            self.authorization_url = m.get('authorizationUrl')
        if m.get('sessionUri') is not None:
            self.session_uri = m.get('sessionUri')
        if m.get('sessionStatus') is not None:
            self.session_status = m.get('sessionStatus')
        return self
