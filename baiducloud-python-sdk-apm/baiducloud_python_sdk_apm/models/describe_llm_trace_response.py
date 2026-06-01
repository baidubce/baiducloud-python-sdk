"""
Request entity for DescribeLLMTraceResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_apm.models.llm_span import LLMSpan


class DescribeLLMTraceResponse(BceResponse):
    """
    DescribeLLMTraceResponse
    """

    def __init__(
        self,
        success=None,
        code=None,
        message=None,
        duration=None,
        min_start_time=None,
        max_end_time=None,
        tokens=None,
        input=None,
        output=None,
        root_spans=None,
    ):
        """
        Initialize DescribeLLMTraceResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 状态码
        :type code: str (optional)

        :param message: 错误信息
        :type message: str (optional)

        :param duration: Trace耗时，单位：us
        :type duration: int (optional)

        :param min_start_time: Trace开始时间戳，单位：us
        :type min_start_time: int (optional)

        :param max_end_time: Trace结束时间戳，单位：us
        :type max_end_time: int (optional)

        :param tokens: Trace包含的tokens总数
        :type tokens: int (optional)

        :param input: Trace LLM输入，可以是任意类型
        :type input: str (optional)

        :param output: Trace LLM输出，可以是任意类型
        :type output: str (optional)

        :param root_spans: 根Span列表，每个Span包含subSpans子Span列表，形成树形结构
        :type root_spans: List[LLMSpan] (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.message = message
        self.duration = duration
        self.min_start_time = min_start_time
        self.max_end_time = max_end_time
        self.tokens = tokens
        self.input = input
        self.output = output
        self.root_spans = root_spans

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
        if self.duration is not None:
            result['duration'] = self.duration
        if self.min_start_time is not None:
            result['minStartTime'] = self.min_start_time
        if self.max_end_time is not None:
            result['maxEndTime'] = self.max_end_time
        if self.tokens is not None:
            result['tokens'] = self.tokens
        if self.input is not None:
            result['input'] = self.input
        if self.output is not None:
            result['output'] = self.output
        if self.root_spans is not None:
            result['rootSpans'] = [i.to_dict() for i in self.root_spans]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeLLMTraceResponse

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
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('minStartTime') is not None:
            self.min_start_time = m.get('minStartTime')
        if m.get('maxEndTime') is not None:
            self.max_end_time = m.get('maxEndTime')
        if m.get('tokens') is not None:
            self.tokens = m.get('tokens')
        if m.get('input') is not None:
            self.input = m.get('input')
        if m.get('output') is not None:
            self.output = m.get('output')
        if m.get('rootSpans') is not None:
            self.root_spans = [LLMSpan().from_dict(i) for i in m.get('rootSpans')]
        return self
