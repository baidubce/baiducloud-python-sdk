"""
SCSSlowlogStatsDuartion information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SCSSlowlogStatsDuartion(AbstractModel):
    """
    SCSSlowlogStatsDuartion
    """

    def __init__(self, start=None, end=None, title=None, count=None):
        """
        Initialize SCSSlowlogStatsDuartion instance.

        :param start: 耗时起点 单位ms
        :type start: int (optional)

        :param end: 耗时终点 单位ms
        :type end: int (optional)

        :param title: 耗时区间 例如 (10，20] ms
        :type title: str (optional)

        :param count: 分布在当前耗时区间的数量
        :type count: int (optional)
        """
        super().__init__()
        self.start = start
        self.end = end
        self.title = title
        self.count = count

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
        if self.start is not None:
            result['start'] = self.start
        if self.end is not None:
            result['end'] = self.end
        if self.title is not None:
            result['title'] = self.title
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SCSSlowlogStatsDuartion

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self
