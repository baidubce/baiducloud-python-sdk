"""
Request entity for CreateRateLimitRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateRateLimitRuleRequest(AbstractModel):
    """
    Request entity for CreateRateLimitRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, gateway_id, ipv6_address, ingress_bandwidth_in_mbps, egress_bandwidth_in_mbps, client_token=None
    ):
        """
        Initialize CreateRateLimitRuleRequest request entity.

        :param gateway_id: gateway_id parameter
        :type gateway_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param ipv6_address: Ipv6的地址
        :type ipv6_address: str (required)

        :param ingress_bandwidth_in_mbps: 限速策略的入向带宽
        :type ingress_bandwidth_in_mbps: int (required)

        :param egress_bandwidth_in_mbps: 限速策略的出向带宽
        :type egress_bandwidth_in_mbps: int (required)
        """
        super().__init__()
        self.gateway_id = gateway_id
        self.client_token = client_token
        self.ipv6_address = ipv6_address
        self.ingress_bandwidth_in_mbps = ingress_bandwidth_in_mbps
        self.egress_bandwidth_in_mbps = egress_bandwidth_in_mbps

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
        if self.ipv6_address is not None:
            result['ipv6Address'] = self.ipv6_address
        if self.ingress_bandwidth_in_mbps is not None:
            result['ingressBandwidthInMbps'] = self.ingress_bandwidth_in_mbps
        if self.egress_bandwidth_in_mbps is not None:
            result['egressBandwidthInMbps'] = self.egress_bandwidth_in_mbps
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateRateLimitRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ipv6Address') is not None:
            self.ipv6_address = m.get('ipv6Address')
        if m.get('ingressBandwidthInMbps') is not None:
            self.ingress_bandwidth_in_mbps = m.get('ingressBandwidthInMbps')
        if m.get('egressBandwidthInMbps') is not None:
            self.egress_bandwidth_in_mbps = m.get('egressBandwidthInMbps')
        return self
