"""
Request entity for CreateOauth2ClientRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateOauth2ClientRequest(AbstractModel):
    """
    Request entity for CreateOauth2ClientRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        user_pool_id,
        name,
        redirect_uris,
        description=None,
        client_type=None,
        grant_types=None,
        scopes=None,
        access_token_ttl=None,
        refresh_token_ttl=None,
    ):
        """
        Initialize CreateOauth2ClientRequest request entity.

        :param user_pool_id: 用户池 ID
        :type user_pool_id: str (required)

        :param name: 客户端名称（1-64字符，池内唯一）
        :type name: str (required)

        :param description: 描述（最多128字符）
        :type description: str (optional)

        :param client_type: 客户端类型：WEB_APP / SPA / M2M，默认 WEB_APP
        :type client_type: str (optional)

        :param redirect_uris: 允许的回调地址白名单（至少1个，最多20个）
        :type redirect_uris: List[str] (required)

        :param grant_types: 允许的授权类型，默认 [\"authorization_code\"]
        :type grant_types: List[str] (optional)

        :param scopes: 允许的 scope
        :type scopes: List[str] (optional)

        :param access_token_ttl: access_token 有效期（秒），默认 3600
        :type access_token_ttl: int (optional)

        :param refresh_token_ttl: refresh_token 有效期（秒），默认 604800
        :type refresh_token_ttl: int (optional)
        """
        super().__init__()
        self.user_pool_id = user_pool_id
        self.name = name
        self.description = description
        self.client_type = client_type
        self.redirect_uris = redirect_uris
        self.grant_types = grant_types
        self.scopes = scopes
        self.access_token_ttl = access_token_ttl
        self.refresh_token_ttl = refresh_token_ttl

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
        if self.user_pool_id is not None:
            result['userPoolId'] = self.user_pool_id
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.client_type is not None:
            result['clientType'] = self.client_type
        if self.redirect_uris is not None:
            result['redirectUris'] = self.redirect_uris
        if self.grant_types is not None:
            result['grantTypes'] = self.grant_types
        if self.scopes is not None:
            result['scopes'] = self.scopes
        if self.access_token_ttl is not None:
            result['accessTokenTtl'] = self.access_token_ttl
        if self.refresh_token_ttl is not None:
            result['refreshTokenTtl'] = self.refresh_token_ttl
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateOauth2ClientRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userPoolId') is not None:
            self.user_pool_id = m.get('userPoolId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('clientType') is not None:
            self.client_type = m.get('clientType')
        if m.get('redirectUris') is not None:
            self.redirect_uris = m.get('redirectUris')
        if m.get('grantTypes') is not None:
            self.grant_types = m.get('grantTypes')
        if m.get('scopes') is not None:
            self.scopes = m.get('scopes')
        if m.get('accessTokenTtl') is not None:
            self.access_token_ttl = m.get('accessTokenTtl')
        if m.get('refreshTokenTtl') is not None:
            self.refresh_token_ttl = m.get('refreshTokenTtl')
        return self
