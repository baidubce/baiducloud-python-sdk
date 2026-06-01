"""
Request entity for DescribeLLMTraceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_apm.models.filter import Filter


class DescribeLLMTraceRequest(AbstractModel):
    """
    Request entity for DescribeLLMTraceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, begin_datetime, end_datetime, trace_id, filters=None, return_height=None):
        """
        Initialize DescribeLLMTraceRequest request entity.

        :param begin_datetime: 开始时间，UTC时间
        :type begin_datetime: str (required)

        :param end_datetime: 结束时间，UTC时间
        :type end_datetime: str (required)

        :param trace_id: TraceID
        :type trace_id: str (required)

        :param filters: 过滤项列表
        :type filters: List[Filter] (optional)

        :param return_height: 是否返回span在瀑布图中的高度，默认值：false
        :type return_height: bool (optional)
        """
        super().__init__()
        self.begin_datetime = begin_datetime
        self.end_datetime = end_datetime
        self.trace_id = trace_id
        self.filters = filters
        self.return_height = return_height

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
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        if self.filters is not None:
            result['filters'] = [i.to_dict() for i in self.filters]
        if self.return_height is not None:
            result['returnHeight'] = self.return_height
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeLLMTraceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('beginDatetime') is not None:
            self.begin_datetime = m.get('beginDatetime')
        if m.get('endDatetime') is not None:
            self.end_datetime = m.get('endDatetime')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('filters') is not None:
            self.filters = [Filter().from_dict(i) for i in m.get('filters')]
        if m.get('returnHeight') is not None:
            self.return_height = m.get('returnHeight')
        return self
