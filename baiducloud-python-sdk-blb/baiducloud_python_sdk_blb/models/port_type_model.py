"""
PortTypeModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PortTypeModel(AbstractModel):
    """
    PortTypeModel
    """

    def __init__(self, port=None, type=None):
        """
        Initialize PortTypeModel instance.

        :param port: 监听端口
        :type port: int (optional)

        :param type: 监听端口的协议
        :type type: str (optional)
        """
        super().__init__()
        self.port = port
        self.type = type

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
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PortTypeModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self
