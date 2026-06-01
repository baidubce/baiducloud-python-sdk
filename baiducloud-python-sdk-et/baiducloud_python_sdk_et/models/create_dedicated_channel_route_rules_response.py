"""
Request entity for CreateDedicatedChannelRouteRulesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateDedicatedChannelRouteRulesResponse(BceResponse):
    """
    CreateDedicatedChannelRouteRulesResponse
    """

    def __init__(self, route_rule_id=None):
        """
        Initialize CreateDedicatedChannelRouteRulesResponse response.

        :param route_rule_id: 路由规则ID
        :type route_rule_id: str (optional)
        """
        super().__init__()
        self.route_rule_id = route_rule_id

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
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateDedicatedChannelRouteRulesResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('routeRuleId') is not None:
            self.route_rule_id = m.get('routeRuleId')
        return self
