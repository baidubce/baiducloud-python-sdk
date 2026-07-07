"""
Request entity for CreateIdpConfigurationRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateIdpConfigurationRequest(AbstractModel):
    """
    Request entity for CreateIdpConfigurationRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        user_pool_id,
        name,
        idp_type,
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
    ):
        """
        Initialize CreateIdpConfigurationRequest request entity.

        :param user_pool_id: 用户池 ID
        :type user_pool_id: str (required)

        :param name: IdP 显示名称（1-64字符，池内唯一）
        :type name: str (required)

        :param idp_type: 协议类型：OAUTH2 / OIDC / CAS
        :type idp_type: str (required)

        :param idp_provider: idp_provider parameter
        :type idp_provider: str (optional)

        :param client_id: （条件必填）OAuth2 client_id（OAuth2 协议必填）
        :type client_id: str (optional)

        :param client_secret: （条件必填）OAuth2 client_secret 明文（OAuth2 协议必填，加密存储）
        :type client_secret: str (optional)

        :param discovery_url: OAuth2/OIDC Discovery URL（提供后自动解析端点）
        :type discovery_url: str (optional)

        :param authorization_endpoint: （条件必填）授权端点（idpProvider=CUSTOM 且无 discoveryUrl 时必填）
        :type authorization_endpoint: str (optional)

        :param token_endpoint: （条件必填）Token 端点（idpProvider=CUSTOM 且无 discoveryUrl 时必填）
        :type token_endpoint: str (optional)

        :param userinfo_endpoint: （条件必填）UserInfo 端点（idpProvider=CUSTOM 且无 discoveryUrl 时必填）
        :type userinfo_endpoint: str (optional)

        :param scopes: 请求的 scope 列表
        :type scopes: List[str] (optional)

        :param user_id_claim: IdP 用户信息中映射到本地 username 的字段名
        :type user_id_claim: str (optional)

        :param display_name_claim: IdP 用户信息中映射到本地 displayName 的字段名
        :type display_name_claim: str (optional)

        :param auto_create_user: 登录时用户不存在是否自动创建，默认 false
        :type auto_create_user: bool (optional)
        """
        super().__init__()
        self.user_pool_id = user_pool_id
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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateIdpConfigurationRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userPoolId') is not None:
            self.user_pool_id = m.get('userPoolId')
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
        return self
