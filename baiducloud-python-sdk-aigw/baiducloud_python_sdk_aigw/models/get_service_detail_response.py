"""
Request entity for GetServiceDetailResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetServiceDetailResponse(BceResponse):
    """
    GetServiceDetailResponse
    """

    def __init__(
        self,
        cluster_id=None,
        cluster_ids=None,
        namespace=None,
        route_count=None,
        service_source=None,
        service_status=None,
        service_port=None,
        service_addresses=None,
        service_protocol=None,
        mcp_server_hosts=None,
        provider=None,
        endpoint=None,
        api_keys=None,
        failover_enabled=None,
        failover_model=None,
        failure_threshold=None,
        health_check_interval=None,
        health_check_timeout=None,
        credential_source=None,
        credential_names=None,
    ):
        """
        Initialize GetServiceDetailResponse response.

        :param cluster_id: 关联集群 ID
        :type cluster_id: str (optional)

        :param cluster_ids: 关联集群 ID 列表
        :type cluster_ids: List[str] (optional)

        :param namespace: 服务命名空间
        :type namespace: str (optional)

        :param route_count: 关联路由数量
        :type route_count: int (optional)

        :param service_source: 服务来源
        :type service_source: str (optional)

        :param service_status: 服务状态
        :type service_status: str (optional)

        :param service_port: 服务端口列表
        :type service_port: List[str] (optional)

        :param service_addresses: 服务地址列表
        :type service_addresses: List[str] (optional)

        :param service_protocol: 服务协议
        :type service_protocol: str (optional)

        :param mcp_server_hosts: 上游 MCP Server 主机列表
        :type mcp_server_hosts: List[str] (optional)

        :param provider: AI_PROXY 模型供应商
        :type provider: str (optional)

        :param endpoint: AI_PROXY 上游端点
        :type endpoint: str (optional)

        :param api_keys: AI_PROXY API Key 列表，返回值按后端规则脱敏
        :type api_keys: List[str] (optional)

        :param failover_enabled: 是否启用 Failover
        :type failover_enabled: bool (optional)

        :param failover_model: Failover 健康检查模型
        :type failover_model: str (optional)

        :param failure_threshold: Failover 连续失败阈值
        :type failure_threshold: int (optional)

        :param health_check_interval: 健康检查间隔
        :type health_check_interval: int (optional)

        :param health_check_timeout: 健康检查超时时间
        :type health_check_timeout: int (optional)

        :param credential_source: AI_PROXY 凭证来源：DEFAULT 或 IAM
        :type credential_source: str (optional)

        :param credential_names: IAM CredentialProvider 名称列表
        :type credential_names: List[str] (optional)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.cluster_ids = cluster_ids
        self.namespace = namespace
        self.route_count = route_count
        self.service_source = service_source
        self.service_status = service_status
        self.service_port = service_port
        self.service_addresses = service_addresses
        self.service_protocol = service_protocol
        self.mcp_server_hosts = mcp_server_hosts
        self.provider = provider
        self.endpoint = endpoint
        self.api_keys = api_keys
        self.failover_enabled = failover_enabled
        self.failover_model = failover_model
        self.failure_threshold = failure_threshold
        self.health_check_interval = health_check_interval
        self.health_check_timeout = health_check_timeout
        self.credential_source = credential_source
        self.credential_names = credential_names

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
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.cluster_ids is not None:
            result['clusterIds'] = self.cluster_ids
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.route_count is not None:
            result['routeCount'] = self.route_count
        if self.service_source is not None:
            result['serviceSource'] = self.service_source
        if self.service_status is not None:
            result['serviceStatus'] = self.service_status
        if self.service_port is not None:
            result['servicePort'] = self.service_port
        if self.service_addresses is not None:
            result['serviceAddresses'] = self.service_addresses
        if self.service_protocol is not None:
            result['serviceProtocol'] = self.service_protocol
        if self.mcp_server_hosts is not None:
            result['mcpServerHosts'] = self.mcp_server_hosts
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
        if self.failure_threshold is not None:
            result['failureThreshold'] = self.failure_threshold
        if self.health_check_interval is not None:
            result['healthCheckInterval'] = self.health_check_interval
        if self.health_check_timeout is not None:
            result['healthCheckTimeout'] = self.health_check_timeout
        if self.credential_source is not None:
            result['credentialSource'] = self.credential_source
        if self.credential_names is not None:
            result['credentialNames'] = self.credential_names
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetServiceDetailResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('clusterIds') is not None:
            self.cluster_ids = m.get('clusterIds')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('routeCount') is not None:
            self.route_count = m.get('routeCount')
        if m.get('serviceSource') is not None:
            self.service_source = m.get('serviceSource')
        if m.get('serviceStatus') is not None:
            self.service_status = m.get('serviceStatus')
        if m.get('servicePort') is not None:
            self.service_port = m.get('servicePort')
        if m.get('serviceAddresses') is not None:
            self.service_addresses = m.get('serviceAddresses')
        if m.get('serviceProtocol') is not None:
            self.service_protocol = m.get('serviceProtocol')
        if m.get('mcpServerHosts') is not None:
            self.mcp_server_hosts = m.get('mcpServerHosts')
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
        if m.get('failureThreshold') is not None:
            self.failure_threshold = m.get('failureThreshold')
        if m.get('healthCheckInterval') is not None:
            self.health_check_interval = m.get('healthCheckInterval')
        if m.get('healthCheckTimeout') is not None:
            self.health_check_timeout = m.get('healthCheckTimeout')
        if m.get('credentialSource') is not None:
            self.credential_source = m.get('credentialSource')
        if m.get('credentialNames') is not None:
            self.credential_names = m.get('credentialNames')
        return self
