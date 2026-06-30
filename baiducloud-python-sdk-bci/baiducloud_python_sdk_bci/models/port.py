"""
Port information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Port(AbstractModel):
    """
    Port
    """

    def __init__(self, name=None, port=None, protocol=None):
        """
        Initialize Port instance.

        :param name: 端口名
        :type name: str (optional)

        :param port: 端口号
        :type port: int (optional)

        :param protocol: 协议类型：TCP、UDP
        :type protocol: str (optional)
        """
        super().__init__()
        self.name = name
        self.port = port
        self.protocol = protocol

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
        if self.name is not None:
            result['name'] = self.name
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Port

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self
