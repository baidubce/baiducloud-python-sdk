"""
Request entity for DescribeLLMSessionResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_apm.models.session_trace import SessionTrace


class DescribeLLMSessionResponse(BceResponse):
    """
    DescribeLLMSessionResponse
    """

    def __init__(
        self,
        success=None,
        code=None,
        message=None,
        start_time=None,
        end_time=None,
        duration=None,
        user_id=None,
        trace_count=None,
        input_tokens=None,
        output_tokens=None,
        total_tokens=None,
        traces=None,
    ):
        """
        Initialize DescribeLLMSessionResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 状态码
        :type code: str (optional)

        :param message: 错误信息
        :type message: str (optional)

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

        :param traces: Traces列表
        :type traces: List[SessionTrace] (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.message = message
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.user_id = user_id
        self.trace_count = trace_count
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens
        self.traces = traces

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.success is not None:
            result['success'] = self.success
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
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
        if self.traces is not None:
            result['traces'] = [i.to_dict() for i in self.traces]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeLLMSessionResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
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
        if m.get('traces') is not None:
            self.traces = [SessionTrace().from_dict(i) for i in m.get('traces')]
        return self
