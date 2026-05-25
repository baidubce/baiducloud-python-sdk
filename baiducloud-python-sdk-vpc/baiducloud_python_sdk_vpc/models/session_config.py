"""
SessionConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SessionConfig(AbstractModel):
    """
    SessionConfig
    """

    def __init__(self, tcp_timeout=None, udp_timeout=None, icmp_timeout=None):
        """
        Initialize SessionConfig instance.

        :param tcp_timeout: tcp超时时间
        :type tcp_timeout: int (optional)

        :param udp_timeout: udp超时时间
        :type udp_timeout: int (optional)

        :param icmp_timeout: icmp超时时间
        :type icmp_timeout: int (optional)
        """
        super().__init__()
        self.tcp_timeout = tcp_timeout
        self.udp_timeout = udp_timeout
        self.icmp_timeout = icmp_timeout

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
        if self.tcp_timeout is not None:
            result['tcpTimeout'] = self.tcp_timeout
        if self.udp_timeout is not None:
            result['udpTimeout'] = self.udp_timeout
        if self.icmp_timeout is not None:
            result['icmpTimeout'] = self.icmp_timeout
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SessionConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('tcpTimeout') is not None:
            self.tcp_timeout = m.get('tcpTimeout')
        if m.get('udpTimeout') is not None:
            self.udp_timeout = m.get('udpTimeout')
        if m.get('icmpTimeout') is not None:
            self.icmp_timeout = m.get('icmpTimeout')
        return self
