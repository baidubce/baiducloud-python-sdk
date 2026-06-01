"""
Request entity for DescribeLLMSessionsStatisticsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_apm.models.filter import Filter


class DescribeLLMSessionsStatisticsRequest(AbstractModel):
    """
    Request entity for DescribeLLMSessionsStatisticsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, begin_datetime, end_datetime, filters=None):
        """
        Initialize DescribeLLMSessionsStatisticsRequest request entity.

        :param begin_datetime: 开始时间，UTC时间
        :type begin_datetime: str (required)

        :param end_datetime: 结束时间，UTC时间
        :type end_datetime: str (required)

        :param filters: filters parameter
        :type filters: List[Filter] (optional)
        """
        super().__init__()
        self.begin_datetime = begin_datetime
        self.end_datetime = end_datetime
        self.filters = filters

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.begin_datetime is not None:
            result['beginDatetime'] = self.begin_datetime
        if self.end_datetime is not None:
            result['endDatetime'] = self.end_datetime
        if self.filters is not None:
            result['filters'] = [i.to_dict() for i in self.filters]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeLLMSessionsStatisticsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('beginDatetime') is not None:
            self.begin_datetime = m.get('beginDatetime')
        if m.get('endDatetime') is not None:
            self.end_datetime = m.get('endDatetime')
        if m.get('filters') is not None:
            self.filters = [Filter().from_dict(i) for i in m.get('filters')]
        return self
