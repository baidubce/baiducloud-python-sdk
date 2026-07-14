"""
Request entity for TokenEndpointResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class TokenEndpointResponse(BceResponse):
    """
    TokenEndpointResponse
    """

    def __init__(
        self,
        access_token=None,
        id_token=None,
        refresh_token=None,
        token_type=None,
        expires_in=None,
        refresh_expires_in=None,
    ):
        """
        Initialize TokenEndpointResponse response.

        :param access_token: JWT 格式的 access token（始终返回）
        :type access_token: str (optional)

        :param id_token: JWT 格式的 ID token（scope 含 openid 时返回）
        :type id_token: str (optional)

        :param refresh_token: refresh_token field
        :type refresh_token: str (optional)

        :param token_type: 固定 Bearer（始终返回）
        :type token_type: str (optional)

        :param expires_in: access_token 有效期（秒），始终返回
        :type expires_in: int (optional)

        :param refresh_expires_in: refresh_token 有效期（秒），有 refresh_token 时返回
        :type refresh_expires_in: int (optional)
        """
        super().__init__()
        self.access_token = access_token
        self.id_token = id_token
        self.refresh_token = refresh_token
        self.token_type = token_type
        self.expires_in = expires_in
        self.refresh_expires_in = refresh_expires_in

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
            result['access_token'] = self.access_token
        if self.id_token is not None:
            result['id_token'] = self.id_token
        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token
        if self.token_type is not None:
            result['token_type'] = self.token_type
        if self.expires_in is not None:
            result['expires_in'] = self.expires_in
        if self.refresh_expires_in is not None:
            result['refresh_expires_in'] = self.refresh_expires_in
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TokenEndpointResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('access_token') is not None:
            self.access_token = m.get('access_token')
        if m.get('id_token') is not None:
            self.id_token = m.get('id_token')
        if m.get('refresh_token') is not None:
            self.refresh_token = m.get('refresh_token')
        if m.get('token_type') is not None:
            self.token_type = m.get('token_type')
        if m.get('expires_in') is not None:
            self.expires_in = m.get('expires_in')
        if m.get('refresh_expires_in') is not None:
            self.refresh_expires_in = m.get('refresh_expires_in')
        return self
