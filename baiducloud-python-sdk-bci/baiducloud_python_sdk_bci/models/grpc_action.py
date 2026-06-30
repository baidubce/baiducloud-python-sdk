"""
GRPCAction information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GRPCAction(AbstractModel):
    """
    GRPCAction
    """

    def __init__(self, port=None, service=None):
        """
        Initialize GRPCAction instance.

        :param port: GRPC检测端口
        :type port: int (optional)

        :param service: GRPC检测服务
        :type service: str (optional)
        """
        super().__init__()
        self.port = port
        self.service = service

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
        if self.service is not None:
            result['service'] = self.service
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GRPCAction

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('service') is not None:
            self.service = m.get('service')
        return self
