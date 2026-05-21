"""
RouteRule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RouteRule(AbstractModel):
    """
    RouteRule
    """

    def __init__(
        self,
        route_rule_id=None,
        route_table_id=None,
        source_address=None,
        destination_address=None,
        nexthop_id=None,
        nexthop_type=None,
        path_type=None,
        description=None,
    ):
        """
        Initialize RouteRule instance.

        :param route_rule_id: 路由规则ID
        :type route_rule_id: str (optional)

        :param route_table_id: 路由表ID
        :type route_table_id: str (optional)

        :param source_address: 源网段
        :type source_address: str (optional)

        :param destination_address: 目标网段
        :type destination_address: str (optional)

        :param nexthop_id: 下一跳ID，当nexthopType是本地网关类型时，该字段可以为空
        :type nexthop_id: str (optional)

        :param nexthop_type: nexthop_type attribute
        :type nexthop_type: str (optional)

        :param path_type: 单线或多线路由。单线为\"normal\"，多线取值为ecmp或ha:active或ha:standby
        :type path_type: str (optional)

        :param description: 描述
        :type description: str (optional)
        """
        super().__init__()
        self.route_rule_id = route_rule_id
        self.route_table_id = route_table_id
        self.source_address = source_address
        self.destination_address = destination_address
        self.nexthop_id = nexthop_id
        self.nexthop_type = nexthop_type
        self.path_type = path_type
        self.description = description

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
        if self.route_rule_id is not None:
            result['routeRuleId'] = self.route_rule_id
        if self.route_table_id is not None:
            result['routeTableId'] = self.route_table_id
        if self.source_address is not None:
            result['sourceAddress'] = self.source_address
        if self.destination_address is not None:
            result['destinationAddress'] = self.destination_address
        if self.nexthop_id is not None:
            result['nexthopId'] = self.nexthop_id
        if self.nexthop_type is not None:
            result['nexthopType'] = self.nexthop_type
        if self.path_type is not None:
            result['pathType'] = self.path_type
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RouteRule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('routeRuleId') is not None:
            self.route_rule_id = m.get('routeRuleId')
        if m.get('routeTableId') is not None:
            self.route_table_id = m.get('routeTableId')
        if m.get('sourceAddress') is not None:
            self.source_address = m.get('sourceAddress')
        if m.get('destinationAddress') is not None:
            self.destination_address = m.get('destinationAddress')
        if m.get('nexthopId') is not None:
            self.nexthop_id = m.get('nexthopId')
        if m.get('nexthopType') is not None:
            self.nexthop_type = m.get('nexthopType')
        if m.get('pathType') is not None:
            self.path_type = m.get('pathType')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
