"""
Timeseries information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_apm.models.dimension import Dimension


class Timeseries(AbstractModel):
    """
    Timeseries
    """

    def __init__(self, metric=None, dimensions=None, data=None, compare_to=None):
        """
        Initialize Timeseries instance.

        :param metric: 指标名
        :type metric: str (optional)

        :param dimensions: 维度列表，对应请求中的groupBy字段
        :type dimensions: List[Dimension] (optional)

        :param data: 指标值序列，每个元素为 [时间戳（秒）, 指标值]
        :type data: List[List[float]] (optional)

        :param compare_to: 同比数据，每组同比为三元组列表 [时间戳, 值, 同比率]
        :type compare_to: List[List[List[float]]] (optional)
        """
        super().__init__()
        self.metric = metric
        self.dimensions = dimensions
        self.data = data
        self.compare_to = compare_to

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
        if self.metric is not None:
            result['metric'] = self.metric
        if self.dimensions is not None:
            result['dimensions'] = [i.to_dict() for i in self.dimensions]
        if self.data is not None:
            result['data'] = self.data
        if self.compare_to is not None:
            result['compareTo'] = self.compare_to
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Timeseries

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('metric') is not None:
            self.metric = m.get('metric')
        if m.get('dimensions') is not None:
            self.dimensions = [Dimension().from_dict(i) for i in m.get('dimensions')]
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('compareTo') is not None:
            self.compare_to = m.get('compareTo')
        return self
