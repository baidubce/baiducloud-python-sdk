"""
CredentialConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CredentialConfig(AbstractModel):
    """
    CredentialConfig
    """

    def __init__(
        self,
        api_key=None,
        config_type=None,
        provider=None,
        discovery_url=None,
        issuer=None,
        authorization_endpoint=None,
        token_endpoint=None,
        userinfo_endpoint=None,
        jwks_uri=None,
        client_id=None,
        client_secret=None,
        scopes=None,
        redirect_uri=None,
        token_encryption_key_id=None,
        role_arn=None,
        external_id=None,
        duration_seconds=None,
    ):
        """
        Initialize CredentialConfig instance.

        :param api_key: 【API_KEY】API Key 的 KMS Secret ID（非明文）
        :type api_key: str (optional)

        :param config_type: 【OAUTH2】配置模式：AUTO_DISCOVERY / MANUAL
        :type config_type: str (optional)

        :param provider: 【OAUTH2】提供方：CUSTOM / DINGTALK / FEISHU，默认 CUSTOM
        :type provider: str (optional)

        :param discovery_url: 【OAUTH2】OIDC Discovery URL（AUTO_DISCOVERY 模式）
        :type discovery_url: str (optional)

        :param issuer: 【OAUTH2】签发者
        :type issuer: str (optional)

        :param authorization_endpoint: 【OAUTH2】授权端点
        :type authorization_endpoint: str (optional)

        :param token_endpoint: 【OAUTH2】Token 端点
        :type token_endpoint: str (optional)

        :param userinfo_endpoint: 【OAUTH2】UserInfo 端点
        :type userinfo_endpoint: str (optional)

        :param jwks_uri: 【OAUTH2】JWKS 端点
        :type jwks_uri: str (optional)

        :param client_id: 【OAUTH2】client_id
        :type client_id: str (optional)

        :param client_secret: 【OAUTH2】client_secret 的 KMS Secret ID（非明文）
        :type client_secret: str (optional)

        :param scopes: 【OAUTH2】scope 列表，逗号分隔
        :type scopes: str (optional)

        :param redirect_uri: 【OAUTH2】回调地址（系统生成）
        :type redirect_uri: str (optional)

        :param token_encryption_key_id: 【OAUTH2】Token Vault 加密密钥的 KMS Secret ID（系统生成）
        :type token_encryption_key_id: str (optional)

        :param role_arn: 【STS】角色 ARN
        :type role_arn: str (optional)

        :param external_id: 【STS】外部 ID（可选）
        :type external_id: str (optional)

        :param duration_seconds: 【STS】临时凭证有效期（秒）
        :type duration_seconds: int (optional)
        """
        super().__init__()
        self.api_key = api_key
        self.config_type = config_type
        self.provider = provider
        self.discovery_url = discovery_url
        self.issuer = issuer
        self.authorization_endpoint = authorization_endpoint
        self.token_endpoint = token_endpoint
        self.userinfo_endpoint = userinfo_endpoint
        self.jwks_uri = jwks_uri
        self.client_id = client_id
        self.client_secret = client_secret
        self.scopes = scopes
        self.redirect_uri = redirect_uri
        self.token_encryption_key_id = token_encryption_key_id
        self.role_arn = role_arn
        self.external_id = external_id
        self.duration_seconds = duration_seconds

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.api_key is not None:
            result['apiKey'] = self.api_key
        if self.config_type is not None:
            result['configType'] = self.config_type
        if self.provider is not None:
            result['provider'] = self.provider
        if self.discovery_url is not None:
            result['discoveryUrl'] = self.discovery_url
        if self.issuer is not None:
            result['issuer'] = self.issuer
        if self.authorization_endpoint is not None:
            result['authorizationEndpoint'] = self.authorization_endpoint
        if self.token_endpoint is not None:
            result['tokenEndpoint'] = self.token_endpoint
        if self.userinfo_endpoint is not None:
            result['userinfoEndpoint'] = self.userinfo_endpoint
        if self.jwks_uri is not None:
            result['jwksUri'] = self.jwks_uri
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.client_secret is not None:
            result['clientSecret'] = self.client_secret
        if self.scopes is not None:
            result['scopes'] = self.scopes
        if self.redirect_uri is not None:
            result['redirectUri'] = self.redirect_uri
        if self.token_encryption_key_id is not None:
            result['tokenEncryptionKeyId'] = self.token_encryption_key_id
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.external_id is not None:
            result['externalId'] = self.external_id
        if self.duration_seconds is not None:
            result['durationSeconds'] = self.duration_seconds
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CredentialConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')
        if m.get('configType') is not None:
            self.config_type = m.get('configType')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('discoveryUrl') is not None:
            self.discovery_url = m.get('discoveryUrl')
        if m.get('issuer') is not None:
            self.issuer = m.get('issuer')
        if m.get('authorizationEndpoint') is not None:
            self.authorization_endpoint = m.get('authorizationEndpoint')
        if m.get('tokenEndpoint') is not None:
            self.token_endpoint = m.get('tokenEndpoint')
        if m.get('userinfoEndpoint') is not None:
            self.userinfo_endpoint = m.get('userinfoEndpoint')
        if m.get('jwksUri') is not None:
            self.jwks_uri = m.get('jwksUri')
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('clientSecret') is not None:
            self.client_secret = m.get('clientSecret')
        if m.get('scopes') is not None:
            self.scopes = m.get('scopes')
        if m.get('redirectUri') is not None:
            self.redirect_uri = m.get('redirectUri')
        if m.get('tokenEncryptionKeyId') is not None:
            self.token_encryption_key_id = m.get('tokenEncryptionKeyId')
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('externalId') is not None:
            self.external_id = m.get('externalId')
        if m.get('durationSeconds') is not None:
            self.duration_seconds = m.get('durationSeconds')
        return self
