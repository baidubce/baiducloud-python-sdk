"""
UDPListenerModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UDPListenerModel(AbstractModel):
    """
    UDPListenerModel
    """

    def __init__(
        self,
        listener_port=None,
        backend_port=None,
        scheduler=None,
        health_check_type=None,
        health_check_port=None,
        health_check_timeout_in_second=None,
        health_check_interval=None,
        unhealthy_threshold=None,
        healthy_threshold=None,
        health_check_string=None,
        udp_session_timeout=None,
    ):
        """
        Initialize UDPListenerModel instance.

        :param listener_port: 监听器的监听端口
        :type listener_port: int (optional)

        :param backend_port: 后端服务器的监听端口
        :type backend_port: int (optional)

        :param scheduler: scheduler attribute
        :type scheduler: str (optional)

        :param health_check_type: 健康检查协议，值为\"UDP\"/\"ICMP\"
        :type health_check_type: str (optional)

        :param health_check_port: 健康检查端口，当健康检查协议为\"UDP\"时可使用
        :type health_check_port: int (optional)

        :param health_check_timeout_in_second: 健康检查超时
        :type health_check_timeout_in_second: int (optional)

        :param health_check_interval: 健康检查间隔
        :type health_check_interval: int (optional)

        :param unhealthy_threshold: 不健康阈值，即连续多少次健康检查失败后，屏蔽该后端服务器
        :type unhealthy_threshold: int (optional)

        :param healthy_threshold: 健康阈值，即连续多少次健康检查成功后，重新将该后端服务器置为可用
        :type healthy_threshold: int (optional)

        :param health_check_string: 健康发送的请求字符串，后端服务器收到后需要进行应答，支持标准转义如\\\\00、\\\\xf2，方便配置二进制格式请求
        :type health_check_string: str (optional)

        :param udp_session_timeout: udp会话超时时间。默认为90，需为5-4000间的整数，单位秒
        :type udp_session_timeout: int (optional)
        """
        super().__init__()
        self.listener_port = listener_port
        self.backend_port = backend_port
        self.scheduler = scheduler
        self.health_check_type = health_check_type
        self.health_check_port = health_check_port
        self.health_check_timeout_in_second = health_check_timeout_in_second
        self.health_check_interval = health_check_interval
        self.unhealthy_threshold = unhealthy_threshold
        self.healthy_threshold = healthy_threshold
        self.health_check_string = health_check_string
        self.udp_session_timeout = udp_session_timeout

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
        if self.health_check_type is not None:
            result['healthCheckType'] = self.health_check_type
        if self.health_check_port is not None:
            result['healthCheckPort'] = self.health_check_port
        if self.health_check_timeout_in_second is not None:
            result['healthCheckTimeoutInSecond'] = self.health_check_timeout_in_second
        if self.health_check_interval is not None:
            result['healthCheckInterval'] = self.health_check_interval
        if self.unhealthy_threshold is not None:
            result['unhealthyThreshold'] = self.unhealthy_threshold
        if self.healthy_threshold is not None:
            result['healthyThreshold'] = self.healthy_threshold
        if self.health_check_string is not None:
            result['healthCheckString'] = self.health_check_string
        if self.udp_session_timeout is not None:
            result['udpSessionTimeout'] = self.udp_session_timeout
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UDPListenerModel

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
        if m.get('healthCheckType') is not None:
            self.health_check_type = m.get('healthCheckType')
        if m.get('healthCheckPort') is not None:
            self.health_check_port = m.get('healthCheckPort')
        if m.get('healthCheckTimeoutInSecond') is not None:
            self.health_check_timeout_in_second = m.get('healthCheckTimeoutInSecond')
        if m.get('healthCheckInterval') is not None:
            self.health_check_interval = m.get('healthCheckInterval')
        if m.get('unhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('unhealthyThreshold')
        if m.get('healthyThreshold') is not None:
            self.healthy_threshold = m.get('healthyThreshold')
        if m.get('healthCheckString') is not None:
            self.health_check_string = m.get('healthCheckString')
        if m.get('udpSessionTimeout') is not None:
            self.udp_session_timeout = m.get('udpSessionTimeout')
        return self
