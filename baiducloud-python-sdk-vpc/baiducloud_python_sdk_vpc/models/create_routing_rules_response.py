"""
Request entity for CreateRoutingRulesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateRoutingRulesResponse(BceResponse):
    """
    CreateRoutingRulesResponse
    """

    def __init__(self, route_rule_id=None, route_rule_ids=None):
        """
        Initialize CreateRoutingRulesResponse response.

        :param route_rule_id: 单线路由规则ID，创建单线路由时返回该参数
        :type route_rule_id: str (optional)

        :param route_rule_ids: 多线路由规则ID，创建多线路由（主备、负载均衡）时返回该参数
        :type route_rule_ids: List[str] (optional)
        """
        super().__init__()
        self.route_rule_id = route_rule_id
        self.route_rule_ids = route_rule_ids

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
        if self.route_rule_id is not None:
            result['routeRuleId'] = self.route_rule_id
        if self.route_rule_ids is not None:
            result['routeRuleIds'] = self.route_rule_ids
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateRoutingRulesResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('routeRuleId') is not None:
            self.route_rule_id = m.get('routeRuleId')
        if m.get('routeRuleIds') is not None:
            self.route_rule_ids = m.get('routeRuleIds')
        return self
