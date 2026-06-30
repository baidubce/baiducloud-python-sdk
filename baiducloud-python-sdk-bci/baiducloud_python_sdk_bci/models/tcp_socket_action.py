"""
TCPSocketAction information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TCPSocketAction(AbstractModel):
    """
    TCPSocketAction
    """

    def __init__(self, port=None, host=None):
        """
        Initialize TCPSocketAction instance.

        :param port: TCP Socket检测端口
        :type port: int (optional)

        :param host: TCP Socket检测host
        :type host: str (optional)
        """
        super().__init__()
        self.port = port
        self.host = host

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
        if self.port is not None:
            result['port'] = self.port
        if self.host is not None:
            result['host'] = self.host
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TCPSocketAction

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('host') is not None:
            self.host = m.get('host')
        return self
