"""
Request entity for DescribeAuthorizeRulesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeAuthorizeRulesRequest(AbstractModel):
    """
    Request entity for DescribeAuthorizeRulesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, action, marker=None, max_keys=None, rule_ids=None, rule_names=None):
        """
        Initialize DescribeAuthorizeRulesRequest request entity.

        :param action: action parameter
        :type action: str (required)

        :param marker: 批量获取列表的查询的起始位置，是一个由系统生成的字符串
        :type marker: str (optional)

        :param max_keys: 每页包含的最大数量，最大数量通常不超过100，缺省值为10
        :type max_keys: int (optional)

        :param rule_ids: 待查询的规则ID
        :type rule_ids: List[str] (optional)

        :param rule_names: 待查询的规则名称
        :type rule_names: List[str] (optional)
        """
        super().__init__()
        self.action = action
        self.marker = marker
        self.max_keys = max_keys
        self.rule_ids = rule_ids
        self.rule_names = rule_names

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
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        if self.rule_ids is not None:
            result['ruleIds'] = self.rule_ids
        if self.rule_names is not None:
            result['ruleNames'] = self.rule_names
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeAuthorizeRulesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('ruleIds') is not None:
            self.rule_ids = m.get('ruleIds')
        if m.get('ruleNames') is not None:
            self.rule_names = m.get('ruleNames')
        return self
