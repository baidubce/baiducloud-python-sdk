"""
LLMSessionItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LLMSessionItem(AbstractModel):
    """
    LLMSessionItem
    """

    def __init__(
        self,
        session_id=None,
        start_time=None,
        end_time=None,
        duration=None,
        user_id=None,
        trace_count=None,
        input_tokens=None,
        output_tokens=None,
        total_tokens=None,
    ):
        """
        Initialize LLMSessionItem instance.

        :param session_id: 会话ID
        :type session_id: str (optional)

        :param start_time: Session开始时间，UTC时间
        :type start_time: str (optional)

        :param end_time: Session结束时间，UTC时间
        :type end_time: str (optional)

        :param duration: Session持续时长，单位：ms
        :type duration: int (optional)

        :param user_id: 用户ID
        :type user_id: str (optional)

        :param trace_count: Trace数量
        :type trace_count: int (optional)

        :param input_tokens: 输入token数
        :type input_tokens: int (optional)

        :param output_tokens: 输出token数
        :type output_tokens: int (optional)

        :param total_tokens: 总token数
        :type total_tokens: int (optional)
        """
        super().__init__()
        self.session_id = session_id
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.user_id = user_id
        self.trace_count = trace_count
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

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
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.duration is not None:
            result['duration'] = self.duration
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.trace_count is not None:
            result['traceCount'] = self.trace_count
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LLMSessionItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('traceCount') is not None:
            self.trace_count = m.get('traceCount')
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')
        return self
