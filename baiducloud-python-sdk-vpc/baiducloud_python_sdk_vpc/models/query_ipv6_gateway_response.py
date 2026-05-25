"""
Request entity for QueryIpv6GatewayResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.egress_only_rule import EgressOnlyRule
from baiducloud_python_sdk_vpc.models.rate_limit_rule import RateLimitRule


class QueryIpv6GatewayResponse(BceResponse):
    """
    QueryIpv6GatewayResponse
    """

    def __init__(
        self,
        gateway_id=None,
        name=None,
        bandwidth_in_mbps=None,
        vpc_id=None,
        egress_only_rules=None,
        rate_limit_rules=None,
        delete_protect=None,
    ):
        """
        Initialize QueryIpv6GatewayResponse response.

        :param gateway_id: IPv6网关的Id
        :type gateway_id: str (optional)

        :param name: IPv6网关的名称
        :type name: str (optional)

        :param bandwidth_in_mbps: IPv6网关的带宽
        :type bandwidth_in_mbps: int (optional)

        :param vpc_id: IPv6网关所属的vpc的Id
        :type vpc_id: str (optional)

        :param egress_only_rules: IPv6网关只出不进的列表
        :type egress_only_rules: List[EgressOnlyRule] (optional)

        :param rate_limit_rules: IPv6网关限速策略的列表
        :type rate_limit_rules: List[RateLimitRule] (optional)

        :param delete_protect: 是否开启释放保护
        :type delete_protect: bool (optional)
        """
        super().__init__()
        self.gateway_id = gateway_id
        self.name = name
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.vpc_id = vpc_id
        self.egress_only_rules = egress_only_rules
        self.rate_limit_rules = rate_limit_rules
        self.delete_protect = delete_protect

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
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.name is not None:
            result['name'] = self.name
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.egress_only_rules is not None:
            result['egressOnlyRules'] = [i.to_dict() for i in self.egress_only_rules]
        if self.rate_limit_rules is not None:
            result['rateLimitRules'] = [i.to_dict() for i in self.rate_limit_rules]
        if self.delete_protect is not None:
            result['deleteProtect'] = self.delete_protect
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryIpv6GatewayResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('egressOnlyRules') is not None:
            self.egress_only_rules = [EgressOnlyRule().from_dict(i) for i in m.get('egressOnlyRules')]
        if m.get('rateLimitRules') is not None:
            self.rate_limit_rules = [RateLimitRule().from_dict(i) for i in m.get('rateLimitRules')]
        if m.get('deleteProtect') is not None:
            self.delete_protect = m.get('deleteProtect')
        return self
