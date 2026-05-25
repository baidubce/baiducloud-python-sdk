"""
AppTCPListenerModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AppTCPListenerModel(AbstractModel):
    """
    AppTCPListenerModel
    """

    def __init__(self, listener_port=None, scheduler=None, tcp_session_timeout=None, description=None):
        """
        Initialize AppTCPListenerModel instance.

        :param listener_port: 监听器的监听端口
        :type listener_port: int (optional)

        :param scheduler: scheduler attribute
        :type scheduler: str (optional)

        :param tcp_session_timeout: tcp设置连接超时时间（单位：秒），默认为900，需为10-4000间的整数
        :type tcp_session_timeout: int (optional)

        :param description: 描述信息，长度不超过200个字符。
        :type description: str (optional)
        """
        super().__init__()
        self.listener_port = listener_port
        self.scheduler = scheduler
        self.tcp_session_timeout = tcp_session_timeout
        self.description = description

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
        if self.scheduler is not None:
            result['scheduler'] = self.scheduler
        if self.tcp_session_timeout is not None:
            result['tcpSessionTimeout'] = self.tcp_session_timeout
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AppTCPListenerModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('listenerPort') is not None:
            self.listener_port = m.get('listenerPort')
        if m.get('scheduler') is not None:
            self.scheduler = m.get('scheduler')
        if m.get('tcpSessionTimeout') is not None:
            self.tcp_session_timeout = m.get('tcpSessionTimeout')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
