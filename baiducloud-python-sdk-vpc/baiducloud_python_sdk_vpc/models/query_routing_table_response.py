"""
Request entity for QueryRoutingTableResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.route_rule import RouteRule


class QueryRoutingTableResponse(BceResponse):
    """
    QueryRoutingTableResponse
    """

    def __init__(self, name=None, route_table_id=None, vpc_id=None, route_rules=None):
        """
        Initialize QueryRoutingTableResponse response.

        :param name: 路由表名称
        :type name: str (optional)

        :param route_table_id: 路由表ID
        :type route_table_id: str (optional)

        :param vpc_id: VPC的ID
        :type vpc_id: str (optional)

        :param route_rules: 路由规则列表
        :type route_rules: List[RouteRule] (optional)
        """
        super().__init__()
        self.name = name
        self.route_table_id = route_table_id
        self.vpc_id = vpc_id
        self.route_rules = route_rules

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
        if self.name is not None:
            result['name'] = self.name
        if self.route_table_id is not None:
            result['routeTableId'] = self.route_table_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.route_rules is not None:
            result['routeRules'] = [i.to_dict() for i in self.route_rules]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryRoutingTableResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('routeTableId') is not None:
            self.route_table_id = m.get('routeTableId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('routeRules') is not None:
            self.route_rules = [RouteRule().from_dict(i) for i in m.get('routeRules')]
        return self
