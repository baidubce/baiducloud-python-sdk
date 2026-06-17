"""
Request entity for DescribeAuthorizeRulesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.inst_user_op_authorize_rule_response import InstUserOpAuthorizeRuleResponse


class DescribeAuthorizeRulesResponse(BceResponse):
    """
    DescribeAuthorizeRulesResponse
    """

    def __init__(
        self, request_id=None, is_truncated=None, marker=None, max_keys=None, next_marker=None, rule_list=None
    ):
        """
        Initialize DescribeAuthorizeRulesResponse response.

        :param request_id: 请求Id
        :type request_id: str (optional)

        :param is_truncated: true表示后面还有数据，false表示已经是最后一页
        :type is_truncated: bool (optional)

        :param marker: 标记查询的起始位置
        :type marker: str (optional)

        :param max_keys: 每页包含的最大数量
        :type max_keys: int (optional)

        :param next_marker: 获取下一页所需要传递的marker值。当isTruncated为false时，该域不出现
        :type next_marker: str (optional)

        :param rule_list: 预授权规则列表
        :type rule_list: List[InstUserOpAuthorizeRuleResponse] (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.is_truncated = is_truncated
        self.marker = marker
        self.max_keys = max_keys
        self.next_marker = next_marker
        self.rule_list = rule_list

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.is_truncated is not None:
            result['isTruncated'] = self.is_truncated
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        if self.next_marker is not None:
            result['nextMarker'] = self.next_marker
        if self.rule_list is not None:
            result['ruleList'] = [i.to_dict() for i in self.rule_list]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeAuthorizeRulesResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('isTruncated') is not None:
            self.is_truncated = m.get('isTruncated')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('nextMarker') is not None:
            self.next_marker = m.get('nextMarker')
        if m.get('ruleList') is not None:
            self.rule_list = [InstUserOpAuthorizeRuleResponse().from_dict(i) for i in m.get('ruleList')]
        return self
