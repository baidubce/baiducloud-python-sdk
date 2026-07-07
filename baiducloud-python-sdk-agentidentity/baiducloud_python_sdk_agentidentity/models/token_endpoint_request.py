"""
Request entity for TokenEndpointRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TokenEndpointRequest(AbstractModel):
    """
    Request entity for TokenEndpointRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, user_pool_id, grant_type, client_id, client_secret, code=None, refresh_token=None, redirect_uri=None
    ):
        """
        Initialize TokenEndpointRequest request entity.

        :param user_pool_id: user_pool_id parameter
        :type user_pool_id: str (required)

        :param grant_type: authorization_code 或 refresh_token
        :type grant_type: str (required)

        :param code: （条件必填）授权码（grant_type=authorization_code 时必填）
        :type code: str (optional)

        :param refresh_token: （条件必填）之前签发的 refresh_token JWT（grant_type=refresh_token 时必填）
        :type refresh_token: str (optional)

        :param client_id: OAuth2 client_id
        :type client_id: str (required)

        :param client_secret: OAuth2 client_secret
        :type client_secret: str (required)

        :param redirect_uri: （条件必填）需与 authorize 时一致（grant_type=authorization_code 时必填）
        :type redirect_uri: str (optional)
        """
        super().__init__()
        self.user_pool_id = user_pool_id
        self.grant_type = grant_type
        self.code = code
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.grant_type is not None:
            result['grant_type'] = self.grant_type
        if self.code is not None:
            result['code'] = self.code
        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token
        if self.client_id is not None:
            result['client_id'] = self.client_id
        if self.client_secret is not None:
            result['client_secret'] = self.client_secret
        if self.redirect_uri is not None:
            result['redirect_uri'] = self.redirect_uri
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TokenEndpointRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userPoolId') is not None:
            self.user_pool_id = m.get('userPoolId')
        if m.get('grant_type') is not None:
            self.grant_type = m.get('grant_type')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('refresh_token') is not None:
            self.refresh_token = m.get('refresh_token')
        if m.get('client_id') is not None:
            self.client_id = m.get('client_id')
        if m.get('client_secret') is not None:
            self.client_secret = m.get('client_secret')
        if m.get('redirect_uri') is not None:
            self.redirect_uri = m.get('redirect_uri')
        return self
