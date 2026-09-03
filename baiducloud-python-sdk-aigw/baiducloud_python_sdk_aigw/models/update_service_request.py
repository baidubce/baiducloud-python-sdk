"""
Request entity for UpdateServiceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateServiceRequest(AbstractModel):
    """
    Request entity for UpdateServiceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        service_name_path,
        x_region,
        service_name=None,
        service_addresses=None,
        service_protocol=None,
        provider=None,
        endpoint=None,
        api_keys=None,
        failover_enabled=None,
        failover_model=None,
        credential_source=None,
        credential_names=None,
    ):
        """
        Initialize UpdateServiceRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param service_name_path: service_name_path parameter
        :type service_name_path: str (required)

        :param service_name: 更新后的服务名称
        :type service_name: str (optional)

        :param service_addresses: 更新后的服务地址列表
        :type service_addresses: List[str] (optional)

        :param service_protocol: HTTP、HTTPS 或 HTTP&HTTPS
        :type service_protocol: str (optional)

        :param provider: AI_PROXY 模型供应商
        :type provider: str (optional)

        :param endpoint: AI_PROXY 上游端点
        :type endpoint: str (optional)

        :param api_keys: AI_PROXY API Key 列表；IAM 模式禁止传入
        :type api_keys: List[str] (optional)

        :param failover_enabled: 是否启用 Failover
        :type failover_enabled: bool (optional)

        :param failover_model: Failover 健康检查模型
        :type failover_model: str (optional)

        :param credential_source: AI_PROXY 凭证来源：DEFAULT 或 IAM
        :type credential_source: str (optional)

        :param credential_names: IAM CredentialProvider 名称列表
        :type credential_names: List[str] (optional)

        :param x_region: x_region parameter
        :type x_region: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.service_name_path = service_name_path
        self.service_name = service_name
        self.service_addresses = service_addresses
        self.service_protocol = service_protocol
        self.provider = provider
        self.endpoint = endpoint
        self.api_keys = api_keys
        self.failover_enabled = failover_enabled
        self.failover_model = failover_model
        self.credential_source = credential_source
        self.credential_names = credential_names
        self.x_region = x_region

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
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.service_addresses is not None:
            result['serviceAddresses'] = self.service_addresses
        if self.service_protocol is not None:
            result['serviceProtocol'] = self.service_protocol
        if self.provider is not None:
            result['provider'] = self.provider
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.api_keys is not None:
            result['apiKeys'] = self.api_keys
        if self.failover_enabled is not None:
            result['failoverEnabled'] = self.failover_enabled
        if self.failover_model is not None:
            result['failoverModel'] = self.failover_model
        if self.credential_source is not None:
            result['credentialSource'] = self.credential_source
        if self.credential_names is not None:
            result['credentialNames'] = self.credential_names
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateServiceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('serviceNamePath') is not None:
            self.service_name_path = m.get('serviceNamePath')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('serviceAddresses') is not None:
            self.service_addresses = m.get('serviceAddresses')
        if m.get('serviceProtocol') is not None:
            self.service_protocol = m.get('serviceProtocol')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('apiKeys') is not None:
            self.api_keys = m.get('apiKeys')
        if m.get('failoverEnabled') is not None:
            self.failover_enabled = m.get('failoverEnabled')
        if m.get('failoverModel') is not None:
            self.failover_model = m.get('failoverModel')
        if m.get('credentialSource') is not None:
            self.credential_source = m.get('credentialSource')
        if m.get('credentialNames') is not None:
            self.credential_names = m.get('credentialNames')
        if m.get('X-Region') is not None:
            self.x_region = m.get('X-Region')
        return self
