"""
EtChannelRouteRule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class EtChannelRouteRule(AbstractModel):
    """
    EtChannelRouteRule
    """

    def __init__(
        self,
        route_rule_id=None,
        ip_version=None,
        dest_address=None,
        nexthop_type=None,
        nexthop_id=None,
        description=None,
    ):
        """
        Initialize EtChannelRouteRule instance.

        :param route_rule_id: 专线通道路由规则ID
        :type route_rule_id: str (optional)

        :param ip_version: IP协议类型，取值[4 \\| 6]
        :type ip_version: int (optional)

        :param dest_address: 目标网段
        :type dest_address: str (optional)

        :param nexthop_type: 下一跳类型，取值[\"etGateway\" \\| \"etChannel\"]，分别表示专线网关、专线通道
        :type nexthop_type: str (optional)

        :param nexthop_id: 下一跳实例ID
        :type nexthop_id: str (optional)

        :param description: 描述
        :type description: str (optional)
        """
        super().__init__()
        self.route_rule_id = route_rule_id
        self.ip_version = ip_version
        self.dest_address = dest_address
        self.nexthop_type = nexthop_type
        self.nexthop_id = nexthop_id
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
        if self.ip_version is not None:
            result['ipVersion'] = self.ip_version
        if self.dest_address is not None:
            result['destAddress'] = self.dest_address
        if self.nexthop_type is not None:
            result['nexthopType'] = self.nexthop_type
        if self.nexthop_id is not None:
            result['nexthopId'] = self.nexthop_id
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
        :rtype: EtChannelRouteRule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('routeRuleId') is not None:
            self.route_rule_id = m.get('routeRuleId')
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        if m.get('destAddress') is not None:
            self.dest_address = m.get('destAddress')
        if m.get('nexthopType') is not None:
            self.nexthop_type = m.get('nexthopType')
        if m.get('nexthopId') is not None:
            self.nexthop_id = m.get('nexthopId')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
