"""
Request entity for CreateBlbTcpListenerRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateBlbTcpListenerRequest(AbstractModel):
    """
    Request entity for CreateBlbTcpListenerRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        blb_id,
        listener_port,
        backend_port,
        scheduler,
        tcp_session_timeout=None,
        health_check_type=None,
        health_check_timeout_in_second=None,
        health_check_interval=None,
        unhealthy_threshold=None,
        healthy_threshold=None,
    ):
        """
        Initialize CreateBlbTcpListenerRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param listener_port: 监听器的监听端口，需为1-65535间的整数
        :type listener_port: int (required)

        :param backend_port: 后端服务器的监听端口，需为1-65535间的整数
        :type backend_port: int (required)

        :param scheduler: scheduler parameter
        :type scheduler: str (required)

        :param tcp_session_timeout: tcp设置连接超时时间（单位：秒），默认900，需为10-4000间的整数
        :type tcp_session_timeout: int (optional)

        :param health_check_type: 健康检查协议类型，默认\"TCP\"
        :type health_check_type: str (optional)

        :param health_check_timeout_in_second: 健康检查超时（单位：秒），默认为3，需为1-60间的整数
        :type health_check_timeout_in_second: int (optional)

        :param health_check_interval: 健康检查间隔（单位：秒），默认为3，需为1-10间的整数
        :type health_check_interval: int (optional)

        :param unhealthy_threshold: 不健康阈值，即连续多少次健康检查失败后，屏蔽该后端服务器。默认为3，需为2-5间的整数
        :type unhealthy_threshold: int (optional)

        :param healthy_threshold: 健康阈值，即连续多少次健康检查成功后，重新将该后端服务器置为可用。默认为3，需为2-5间的整数
        :type healthy_threshold: int (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.listener_port = listener_port
        self.backend_port = backend_port
        self.scheduler = scheduler
        self.tcp_session_timeout = tcp_session_timeout
        self.health_check_type = health_check_type
        self.health_check_timeout_in_second = health_check_timeout_in_second
        self.health_check_interval = health_check_interval
        self.unhealthy_threshold = unhealthy_threshold
        self.healthy_threshold = healthy_threshold

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
        if self.listener_port is not None:
            result['listenerPort'] = self.listener_port
        if self.backend_port is not None:
            result['backendPort'] = self.backend_port
        if self.scheduler is not None:
            result['scheduler'] = self.scheduler
        if self.tcp_session_timeout is not None:
            result['tcpSessionTimeout'] = self.tcp_session_timeout
        if self.health_check_type is not None:
            result['healthCheckType'] = self.health_check_type
        if self.health_check_timeout_in_second is not None:
            result['healthCheckTimeoutInSecond'] = self.health_check_timeout_in_second
        if self.health_check_interval is not None:
            result['healthCheckInterval'] = self.health_check_interval
        if self.unhealthy_threshold is not None:
            result['unhealthyThreshold'] = self.unhealthy_threshold
        if self.healthy_threshold is not None:
            result['healthyThreshold'] = self.healthy_threshold
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateBlbTcpListenerRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('listenerPort') is not None:
            self.listener_port = m.get('listenerPort')
        if m.get('backendPort') is not None:
            self.backend_port = m.get('backendPort')
        if m.get('scheduler') is not None:
            self.scheduler = m.get('scheduler')
        if m.get('tcpSessionTimeout') is not None:
            self.tcp_session_timeout = m.get('tcpSessionTimeout')
        if m.get('healthCheckType') is not None:
            self.health_check_type = m.get('healthCheckType')
        if m.get('healthCheckTimeoutInSecond') is not None:
            self.health_check_timeout_in_second = m.get('healthCheckTimeoutInSecond')
        if m.get('healthCheckInterval') is not None:
            self.health_check_interval = m.get('healthCheckInterval')
        if m.get('unhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('unhealthyThreshold')
        if m.get('healthyThreshold') is not None:
            self.healthy_threshold = m.get('healthyThreshold')
        return self
