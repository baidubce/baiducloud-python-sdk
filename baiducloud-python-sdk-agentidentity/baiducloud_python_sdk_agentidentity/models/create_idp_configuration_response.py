"""
CreateIdpConfigurationResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateIdpConfigurationResponse(BceResponse):
    """
    CreateIdpConfigurationResponse
    """

    def __init__(
        self,
        id=None,
        name=None,
        idp_type=None,
        idp_provider=None,
        client_id=None,
        client_secret=None,
        discovery_url=None,
        authorization_endpoint=None,
        token_endpoint=None,
        userinfo_endpoint=None,
        scopes=None,
        user_id_claim=None,
        display_name_claim=None,
        auto_create_user=None,
        enabled=None,
        callback_url=None,
        created_at=None,
    ):
        """
        Initialize CreateIdpConfigurationResponse instance.

        :param id: IdP 配置 ID
        :type id: str (optional)

        :param name: 显示名称
        :type name: str (optional)

        :param idp_type: 协议类型：OAUTH2 / OIDC / CAS
        :type idp_type: str (optional)

        :param idp_provider: OAuth2 提供方：CUSTOM / DINGTALK / FEISHU；非 OAuth2 为 null
        :type idp_provider: str (optional)

        :param client_id: OAuth2 client_id
        :type client_id: str (optional)

        :param client_secret: client_secret（get 返回明文，list 不返回）
        :type client_secret: str (optional)

        :param discovery_url: Discovery URL
        :type discovery_url: str (optional)

        :param authorization_endpoint: 授权端点
        :type authorization_endpoint: str (optional)

        :param token_endpoint: Token 端点
        :type token_endpoint: str (optional)

        :param userinfo_endpoint: UserInfo 端点
        :type userinfo_endpoint: str (optional)

        :param scopes: 请求的 scope
        :type scopes: List[str] (optional)

        :param user_id_claim: 用户 ID 映射字段
        :type user_id_claim: str (optional)

        :param display_name_claim: 显示名称映射字段
        :type display_name_claim: str (optional)

        :param auto_create_user: 是否自动创建用户
        :type auto_create_user: bool (optional)

        :param enabled: 是否启用
        :type enabled: bool (optional)

        :param callback_url: 统一 IdP 回调地址（运行时派生）
        :type callback_url: str (optional)

        :param created_at: 创建时间
        :type created_at: datetime (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.idp_type = idp_type
        self.idp_provider = idp_provider
        self.client_id = client_id
        self.client_secret = client_secret
        self.discovery_url = discovery_url
        self.authorization_endpoint = authorization_endpoint
        self.token_endpoint = token_endpoint
        self.userinfo_endpoint = userinfo_endpoint
        self.scopes = scopes
        self.user_id_claim = user_id_claim
        self.display_name_claim = display_name_claim
        self.auto_create_user = auto_create_user
        self.enabled = enabled
        self.callback_url = callback_url
        self.created_at = created_at

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
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
        if self.name is not None:
            result['name'] = self.name
        if self.idp_type is not None:
            result['idpType'] = self.idp_type
        if self.idp_provider is not None:
            result['idpProvider'] = self.idp_provider
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.client_secret is not None:
            result['clientSecret'] = self.client_secret
        if self.discovery_url is not None:
            result['discoveryUrl'] = self.discovery_url
        if self.authorization_endpoint is not None:
            result['authorizationEndpoint'] = self.authorization_endpoint
        if self.token_endpoint is not None:
            result['tokenEndpoint'] = self.token_endpoint
        if self.userinfo_endpoint is not None:
            result['userinfoEndpoint'] = self.userinfo_endpoint
        if self.scopes is not None:
            result['scopes'] = self.scopes
        if self.user_id_claim is not None:
            result['userIdClaim'] = self.user_id_claim
        if self.display_name_claim is not None:
            result['displayNameClaim'] = self.display_name_claim
        if self.auto_create_user is not None:
            result['autoCreateUser'] = self.auto_create_user
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.callback_url is not None:
            result['callbackUrl'] = self.callback_url
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateIdpConfigurationResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('idpType') is not None:
            self.idp_type = m.get('idpType')
        if m.get('idpProvider') is not None:
            self.idp_provider = m.get('idpProvider')
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('clientSecret') is not None:
            self.client_secret = m.get('clientSecret')
        if m.get('discoveryUrl') is not None:
            self.discovery_url = m.get('discoveryUrl')
        if m.get('authorizationEndpoint') is not None:
            self.authorization_endpoint = m.get('authorizationEndpoint')
        if m.get('tokenEndpoint') is not None:
            self.token_endpoint = m.get('tokenEndpoint')
        if m.get('userinfoEndpoint') is not None:
            self.userinfo_endpoint = m.get('userinfoEndpoint')
        if m.get('scopes') is not None:
            self.scopes = m.get('scopes')
        if m.get('userIdClaim') is not None:
            self.user_id_claim = m.get('userIdClaim')
        if m.get('displayNameClaim') is not None:
            self.display_name_claim = m.get('displayNameClaim')
        if m.get('autoCreateUser') is not None:
            self.auto_create_user = m.get('autoCreateUser')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('callbackUrl') is not None:
            self.callback_url = m.get('callbackUrl')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        return self
