"""
TrendResultBase information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_dbsc.models.trend_result_series import TrendResultSeries


class TrendResultBase(AbstractModel):
    """
    TrendResultBase
    """

    def __init__(self, category=None, series=None):
        """
        Initialize TrendResultBase instance.

        :param category: 时间列表
        :type category: List[str] (optional)

        :param series: 各个指标的数据列表
        :type series: List[TrendResultSeries] (optional)
        """
        super().__init__()
        self.category = category
        self.series = series

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
        if self.category is not None:
            result['category'] = self.category
        if self.series is not None:
            result['series'] = [i.to_dict() for i in self.series]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TrendResultBase

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('series') is not None:
            self.series = [TrendResultSeries().from_dict(i) for i in m.get('series')]
        return self
