"""
Request entity for DescribeLLMSpansRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_apm.models.filter import Filter


class DescribeLLMSpansRequest(AbstractModel):
    """
    Request entity for DescribeLLMSpansRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        begin_datetime,
        end_datetime,
        parse_llm_input_output=None,
        filters=None,
        order_by=None,
        order=None,
        marker=None,
    ):
        """
        Initialize DescribeLLMSpansRequest request entity.

        :param begin_datetime: 开始时间，UTC时间
        :type begin_datetime: str (required)

        :param end_datetime: 结束时间，UTC时间
        :type end_datetime: str (required)

        :param parse_llm_input_output: 是否填充gen_ai.input和gen_ai.output字段，默认false
        :type parse_llm_input_output: bool (optional)

        :param filters: filters parameter
        :type filters: List[Filter] (optional)

        :param order_by: 排序字段，默认值：startTime，可选项：startTime(开始时间)
        :type order_by: str (optional)

        :param order: 排序方向，可选值：asc(升序)、desc(降序)
        :type order: str (optional)

        :param marker: 翻页游标。请求第一页时填空，请求后续页时使用上一页返回的nextMarker值
        :type marker: str (optional)
        """
        super().__init__()
        self.begin_datetime = begin_datetime
        self.end_datetime = end_datetime
        self.parse_llm_input_output = parse_llm_input_output
        self.filters = filters
        self.order_by = order_by
        self.order = order
        self.marker = marker

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
        if self.parse_llm_input_output is not None:
            result['parseLLMInputOutput'] = self.parse_llm_input_output
        if self.filters is not None:
            result['filters'] = [i.to_dict() for i in self.filters]
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.order is not None:
            result['order'] = self.order
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeLLMSpansRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('beginDatetime') is not None:
            self.begin_datetime = m.get('beginDatetime')
        if m.get('endDatetime') is not None:
            self.end_datetime = m.get('endDatetime')
        if m.get('parseLLMInputOutput') is not None:
            self.parse_llm_input_output = m.get('parseLLMInputOutput')
        if m.get('filters') is not None:
            self.filters = [Filter().from_dict(i) for i in m.get('filters')]
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self
