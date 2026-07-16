"""
Request entity for UpdateBlbHttpsListenerRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_blb.models.additional_attributes_model import AdditionalAttributesModel
from baiducloud_python_sdk_blb.models.additional_cert_domain import AdditionalCertDomain


class UpdateBlbHttpsListenerRequest(AbstractModel):
    """
    Request entity for UpdateBlbHttpsListenerRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        blb_id,
        listener_port,
        client_token=None,
        backend_port=None,
        scheduler=None,
        keep_session=None,
        keep_session_type=None,
        keep_session_duration=None,
        keep_session_cookie_name=None,
        x_forward_for=None,
        x_forwarded_proto=None,
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
        encryption_type=None,
        encryption_protocols=None,
        applied_ciphers=None,
    ):
        """
        Initialize UpdateBlbHttpsListenerRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param listener_port: listener_port parameter
        :type listener_port: int (required)

        :param backend_port: 后端服务器的监听端口，需为1-65535间的整数
        :type backend_port: int (optional)

        :param scheduler: scheduler parameter
        :type scheduler: str (optional)

        :param keep_session: 是否开启会话保持功能，即同一个Client发出的请求都会到达同一个后端服务器，默认关闭
        :type keep_session: bool (optional)

        :param keep_session_type: keep_session_type parameter
        :type keep_session_type: str (optional)

        :param keep_session_duration: 会话保持的cookie有效时间（单位：秒），当且仅当开启会话保持时有效，默认3600s，需为1-15552000间的整数
        :type keep_session_duration: int (optional)

        :param keep_session_cookie_name: 会话保持需要覆盖的cookie名称，当且仅当开启会话保持且keepSessionType=\"rewrite\"时有效
        :type keep_session_cookie_name: str (optional)

        :param x_forward_for: x_forward_for parameter
        :type x_forward_for: bool (optional)

        :param x_forwarded_proto: 将监听使用的协议通过x-forwarded-proto HTTP Header 转发给后端服务器
        :type x_forwarded_proto: bool (optional)

        :param additional_attributes: additional_attributes parameter
        :type additional_attributes: AdditionalAttributesModel (optional)

        :param health_check_type: 健康检查协议，支持\"HTTP\"/\"TCP\"
        :type health_check_type: str (optional)

        :param health_check_port: 健康检查端口，默认为backendPort
        :type health_check_port: int (optional)

        :param health_check_uri: 健康检查URI，默认/。当健康检查协议为\"HTTP\"时生效
        :type health_check_uri: str (optional)

        :param health_check_timeout_in_second: 健康检查超时（单位：秒），默认为3，需为1-60间的整数
        :type health_check_timeout_in_second: int (optional)

        :param health_check_interval: 健康检查间隔（单位：秒），默认为3，需为1-10间的整数
        :type health_check_interval: int (optional)

        :param unhealthy_threshold: 不健康阈值，即连续多少次健康检查失败后，屏蔽该后端服务器。默认为3，需为2-5间的整数
        :type unhealthy_threshold: int (optional)

        :param healthy_threshold: 健康阈值，即连续多少次健康检查成功后，重新将该后端服务器置为可用。默认为3，需为2-5间的整数
        :type healthy_threshold: int (optional)

        :param health_check_normal_status: health_check_normal_status parameter
        :type health_check_normal_status: str (optional)

        :param health_check_host: health_check_host parameter
        :type health_check_host: str (optional)

        :param server_timeout: 后端服务器最大超时（单位：秒），默认30s，需为1-3600间的整数
        :type server_timeout: int (optional)

        :param cert_ids: 监听器要加载的证书链,当前仅允许传入1个证书ID，如果传入多个，则只有最后一个生效
        :type cert_ids: List[str] (optional)

        :param additional_cert_domains: 扩展域名
        :type additional_cert_domains: List[AdditionalCertDomain] (optional)

        :param encryption_type: encryption_type parameter
        :type encryption_type: str (optional)

        :param encryption_protocols: encryption_protocols parameter
        :type encryption_protocols: List[str] (optional)

        :param applied_ciphers: applied_ciphers parameter
        :type applied_ciphers: str (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.client_token = client_token
        self.listener_port = listener_port
        self.backend_port = backend_port
        self.scheduler = scheduler
        self.keep_session = keep_session
        self.keep_session_type = keep_session_type
        self.keep_session_duration = keep_session_duration
        self.keep_session_cookie_name = keep_session_cookie_name
        self.x_forward_for = x_forward_for
        self.x_forwarded_proto = x_forwarded_proto
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
        self.encryption_type = encryption_type
        self.encryption_protocols = encryption_protocols
        self.applied_ciphers = applied_ciphers

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
        if self.x_forwarded_proto is not None:
            result['xForwardedProto'] = self.x_forwarded_proto
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
        if self.encryption_type is not None:
            result['encryptionType'] = self.encryption_type
        if self.encryption_protocols is not None:
            result['encryptionProtocols'] = self.encryption_protocols
        if self.applied_ciphers is not None:
            result['appliedCiphers'] = self.applied_ciphers
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateBlbHttpsListenerRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
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
        if m.get('xForwardedProto') is not None:
            self.x_forwarded_proto = m.get('xForwardedProto')
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
        if m.get('encryptionType') is not None:
            self.encryption_type = m.get('encryptionType')
        if m.get('encryptionProtocols') is not None:
            self.encryption_protocols = m.get('encryptionProtocols')
        if m.get('appliedCiphers') is not None:
            self.applied_ciphers = m.get('appliedCiphers')
        return self
