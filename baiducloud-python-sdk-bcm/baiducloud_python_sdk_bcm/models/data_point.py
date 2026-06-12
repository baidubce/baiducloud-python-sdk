"""
DataPoint information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DataPoint(AbstractModel):
    """
    DataPoint
    """

    def __init__(self, timestmap=None, avg=None, max=None, min=None, sum=None, count=None):
        """
        Initialize DataPoint instance.

        :param timestmap: 时间戳，单位：毫秒
        :type timestmap: int (optional)

        :param avg: 若aggregationOverTime包含avg，返回平均值
        :type avg: float (optional)

        :param max: 若aggregationOverTime包含max，返回最大值
        :type max: float (optional)

        :param min: 若aggregationOverTime包含min，返回最小值
        :type min: float (optional)

        :param sum: 若aggregationOverTime包含sum，返回和值
        :type sum: float (optional)

        :param count: 若aggregationOverTime包含count，返回数量
        :type count: int (optional)
        """
        super().__init__()
        self.timestmap = timestmap
        self.avg = avg
        self.max = max
        self.min = min
        self.sum = sum
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
        if self.timestmap is not None:
            result['timestmap'] = self.timestmap
        if self.avg is not None:
            result['avg'] = self.avg
        if self.max is not None:
            result['max'] = self.max
        if self.min is not None:
            result['min'] = self.min
        if self.sum is not None:
            result['sum'] = self.sum
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
        :rtype: DataPoint

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('timestmap') is not None:
            self.timestmap = m.get('timestmap')
        if m.get('avg') is not None:
            self.avg = m.get('avg')
        if m.get('max') is not None:
            self.max = m.get('max')
        if m.get('min') is not None:
            self.min = m.get('min')
        if m.get('sum') is not None:
            self.sum = m.get('sum')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self
