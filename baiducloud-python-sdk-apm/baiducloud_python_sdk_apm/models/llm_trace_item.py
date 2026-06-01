"""
LLMTraceItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LLMTraceItem(AbstractModel):
    """
    LLMTraceItem
    """

    def __init__(
        self,
        trace_id=None,
        start_time=None,
        end_time=None,
        service=None,
        session_id=None,
        user_id=None,
        input_tokens=None,
        output_tokens=None,
        total_tokens=None,
        input=None,
        output=None,
        models=None,
        tools=None,
        duration=None,
    ):
        """
        Initialize LLMTraceItem instance.

        :param trace_id: Trace ID
        :type trace_id: str (optional)

        :param start_time: 开始时间，UTC时间
        :type start_time: str (optional)

        :param end_time: 结束时间，UTC时间
        :type end_time: str (optional)

        :param service: 入口应用名称
        :type service: str (optional)

        :param session_id: 会话ID
        :type session_id: str (optional)

        :param user_id: 用户ID
        :type user_id: str (optional)

        :param input_tokens: 输入token数
        :type input_tokens: int (optional)

        :param output_tokens: 输出token数
        :type output_tokens: int (optional)

        :param total_tokens: 总token数
        :type total_tokens: int (optional)

        :param input: 输入内容
        :type input: str (optional)

        :param output: 输出内容
        :type output: str (optional)

        :param models: 模型列表
        :type models: List[str] (optional)

        :param tools: 工具列表
        :type tools: List[str] (optional)

        :param duration: 持续时长，单位：ms
        :type duration: int (optional)
        """
        super().__init__()
        self.trace_id = trace_id
        self.start_time = start_time
        self.end_time = end_time
        self.service = service
        self.session_id = session_id
        self.user_id = user_id
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens
        self.input = input
        self.output = output
        self.models = models
        self.tools = tools
        self.duration = duration

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
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.service is not None:
            result['service'] = self.service
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens
        if self.input is not None:
            result['input'] = self.input
        if self.output is not None:
            result['output'] = self.output
        if self.models is not None:
            result['models'] = self.models
        if self.tools is not None:
            result['tools'] = self.tools
        if self.duration is not None:
            result['duration'] = self.duration
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LLMTraceItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')
        if m.get('input') is not None:
            self.input = m.get('input')
        if m.get('output') is not None:
            self.output = m.get('output')
        if m.get('models') is not None:
            self.models = m.get('models')
        if m.get('tools') is not None:
            self.tools = m.get('tools')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        return self
