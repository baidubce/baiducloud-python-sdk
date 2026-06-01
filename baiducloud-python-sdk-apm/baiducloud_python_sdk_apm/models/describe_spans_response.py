"""
Request entity for DescribeSpansResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_apm.models.span import Span


class DescribeSpansResponse(BceResponse):
    """
    DescribeSpansResponse
    """

    def __init__(self, success=None, code=None, message=None, spans=None, next_marker=None, is_truncated=None):
        """
        Initialize DescribeSpansResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 状态码
        :type code: str (optional)

        :param message: 错误信息
        :type message: str (optional)

        :param spans: Span列表
        :type spans: List[Span] (optional)

        :param next_marker: 翻页游标，用于填充下一页请求中的marker参数
        :type next_marker: str (optional)

        :param is_truncated: 是否还有下一页，true表示还有下一页，false表示已是最后一页
        :type is_truncated: bool (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.message = message
        self.spans = spans
        self.next_marker = next_marker
        self.is_truncated = is_truncated

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
        if self.spans is not None:
            result['spans'] = [i.to_dict() for i in self.spans]
        if self.next_marker is not None:
            result['nextMarker'] = self.next_marker
        if self.is_truncated is not None:
            result['isTruncated'] = self.is_truncated
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeSpansResponse

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
        if m.get('spans') is not None:
            self.spans = [Span().from_dict(i) for i in m.get('spans')]
        if m.get('nextMarker') is not None:
            self.next_marker = m.get('nextMarker')
        if m.get('isTruncated') is not None:
            self.is_truncated = m.get('isTruncated')
        return self
