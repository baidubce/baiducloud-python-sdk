"""
Endpoint information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Endpoint(AbstractModel):
    """
    Endpoint
    """

    def __init__(self, port=None, path=None, interval=None, matched_target_count=None):
        """
        Initialize Endpoint instance.

        :param port: 端口名称
        :type port: str (optional)

        :param path: 采集路径
        :type path: str (optional)

        :param interval: 采集间隔
        :type interval: str (optional)

        :param matched_target_count: 匹配的 target 数量
        :type matched_target_count: int (optional)
        """
        super().__init__()
        self.port = port
        self.path = path
        self.interval = interval
        self.matched_target_count = matched_target_count

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
        if self.path is not None:
            result['path'] = self.path
        if self.interval is not None:
            result['interval'] = self.interval
        if self.matched_target_count is not None:
            result['matchedTargetCount'] = self.matched_target_count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Endpoint

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('interval') is not None:
            self.interval = m.get('interval')
        if m.get('matchedTargetCount') is not None:
            self.matched_target_count = m.get('matchedTargetCount')
        return self
