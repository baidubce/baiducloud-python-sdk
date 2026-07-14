"""
Request entity for GetOauth2ClientResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetOauth2ClientResponse(BceResponse):
    """
    GetOauth2ClientResponse
    """

    def __init__(
        self,
        id=None,
        client_id=None,
        client_secret=None,
        name=None,
        description=None,
        client_type=None,
        redirect_uris=None,
        grant_types=None,
        scopes=None,
        access_token_ttl=None,
        refresh_token_ttl=None,
        enabled=None,
        login_url=None,
        created_at=None,
    ):
        """
        Initialize GetOauth2ClientResponse response.

        :param id: 客户端记录 ID
        :type id: str (optional)

        :param client_id: OAuth2 client_id
        :type client_id: str (optional)

        :param client_secret: client_secret（get 返回明文，list 不返回）
        :type client_secret: str (optional)

        :param name: 客户端名称
        :type name: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param client_type: 客户端类型：WEB_APP / SPA / M2M
        :type client_type: str (optional)

        :param redirect_uris: 回调地址白名单
        :type redirect_uris: List[str] (optional)

        :param grant_types: 授权类型
        :type grant_types: List[str] (optional)

        :param scopes: 允许的 scope
        :type scopes: List[str] (optional)

        :param access_token_ttl: access_token 有效期（秒）
        :type access_token_ttl: int (optional)

        :param refresh_token_ttl: refresh_token 有效期（秒）
        :type refresh_token_ttl: int (optional)

        :param enabled: 是否启用
        :type enabled: bool (optional)

        :param login_url: 拼装好的 OAuth2 authorize 链接
        :type login_url: str (optional)

        :param created_at: 创建时间
        :type created_at: datetime (optional)
        """
        super().__init__()
        self.id = id
        self.client_id = client_id
        self.client_secret = client_secret
        self.name = name
        self.description = description
        self.client_type = client_type
        self.redirect_uris = redirect_uris
        self.grant_types = grant_types
        self.scopes = scopes
        self.access_token_ttl = access_token_ttl
        self.refresh_token_ttl = refresh_token_ttl
        self.enabled = enabled
        self.login_url = login_url
        self.created_at = created_at

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
        if self.id is not None:
            result['id'] = self.id
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.client_secret is not None:
            result['clientSecret'] = self.client_secret
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
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.login_url is not None:
            result['loginUrl'] = self.login_url
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetOauth2ClientResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('clientSecret') is not None:
            self.client_secret = m.get('clientSecret')
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
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('loginUrl') is not None:
            self.login_url = m.get('loginUrl')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        return self
