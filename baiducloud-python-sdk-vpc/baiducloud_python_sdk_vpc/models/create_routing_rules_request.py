"""
Request entity for CreateRoutingRulesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.next_hop import NextHop


class CreateRoutingRulesRequest(AbstractModel):
    """
    Request entity for CreateRoutingRulesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        route_table_id,
        source_address,
        destination_address,
        client_token=None,
        nexthop_id=None,
        nexthop_type=None,
        next_hop_list=None,
        description=None,
    ):
        """
        Initialize CreateRoutingRulesRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param route_table_id: 路由表ID
        :type route_table_id: str (required)

        :param source_address: 源网段，可填全部网段0.0.0.0/0、VPC内已有子网网段或子网范围内网段
        :type source_address: str (required)

        :param destination_address: 目标网段
        :type destination_address: str (required)

        :param nexthop_id: 下一跳ID，创建单线路由时该字段必填
        :type nexthop_id: str (optional)

        :param nexthop_type: nexthop_type parameter
        :type nexthop_type: str (optional)

        :param next_hop_list: 多线路由下一跳信息，创建多线路由时该字段必填
        :type next_hop_list: List[NextHop] (optional)

        :param description: 路由表规则描述，不超过200字符
        :type description: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.route_table_id = route_table_id
        self.source_address = source_address
        self.destination_address = destination_address
        self.nexthop_id = nexthop_id
        self.nexthop_type = nexthop_type
        self.next_hop_list = next_hop_list
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
        if self.next_hop_list is not None:
            result['nextHopList'] = [i.to_dict() for i in self.next_hop_list]
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
        :rtype: CreateRoutingRulesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
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
        if m.get('nextHopList') is not None:
            self.next_hop_list = [NextHop().from_dict(i) for i in m.get('nextHopList')]
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
