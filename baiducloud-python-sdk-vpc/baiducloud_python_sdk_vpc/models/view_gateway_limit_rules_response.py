"""
Request entity for ViewGatewayLimitRulesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.glr_item import GlrItem


class ViewGatewayLimitRulesResponse(BceResponse):
    """
    ViewGatewayLimitRulesResponse
    """

    def __init__(self, result=None, marker=None, is_truncated=None, max_keys=None, next_marker=None):
        """
        Initialize ViewGatewayLimitRulesResponse response.

        :param result: 限流规则列表
        :type result: List[GlrItem] (optional)

        :param marker: 标记查询的起始位置
        :type marker: str (optional)

        :param is_truncated: true表示后面还有数据，false表示已经是最后一页
        :type is_truncated: bool (optional)

        :param max_keys: 每页包含的最大数量
        :type max_keys: int (optional)

        :param next_marker: 获取下一页所需要传递的marker值。当isTruncated为false时，该域不出现
        :type next_marker: str (optional)
        """
        super().__init__()
        self.result = result
        self.marker = marker
        self.is_truncated = is_truncated
        self.max_keys = max_keys
        self.next_marker = next_marker

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
            result['metadata'] = self.metadata
        if self.result is not None:
            result['result'] = [i.to_dict() for i in self.result]
        if self.marker is not None:
            result['marker'] = self.marker
        if self.is_truncated is not None:
            result['isTruncated'] = self.is_truncated
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        if self.next_marker is not None:
            result['nextMarker'] = self.next_marker
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ViewGatewayLimitRulesResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('result') is not None:
            self.result = [GlrItem().from_dict(i) for i in m.get('result')]
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('isTruncated') is not None:
            self.is_truncated = m.get('isTruncated')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('nextMarker') is not None:
            self.next_marker = m.get('nextMarker')
        return self
