"""
HTTPSListenerModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_blb.models.additional_attributes_model import AdditionalAttributesModel

from baiducloud_python_sdk_blb.models.additional_cert_domain import AdditionalCertDomain


class HTTPSListenerModel(AbstractModel):
    """
    HTTPSListenerModel
    """

    def __init__(
        self,
        listener_port=None,
        backend_port=None,
        scheduler=None,
        keep_session=None,
        keep_session_type=None,
        keep_session_duration=None,
        keep_session_cookie_name=None,
        x_forward_for=None,
        additional_attributes=None,
        health_check_type=None,
        health_check_port=None,
        health_check_uri=None,
        health_check_timeout_in_second=None,
        health_check_interval=None,
        unhealthy_threshold=None,
        healthy_threshold=None,
        health_check_normal_status=None,
        health_check_host=None,
        server_timeout=None,
        cert_ids=None,
        additional_cert_domains=None,
        dual_auth=None,
        client_cert_ids=None,
        encryption_type=None,
        encryption_protocols=None,
        applied_ciphers=None,
    ):
        """
        Initialize HTTPSListenerModel instance.

        :param listener_port: 监听器的监听端口
        :type listener_port: int (optional)

        :param backend_port: 后端服务器的监听端口
        :type backend_port: int (optional)

        :param scheduler: 负载均衡算法，值为\"RoundRobin\"/\"LeastConnection\"
        :type scheduler: str (optional)

        :param keep_session: 是否开启会话保持功能，即同一个Client发出的请求都会到达同一个后端服务器
        :type keep_session: bool (optional)

        :param keep_session_type: 会话保持的cookie处理方式，当且仅当开启会话保持时有效，值为\"insert\"/\"rewrite\"
        :type keep_session_type: str (optional)

        :param keep_session_duration: 会话保持的cookie有效时间（单位：秒），当且仅当开启会话保持时有效
        :type keep_session_duration: int (optional)

        :param keep_session_cookie_name: 会话保持需要覆盖的cookie名称，当且仅当开启会话保持且keepSessionType=\"rewrite\"时有效
        :type keep_session_cookie_name: str (optional)

        :param x_forward_for: x_forward_for attribute
        :type x_forward_for: bool (optional)

        :param additional_attributes: additional_attributes attribute
        :type additional_attributes: AdditionalAttributesModel (optional)

        :param health_check_type: 健康检查协议，值为\"HTTP\"/\"TCP\"
        :type health_check_type: str (optional)

        :param health_check_port: 健康检查端口
        :type health_check_port: int (optional)

        :param health_check_uri: 健康检查URI
        :type health_check_uri: str (optional)

        :param health_check_timeout_in_second: 健康检查超时
        :type health_check_timeout_in_second: int (optional)

        :param health_check_interval: 健康检查间隔
        :type health_check_interval: int (optional)

        :param unhealthy_threshold: 不健康阈值，即连续多少次健康检查失败后，屏蔽该后端服务器
        :type unhealthy_threshold: int (optional)

        :param healthy_threshold: 健康阈值，即连续多少次健康检查成功后，重新将该后端服务器置为可用
        :type healthy_threshold: int (optional)

        :param health_check_normal_status: 健康检查正常时的HTTP状态码，支持5类状态码的组合，格式为http_1xx 或 http_2xx
        :type health_check_normal_status: str (optional)

        :param health_check_host: health_check_host attribute
        :type health_check_host: str (optional)

        :param server_timeout: 后端服务器最大超时（单位：秒）
        :type server_timeout: int (optional)

        :param cert_ids: 加载的SSl证书，目前HTTPS监听器只能绑定一个SSL证书
        :type cert_ids: List[str] (optional)

        :param additional_cert_domains: 扩展域名
        :type additional_cert_domains: List[AdditionalCertDomain] (optional)

        :param dual_auth: 是否开启双向认证，默认为关闭
        :type dual_auth: bool (optional)

        :param client_cert_ids: 当dualAuth为true时，加载的客户端证书链
        :type client_cert_ids: List[str] (optional)

        :param encryption_type: 加密类型
        :type encryption_type: str (optional)

        :param encryption_protocols: 加密协议
        :type encryption_protocols: List[str] (optional)

        :param applied_ciphers: 加密套件
        :type applied_ciphers: str (optional)
        """
        super().__init__()
        self.listener_port = listener_port
        self.backend_port = backend_port
        self.scheduler = scheduler
        self.keep_session = keep_session
        self.keep_session_type = keep_session_type
        self.keep_session_duration = keep_session_duration
        self.keep_session_cookie_name = keep_session_cookie_name
        self.x_forward_for = x_forward_for
        self.additional_attributes = additional_attributes
        self.health_check_type = health_check_type
        self.health_check_port = health_check_port
        self.health_check_uri = health_check_uri
        self.health_check_timeout_in_second = health_check_timeout_in_second
        self.health_check_interval = health_check_interval
        self.unhealthy_threshold = unhealthy_threshold
        self.healthy_threshold = healthy_threshold
        self.health_check_normal_status = health_check_normal_status
        self.health_check_host = health_check_host
        self.server_timeout = server_timeout
        self.cert_ids = cert_ids
        self.additional_cert_domains = additional_cert_domains
        self.dual_auth = dual_auth
        self.client_cert_ids = client_cert_ids
        self.encryption_type = encryption_type
        self.encryption_protocols = encryption_protocols
        self.applied_ciphers = applied_ciphers

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
        if self.keep_session is not None:
            result['keepSession'] = self.keep_session
        if self.keep_session_type is not None:
            result['keepSessionType'] = self.keep_session_type
        if self.keep_session_duration is not None:
            result['keepSessionDuration'] = self.keep_session_duration
        if self.keep_session_cookie_name is not None:
            result['keepSessionCookieName'] = self.keep_session_cookie_name
        if self.x_forward_for is not None:
            result['xForwardFor'] = self.x_forward_for
        if self.additional_attributes is not None:
            result['additionalAttributes'] = self.additional_attributes.to_dict()
        if self.health_check_type is not None:
            result['healthCheckType'] = self.health_check_type
        if self.health_check_port is not None:
            result['healthCheckPort'] = self.health_check_port
        if self.health_check_uri is not None:
            result['healthCheckURI'] = self.health_check_uri
        if self.health_check_timeout_in_second is not None:
            result['healthCheckTimeoutInSecond'] = self.health_check_timeout_in_second
        if self.health_check_interval is not None:
            result['healthCheckInterval'] = self.health_check_interval
        if self.unhealthy_threshold is not None:
            result['unhealthyThreshold'] = self.unhealthy_threshold
        if self.healthy_threshold is not None:
            result['healthyThreshold'] = self.healthy_threshold
        if self.health_check_normal_status is not None:
            result['healthCheckNormalStatus'] = self.health_check_normal_status
        if self.health_check_host is not None:
            result['healthCheckHost'] = self.health_check_host
        if self.server_timeout is not None:
            result['serverTimeout'] = self.server_timeout
        if self.cert_ids is not None:
            result['certIds'] = self.cert_ids
        if self.additional_cert_domains is not None:
            result['additionalCertDomains'] = [i.to_dict() for i in self.additional_cert_domains]
        if self.dual_auth is not None:
            result['dualAuth'] = self.dual_auth
        if self.client_cert_ids is not None:
            result['clientCertIds'] = self.client_cert_ids
        if self.encryption_type is not None:
            result['encryptionType'] = self.encryption_type
        if self.encryption_protocols is not None:
            result['encryptionProtocols'] = self.encryption_protocols
        if self.applied_ciphers is not None:
            result['appliedCiphers'] = self.applied_ciphers
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HTTPSListenerModel

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
        if m.get('keepSession') is not None:
            self.keep_session = m.get('keepSession')
        if m.get('keepSessionType') is not None:
            self.keep_session_type = m.get('keepSessionType')
        if m.get('keepSessionDuration') is not None:
            self.keep_session_duration = m.get('keepSessionDuration')
        if m.get('keepSessionCookieName') is not None:
            self.keep_session_cookie_name = m.get('keepSessionCookieName')
        if m.get('xForwardFor') is not None:
            self.x_forward_for = m.get('xForwardFor')
        if m.get('additionalAttributes') is not None:
            self.additional_attributes = AdditionalAttributesModel().from_dict(m.get('additionalAttributes'))
        if m.get('healthCheckType') is not None:
            self.health_check_type = m.get('healthCheckType')
        if m.get('healthCheckPort') is not None:
            self.health_check_port = m.get('healthCheckPort')
        if m.get('healthCheckURI') is not None:
            self.health_check_uri = m.get('healthCheckURI')
        if m.get('healthCheckTimeoutInSecond') is not None:
            self.health_check_timeout_in_second = m.get('healthCheckTimeoutInSecond')
        if m.get('healthCheckInterval') is not None:
            self.health_check_interval = m.get('healthCheckInterval')
        if m.get('unhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('unhealthyThreshold')
        if m.get('healthyThreshold') is not None:
            self.healthy_threshold = m.get('healthyThreshold')
        if m.get('healthCheckNormalStatus') is not None:
            self.health_check_normal_status = m.get('healthCheckNormalStatus')
        if m.get('healthCheckHost') is not None:
            self.health_check_host = m.get('healthCheckHost')
        if m.get('serverTimeout') is not None:
            self.server_timeout = m.get('serverTimeout')
        if m.get('certIds') is not None:
            self.cert_ids = m.get('certIds')
        if m.get('additionalCertDomains') is not None:
            self.additional_cert_domains = [
                AdditionalCertDomain().from_dict(i) for i in m.get('additionalCertDomains')
            ]
        if m.get('dualAuth') is not None:
            self.dual_auth = m.get('dualAuth')
        if m.get('clientCertIds') is not None:
            self.client_cert_ids = m.get('clientCertIds')
        if m.get('encryptionType') is not None:
            self.encryption_type = m.get('encryptionType')
        if m.get('encryptionProtocols') is not None:
            self.encryption_protocols = m.get('encryptionProtocols')
        if m.get('appliedCiphers') is not None:
            self.applied_ciphers = m.get('appliedCiphers')
        return self
