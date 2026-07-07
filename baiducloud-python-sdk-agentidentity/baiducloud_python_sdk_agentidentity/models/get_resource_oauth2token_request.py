"""
Request entity for GetResourceOauth2tokenRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_core.annotation import host


class GetResourceOauth2tokenRequest(AbstractModel):
    """
    Request entity for GetResourceOauth2tokenRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        x_bce_workload_access_token,
        workload_access_token,
        resource_credential_provider_name=None,
        scopes=None,
        oauth2_flow=None,
        resource_oauth2_return_url=None,
        session_uri=None,
        force_authentication=None,
    ):
        """
        Initialize GetResourceOauth2tokenRequest request entity.

        :param x_bce_workload_access_token: x_bce_workload_access_token parameter
        :type x_bce_workload_access_token: str (required)

        :param resource_credential_provider_name: （首次调用必填）凭证提供方名称
        :type resource_credential_provider_name: str (optional)

        :param scopes: OAuth2 scope 列表，不传则使用 provider 默认值
        :type scopes: List[str] (optional)

        :param oauth2_flow: 默认 USER_FEDERATION（3LO）
        :type oauth2_flow: str (optional)

        :param resource_oauth2_return_url: （首次调用必填）客户端回调 URL，需在 Agent 白名单中注册
        :type resource_oauth2_return_url: str (optional)

        :param session_uri: （轮询时必填）首次请求返回的 sessionUri
        :type session_uri: str (optional)

        :param force_authentication: 默认 false，true 时跳过缓存强制重新授权
        :type force_authentication: bool (optional)

        :param workload_access_token: WAT（Body 传递，也可通过 Header 传递）
        :type workload_access_token: str (required)
        """
        super().__init__()
        self._x_bce_workload_access_token = x_bce_workload_access_token
        self.resource_credential_provider_name = resource_credential_provider_name
        self.scopes = scopes
        self.oauth2_flow = oauth2_flow
        self.resource_oauth2_return_url = resource_oauth2_return_url
        self.session_uri = session_uri
        self.force_authentication = force_authentication
        self.workload_access_token = workload_access_token

    @property
    @host
    def x_bce_workload_access_token(self):
        """x_bce_workload_access_token property"""
        return self._x_bce_workload_access_token

    @x_bce_workload_access_token.setter
    def x_bce_workload_access_token(self, value):
        """Set x_bce_workload_access_token value"""
        self._x_bce_workload_access_token = value

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
        if self.resource_credential_provider_name is not None:
            result['resourceCredentialProviderName'] = self.resource_credential_provider_name
        if self.scopes is not None:
            result['scopes'] = self.scopes
        if self.oauth2_flow is not None:
            result['oauth2Flow'] = self.oauth2_flow
        if self.resource_oauth2_return_url is not None:
            result['resourceOauth2ReturnUrl'] = self.resource_oauth2_return_url
        if self.session_uri is not None:
            result['sessionUri'] = self.session_uri
        if self.force_authentication is not None:
            result['forceAuthentication'] = self.force_authentication
        if self.workload_access_token is not None:
            result['workloadAccessToken'] = self.workload_access_token
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetResourceOauth2tokenRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('xBceWorkloadAccessToken') is not None:
            self.x_bce_workload_access_token = m.get('xBceWorkloadAccessToken')
        if m.get('resourceCredentialProviderName') is not None:
            self.resource_credential_provider_name = m.get('resourceCredentialProviderName')
        if m.get('scopes') is not None:
            self.scopes = m.get('scopes')
        if m.get('oauth2Flow') is not None:
            self.oauth2_flow = m.get('oauth2Flow')
        if m.get('resourceOauth2ReturnUrl') is not None:
            self.resource_oauth2_return_url = m.get('resourceOauth2ReturnUrl')
        if m.get('sessionUri') is not None:
            self.session_uri = m.get('sessionUri')
        if m.get('forceAuthentication') is not None:
            self.force_authentication = m.get('forceAuthentication')
        if m.get('workloadAccessToken') is not None:
            self.workload_access_token = m.get('workloadAccessToken')
        return self
