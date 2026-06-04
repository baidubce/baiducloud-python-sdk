"""
DnsServerConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DnsServerConfig(AbstractModel):
    """
    DnsServerConfig
    """

    def __init__(self, ip=None, port=None):
        """
        Initialize DnsServerConfig instance.

        :param ip: 转发目标 IP 地址
        :type ip: str (optional)

        :param port: 转发目标 IP 地址的端口号
        :type port: int (optional)
        """
        super().__init__()
        self.ip = ip
        self.port = port

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
        if self.ip is not None:
            result['ip'] = self.ip
        if self.port is not None:
            result['port'] = self.port
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DnsServerConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('port') is not None:
            self.port = m.get('port')
        return self
