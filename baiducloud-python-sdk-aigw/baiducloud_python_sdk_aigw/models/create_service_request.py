"""
Request entity for CreateServiceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_aigw.models.service_item import ServiceItem


class CreateServiceRequest(AbstractModel):
    """
    Request entity for CreateServiceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        service_source,
        namespace,
        x_region,
        service_name=None,
        cluster_id=None,
        cluster_ids=None,
        service_list=None,
        registry_id=None,
        service_addresses=None,
        service_protocol=None,
        provider=None,
        endpoint=None,
        api_keys=None,
        credential_source=None,
        credential_names=None,
        failover_enabled=None,
        failover_model=None,
    ):
        """
        Initialize CreateServiceRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param service_source: 服务来源：CCE、MSE、FIXED_IP、DNS_DOMAIN、CFC、AI_PROXY
        :type service_source: str (required)

        :param namespace: 服务命名空间；AI_PROXY 默认 default
        :type namespace: str (required)

        :param service_name: 固定 IP、DNS_DOMAIN 或 AI_PROXY 服务名称
        :type service_name: str (optional)

        :param cluster_id: CCE 或托管集群 ID
        :type cluster_id: str (optional)

        :param cluster_ids: CCE 多集群绑定 ID 列表
        :type cluster_ids: List[str] (optional)

        :param service_list: CCE/MSE/CFC 服务列表
        :type service_list: List[ServiceItem] (optional)

        :param registry_id: MSE 服务注册中心 ID
        :type registry_id: str (optional)

        :param service_addresses: 固定 IP 或 DNS 地址列表，格式为 host:port
        :type service_addresses: List[str] (optional)

        :param service_protocol: HTTP、HTTPS 或 HTTP&HTTPS
        :type service_protocol: str (optional)

        :param provider: AI_PROXY 模型供应商，如 QIANFAN、DEEPSEEK、OPENAI
        :type provider: str (optional)

        :param endpoint: 模型供应商端点；Qianfan 使用 https://qianfan.baidubce.com/v2
        :type endpoint: str (optional)

        :param api_keys: 模型供应商 API Key 列表；IAM 模式禁止传入
        :type api_keys: List[str] (optional)

        :param credential_source: AI_PROXY 凭证来源：DEFAULT 或 IAM
        :type credential_source: str (optional)

        :param credential_names: IAM CredentialProvider 名称列表
        :type credential_names: List[str] (optional)

        :param failover_enabled: 是否启用模型 Failover
        :type failover_enabled: bool (optional)

        :param failover_model: Failover 健康检查模型
        :type failover_model: str (optional)

        :param x_region: x_region parameter
        :type x_region: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.service_source = service_source
        self.namespace = namespace
        self.service_name = service_name
        self.cluster_id = cluster_id
        self.cluster_ids = cluster_ids
        self.service_list = service_list
        self.registry_id = registry_id
        self.service_addresses = service_addresses
        self.service_protocol = service_protocol
        self.provider = provider
        self.endpoint = endpoint
        self.api_keys = api_keys
        self.credential_source = credential_source
        self.credential_names = credential_names
        self.failover_enabled = failover_enabled
        self.failover_model = failover_model
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
        if self.service_source is not None:
            result['serviceSource'] = self.service_source
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.cluster_ids is not None:
            result['clusterIds'] = self.cluster_ids
        if self.service_list is not None:
            result['serviceList'] = [i.to_dict() for i in self.service_list]
        if self.registry_id is not None:
            result['registryId'] = self.registry_id
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
        if self.credential_source is not None:
            result['credentialSource'] = self.credential_source
        if self.credential_names is not None:
            result['credentialNames'] = self.credential_names
        if self.failover_enabled is not None:
            result['failoverEnabled'] = self.failover_enabled
        if self.failover_model is not None:
            result['failoverModel'] = self.failover_model
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateServiceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('serviceSource') is not None:
            self.service_source = m.get('serviceSource')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('clusterIds') is not None:
            self.cluster_ids = m.get('clusterIds')
        if m.get('serviceList') is not None:
            self.service_list = [ServiceItem().from_dict(i) for i in m.get('serviceList')]
        if m.get('registryId') is not None:
            self.registry_id = m.get('registryId')
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
        if m.get('credentialSource') is not None:
            self.credential_source = m.get('credentialSource')
        if m.get('credentialNames') is not None:
            self.credential_names = m.get('credentialNames')
        if m.get('failoverEnabled') is not None:
            self.failover_enabled = m.get('failoverEnabled')
        if m.get('failoverModel') is not None:
            self.failover_model = m.get('failoverModel')
        if m.get('X-Region') is not None:
            self.x_region = m.get('X-Region')
        return self
