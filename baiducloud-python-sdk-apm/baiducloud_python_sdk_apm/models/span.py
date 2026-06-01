"""
Span information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_apm.models.span_event import SpanEvent


class Span(AbstractModel):
    """
    Span
    """

    def __init__(
        self,
        trace_id=None,
        span_id=None,
        parent_span_id=None,
        name=None,
        service=None,
        start=None,
        end=None,
        duration=None,
        host=None,
        status_code=None,
        kind=None,
        attributes=None,
        resource=None,
        events=None,
        height=None,
        sub_spans=None,
    ):
        """
        Initialize Span instance.

        :param trace_id: Trace ID
        :type trace_id: str (optional)

        :param span_id: Span ID
        :type span_id: str (optional)

        :param parent_span_id: 父Span ID
        :type parent_span_id: str (optional)

        :param name: Span名称
        :type name: str (optional)

        :param service: Span所属服务名称
        :type service: str (optional)

        :param start: 开始时间戳，单位：us
        :type start: int (optional)

        :param end: 结束时间戳，单位：us
        :type end: int (optional)

        :param duration: 响应耗时，单位：us
        :type duration: int (optional)

        :param host: 实例名称
        :type host: str (optional)

        :param status_code: status_code attribute
        :type status_code: str (optional)

        :param kind: kind attribute
        :type kind: str (optional)

        :param attributes: Span属性列表，值可以是任意类型
        :type attributes: Dict[str, str] (optional)

        :param resource: OTEL Resource对象，值可以是任意类型
        :type resource: Dict[str, str] (optional)

        :param events: 事件列表
        :type events: List[SpanEvent] (optional)

        :param height: 当前span在瀑布图中的高度，从0开始计数
        :type height: int (optional)

        :param sub_spans: 子span列表，用于Trace详情的树形结构
        :type sub_spans: List[Span] (optional)
        """
        super().__init__()
        self.trace_id = trace_id
        self.span_id = span_id
        self.parent_span_id = parent_span_id
        self.name = name
        self.service = service
        self.start = start
        self.end = end
        self.duration = duration
        self.host = host
        self.status_code = status_code
        self.kind = kind
        self.attributes = attributes
        self.resource = resource
        self.events = events
        self.height = height
        self.sub_spans = sub_spans

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
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        if self.span_id is not None:
            result['spanId'] = self.span_id
        if self.parent_span_id is not None:
            result['parentSpanId'] = self.parent_span_id
        if self.name is not None:
            result['name'] = self.name
        if self.service is not None:
            result['service'] = self.service
        if self.start is not None:
            result['start'] = self.start
        if self.end is not None:
            result['end'] = self.end
        if self.duration is not None:
            result['duration'] = self.duration
        if self.host is not None:
            result['host'] = self.host
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.kind is not None:
            result['kind'] = self.kind
        if self.attributes is not None:
            result['attributes'] = self.attributes
        if self.resource is not None:
            result['resource'] = self.resource
        if self.events is not None:
            result['events'] = [i.to_dict() for i in self.events]
        if self.height is not None:
            result['height'] = self.height
        if self.sub_spans is not None:
            result['subSpans'] = [i.to_dict() for i in self.sub_spans]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Span

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('spanId') is not None:
            self.span_id = m.get('spanId')
        if m.get('parentSpanId') is not None:
            self.parent_span_id = m.get('parentSpanId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        if m.get('events') is not None:
            self.events = [SpanEvent().from_dict(i) for i in m.get('events')]
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('subSpans') is not None:
            self.sub_spans = [Span().from_dict(i) for i in m.get('subSpans')]
        return self
