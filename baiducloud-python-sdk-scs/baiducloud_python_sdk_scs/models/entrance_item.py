"""
EntranceItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class EntranceItem(AbstractModel):
    """
    EntranceItem
    """

    def __init__(self, ip=None, port=None, zone=None):
        """
        Initialize EntranceItem instance.

        :param ip: 入口IP
        :type ip: str (optional)

        :param port: 端口
        :type port: int (optional)

        :param zone: 可用区
        :type zone: str (optional)
        """
        super().__init__()
        self.ip = ip
        self.port = port
        self.zone = zone

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
        if self.zone is not None:
            result['zone'] = self.zone
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EntranceItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        return self
