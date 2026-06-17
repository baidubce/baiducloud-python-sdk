"""
Timeseries information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcm.models.dimension import Dimension

from baiducloud_python_sdk_bcm.models.data_point import DataPoint


class Timeseries(AbstractModel):
    """
    Timeseries
    """

    def __init__(self, metric_name=None, dimensions=None, data_points=None):
        """
        Initialize Timeseries instance.

        :param metric_name: 指标名
        :type metric_name: str (optional)

        :param dimensions: 维度列表，对应请求中的filters字段
        :type dimensions: List[Dimension] (optional)

        :param data_points: 指标数据点列表
        :type data_points: List[DataPoint] (optional)
        """
        super().__init__()
        self.metric_name = metric_name
        self.dimensions = dimensions
        self.data_points = data_points

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
        if self.metric_name is not None:
            result['metricName'] = self.metric_name
        if self.dimensions is not None:
            result['dimensions'] = [i.to_dict() for i in self.dimensions]
        if self.data_points is not None:
            result['dataPoints'] = [i.to_dict() for i in self.data_points]
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
        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')
        if m.get('dimensions') is not None:
            self.dimensions = [Dimension().from_dict(i) for i in m.get('dimensions')]
        if m.get('dataPoints') is not None:
            self.data_points = [DataPoint().from_dict(i) for i in m.get('dataPoints')]
        return self
