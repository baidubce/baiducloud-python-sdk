"""
Probe information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bci.models.http_get_action import HTTPGetAction

from baiducloud_python_sdk_bci.models.tcp_socket_action import TCPSocketAction

from baiducloud_python_sdk_bci.models.exec_action import ExecAction

from baiducloud_python_sdk_bci.models.grpc_action import GRPCAction


class Probe(AbstractModel):
    """
    Probe
    """

    def __init__(
        self,
        initial_delay_seconds=None,
        timeout_seconds=None,
        period_seconds=None,
        success_threshold=None,
        failure_threshold=None,
        termination_grace_period_seconds=None,
        http_get=None,
        tcp_socket=None,
        bci_exec=None,
        grpc=None,
    ):
        """
        Initialize Probe instance.

        :param initial_delay_seconds: 检查开始执行时间，以容器启动完成为起点
        :type initial_delay_seconds: int (optional)

        :param timeout_seconds: 检查超时时间，默认1秒，最小1秒
        :type timeout_seconds: int (optional)

        :param period_seconds: 检查执行周期，默认10秒，最小1秒
        :type period_seconds: int (optional)

        :param success_threshold: 重新认定成功的阈值，默认1，当前必须为1
        :type success_threshold: int (optional)

        :param failure_threshold: 认定失败的阈值，默认3
        :type failure_threshold: int (optional)

        :param termination_grace_period_seconds: 程序缓冲时间，处理关闭前操作
        :type termination_grace_period_seconds: int (optional)

        :param http_get: http_get attribute
        :type http_get: HTTPGetAction (optional)

        :param tcp_socket: tcp_socket attribute
        :type tcp_socket: TCPSocketAction (optional)

        :param bci_exec: bci_exec attribute
        :type bci_exec: ExecAction (optional)

        :param grpc: grpc attribute
        :type grpc: GRPCAction (optional)
        """
        super().__init__()
        self.initial_delay_seconds = initial_delay_seconds
        self.timeout_seconds = timeout_seconds
        self.period_seconds = period_seconds
        self.success_threshold = success_threshold
        self.failure_threshold = failure_threshold
        self.termination_grace_period_seconds = termination_grace_period_seconds
        self.http_get = http_get
        self.tcp_socket = tcp_socket
        self.bci_exec = bci_exec
        self.grpc = grpc

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
        if self.initial_delay_seconds is not None:
            result['initialDelaySeconds'] = self.initial_delay_seconds
        if self.timeout_seconds is not None:
            result['timeoutSeconds'] = self.timeout_seconds
        if self.period_seconds is not None:
            result['periodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['successThreshold'] = self.success_threshold
        if self.failure_threshold is not None:
            result['failureThreshold'] = self.failure_threshold
        if self.termination_grace_period_seconds is not None:
            result['terminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        if self.http_get is not None:
            result['httpGet'] = self.http_get.to_dict()
        if self.tcp_socket is not None:
            result['tcpSocket'] = self.tcp_socket.to_dict()
        if self.bci_exec is not None:
            result['exec'] = self.bci_exec.to_dict()
        if self.grpc is not None:
            result['grpc'] = self.grpc.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Probe

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('initialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('initialDelaySeconds')
        if m.get('timeoutSeconds') is not None:
            self.timeout_seconds = m.get('timeoutSeconds')
        if m.get('periodSeconds') is not None:
            self.period_seconds = m.get('periodSeconds')
        if m.get('successThreshold') is not None:
            self.success_threshold = m.get('successThreshold')
        if m.get('failureThreshold') is not None:
            self.failure_threshold = m.get('failureThreshold')
        if m.get('terminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('terminationGracePeriodSeconds')
        if m.get('httpGet') is not None:
            self.http_get = HTTPGetAction().from_dict(m.get('httpGet'))
        if m.get('tcpSocket') is not None:
            self.tcp_socket = TCPSocketAction().from_dict(m.get('tcpSocket'))
        if m.get('exec') is not None:
            self.bci_exec = ExecAction().from_dict(m.get('exec'))
        if m.get('grpc') is not None:
            self.grpc = GRPCAction().from_dict(m.get('grpc'))
        return self
