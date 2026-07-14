"""
Request entity for UpdateUserPoolResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class UpdateUserPoolResponse(BceResponse):
    """
    UpdateUserPoolResponse
    """

    def __init__(
        self,
        id=None,
        domain_id=None,
        name=None,
        description=None,
        user_count=None,
        client_count=None,
        idp_count=None,
        callback_url=None,
        discovery_url=None,
        authorization_endpoint=None,
        token_endpoint=None,
        userinfo_endpoint=None,
        jwks_url=None,
        enabled=None,
        created_at=None,
    ):
        """
        Initialize UpdateUserPoolResponse response.

        :param id: 用户池 ID
        :type id: str (optional)

        :param domain_id: BCE 账户 ID
        :type domain_id: str (optional)

        :param name: 用户池名称
        :type name: str (optional)

        :param description: 用户池描述
        :type description: str (optional)

        :param user_count: 用户池内用户数量
        :type user_count: int (optional)

        :param client_count: 用户池内 OAuth2 客户端数量
        :type client_count: int (optional)

        :param idp_count: 用户池内 IdP 配置数量
        :type idp_count: int (optional)

        :param callback_url: 统一 IdP 回调地址
        :type callback_url: str (optional)

        :param discovery_url: OIDC Discovery URL
        :type discovery_url: str (optional)

        :param authorization_endpoint: 授权端点
        :type authorization_endpoint: str (optional)

        :param token_endpoint: Token 端点
        :type token_endpoint: str (optional)

        :param userinfo_endpoint: UserInfo 端点
        :type userinfo_endpoint: str (optional)

        :param jwks_url: JWKS 端点
        :type jwks_url: str (optional)

        :param enabled: 是否启用
        :type enabled: bool (optional)

        :param created_at: 创建时间
        :type created_at: datetime (optional)
        """
        super().__init__()
        self.id = id
        self.domain_id = domain_id
        self.name = name
        self.description = description
        self.user_count = user_count
        self.client_count = client_count
        self.idp_count = idp_count
        self.callback_url = callback_url
        self.discovery_url = discovery_url
        self.authorization_endpoint = authorization_endpoint
        self.token_endpoint = token_endpoint
        self.userinfo_endpoint = userinfo_endpoint
        self.jwks_url = jwks_url
        self.enabled = enabled
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
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.user_count is not None:
            result['userCount'] = self.user_count
        if self.client_count is not None:
            result['clientCount'] = self.client_count
        if self.idp_count is not None:
            result['idpCount'] = self.idp_count
        if self.callback_url is not None:
            result['callbackUrl'] = self.callback_url
        if self.discovery_url is not None:
            result['discoveryUrl'] = self.discovery_url
        if self.authorization_endpoint is not None:
            result['authorizationEndpoint'] = self.authorization_endpoint
        if self.token_endpoint is not None:
            result['tokenEndpoint'] = self.token_endpoint
        if self.userinfo_endpoint is not None:
            result['userinfoEndpoint'] = self.userinfo_endpoint
        if self.jwks_url is not None:
            result['jwksUrl'] = self.jwks_url
        if self.enabled is not None:
            result['enabled'] = self.enabled
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
        :rtype: UpdateUserPoolResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('userCount') is not None:
            self.user_count = m.get('userCount')
        if m.get('clientCount') is not None:
            self.client_count = m.get('clientCount')
        if m.get('idpCount') is not None:
            self.idp_count = m.get('idpCount')
        if m.get('callbackUrl') is not None:
            self.callback_url = m.get('callbackUrl')
        if m.get('discoveryUrl') is not None:
            self.discovery_url = m.get('discoveryUrl')
        if m.get('authorizationEndpoint') is not None:
            self.authorization_endpoint = m.get('authorizationEndpoint')
        if m.get('tokenEndpoint') is not None:
            self.token_endpoint = m.get('tokenEndpoint')
        if m.get('userinfoEndpoint') is not None:
            self.userinfo_endpoint = m.get('userinfoEndpoint')
        if m.get('jwksUrl') is not None:
            self.jwks_url = m.get('jwksUrl')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        return self
