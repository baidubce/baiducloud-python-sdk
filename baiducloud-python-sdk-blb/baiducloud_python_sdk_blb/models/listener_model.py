"""
ListenerModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListenerModel(AbstractModel):
    """
    ListenerModel
    """

    def __init__(self, port=None, type=None, description=None):
        """
        Initialize ListenerModel instance.

        :param port: 监听器端口
        :type port: str (optional)

        :param type: 监听器协议类型
        :type type: str (optional)

        :param description: 描述信息，长度不超过200个字符。
        :type description: str (optional)
        """
        super().__init__()
        self.port = port
        self.type = type
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
        if self.port is not None:
            result['port'] = self.port
        if self.type is not None:
            result['type'] = self.type
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
        :rtype: ListenerModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
