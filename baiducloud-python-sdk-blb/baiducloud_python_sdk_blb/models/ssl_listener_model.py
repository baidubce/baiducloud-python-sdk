"""
SSLListenerModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SSLListenerModel(AbstractModel):
    """
    SSLListenerModel
    """

    def __init__(
        self,
        listener_port=None,
        backend_port=None,
        scheduler=None,
        health_check_timeout_in_second=None,
        health_check_interval=None,
        unhealthy_threshold=None,
        healthy_threshold=None,
        cert_ids=None,
        encryption_type=None,
        encryption_protocols=None,
        applied_ciphers=None,
        dual_auth=None,
        client_cert_ids=None,
        server_timeout=None,
    ):
        """
        Initialize SSLListenerModel instance.

        :param listener_port: 监听器的监听端口
        :type listener_port: int (optional)

        :param backend_port: 后端服务器的监听端口
        :type backend_port: int (optional)

        :param scheduler: scheduler attribute
        :type scheduler: str (optional)

        :param health_check_timeout_in_second: 健康检查超时
        :type health_check_timeout_in_second: int (optional)

        :param health_check_interval: 健康检查间隔
        :type health_check_interval: int (optional)

        :param unhealthy_threshold: 不健康阈值，即连续多少次健康检查失败后，屏蔽该后端服务器
        :type unhealthy_threshold: int (optional)

        :param healthy_threshold: 健康阈值，即连续多少次健康检查成功后，重新将该后端服务器置为可用
        :type healthy_threshold: int (optional)

        :param cert_ids: 加载的SSl证书链
        :type cert_ids: List[str] (optional)

        :param encryption_type: 加密类型
        :type encryption_type: str (optional)

        :param encryption_protocols: 加密协议
        :type encryption_protocols: List[str] (optional)

        :param applied_ciphers: 加密套件
        :type applied_ciphers: str (optional)

        :param dual_auth: 是否开启双向认证，默认为关闭
        :type dual_auth: bool (optional)

        :param client_cert_ids: 当dualAuth为true时，加载的客户端证书链
        :type client_cert_ids: List[str] (optional)

        :param server_timeout: 后端服务器最大超时（单位：秒），默认900s，需为10-4000间的整数
        :type server_timeout: int (optional)
        """
        super().__init__()
        self.listener_port = listener_port
        self.backend_port = backend_port
        self.scheduler = scheduler
        self.health_check_timeout_in_second = health_check_timeout_in_second
        self.health_check_interval = health_check_interval
        self.unhealthy_threshold = unhealthy_threshold
        self.healthy_threshold = healthy_threshold
        self.cert_ids = cert_ids
        self.encryption_type = encryption_type
        self.encryption_protocols = encryption_protocols
        self.applied_ciphers = applied_ciphers
        self.dual_auth = dual_auth
        self.client_cert_ids = client_cert_ids
        self.server_timeout = server_timeout

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
        if self.listener_port is not None:
            result['listenerPort'] = self.listener_port
        if self.backend_port is not None:
            result['backendPort'] = self.backend_port
        if self.scheduler is not None:
            result['scheduler'] = self.scheduler
        if self.health_check_timeout_in_second is not None:
            result['healthCheckTimeoutInSecond'] = self.health_check_timeout_in_second
        if self.health_check_interval is not None:
            result['healthCheckInterval'] = self.health_check_interval
        if self.unhealthy_threshold is not None:
            result['unhealthyThreshold'] = self.unhealthy_threshold
        if self.healthy_threshold is not None:
            result['healthyThreshold'] = self.healthy_threshold
        if self.cert_ids is not None:
            result['certIds'] = self.cert_ids
        if self.encryption_type is not None:
            result['encryptionType'] = self.encryption_type
        if self.encryption_protocols is not None:
            result['encryptionProtocols'] = self.encryption_protocols
        if self.applied_ciphers is not None:
            result['appliedCiphers'] = self.applied_ciphers
        if self.dual_auth is not None:
            result['dualAuth'] = self.dual_auth
        if self.client_cert_ids is not None:
            result['clientCertIds'] = self.client_cert_ids
        if self.server_timeout is not None:
            result['serverTimeout'] = self.server_timeout
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SSLListenerModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('listenerPort') is not None:
            self.listener_port = m.get('listenerPort')
        if m.get('backendPort') is not None:
            self.backend_port = m.get('backendPort')
        if m.get('scheduler') is not None:
            self.scheduler = m.get('scheduler')
        if m.get('healthCheckTimeoutInSecond') is not None:
            self.health_check_timeout_in_second = m.get('healthCheckTimeoutInSecond')
        if m.get('healthCheckInterval') is not None:
            self.health_check_interval = m.get('healthCheckInterval')
        if m.get('unhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('unhealthyThreshold')
        if m.get('healthyThreshold') is not None:
            self.healthy_threshold = m.get('healthyThreshold')
        if m.get('certIds') is not None:
            self.cert_ids = m.get('certIds')
        if m.get('encryptionType') is not None:
            self.encryption_type = m.get('encryptionType')
        if m.get('encryptionProtocols') is not None:
            self.encryption_protocols = m.get('encryptionProtocols')
        if m.get('appliedCiphers') is not None:
            self.applied_ciphers = m.get('appliedCiphers')
        if m.get('dualAuth') is not None:
            self.dual_auth = m.get('dualAuth')
        if m.get('clientCertIds') is not None:
            self.client_cert_ids = m.get('clientCertIds')
        if m.get('serverTimeout') is not None:
            self.server_timeout = m.get('serverTimeout')
        return self
