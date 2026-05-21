"""
Request entity for UpdateRoutingRulesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateRoutingRulesRequest(AbstractModel):
    """
    Request entity for UpdateRoutingRulesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        route_rule_id,
        client_token=None,
        source_address=None,
        destination_address=None,
        nexthop_id=None,
        description=None,
    ):
        """
        Initialize UpdateRoutingRulesRequest request entity.

        :param route_rule_id: route_rule_id parameter
        :type route_rule_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param source_address: 源网段，CIDR格式，可填全部网段0.0.0.0/0、VPC内已有子网网段或子网范围内网段
        :type source_address: str (optional)

        :param destination_address: destination_address parameter
        :type destination_address: str (optional)

        :param nexthop_id: 下一跳ID
        :type nexthop_id: str (optional)

        :param description: 描述，不超过200字符
        :type description: str (optional)
        """
        super().__init__()
        self.route_rule_id = route_rule_id
        self.client_token = client_token
        self.source_address = source_address
        self.destination_address = destination_address
        self.nexthop_id = nexthop_id
        self.description = description

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
        if self.source_address is not None:
            result['sourceAddress'] = self.source_address
        if self.destination_address is not None:
            result['destinationAddress'] = self.destination_address
        if self.nexthop_id is not None:
            result['nexthopId'] = self.nexthop_id
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateRoutingRulesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('routeRuleId') is not None:
            self.route_rule_id = m.get('routeRuleId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('sourceAddress') is not None:
            self.source_address = m.get('sourceAddress')
        if m.get('destinationAddress') is not None:
            self.destination_address = m.get('destinationAddress')
        if m.get('nexthopId') is not None:
            self.nexthop_id = m.get('nexthopId')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
