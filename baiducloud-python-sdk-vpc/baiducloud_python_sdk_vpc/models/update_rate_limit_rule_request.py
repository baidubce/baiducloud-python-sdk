"""
Request entity for UpdateRateLimitRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateRateLimitRuleRequest(AbstractModel):
    """
    Request entity for UpdateRateLimitRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, gateway_id, rate_limit_rule_id, ingress_bandwidth_in_mbps, egress_bandwidth_in_mbps, client_token=None
    ):
        """
        Initialize UpdateRateLimitRuleRequest request entity.

        :param gateway_id: gateway_id parameter
        :type gateway_id: str (required)

        :param rate_limit_rule_id: rate_limit_rule_id parameter
        :type rate_limit_rule_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param ingress_bandwidth_in_mbps: 限速策略的入向带宽
        :type ingress_bandwidth_in_mbps: int (required)

        :param egress_bandwidth_in_mbps: 限速策略的出向带宽
        :type egress_bandwidth_in_mbps: int (required)
        """
        super().__init__()
        self.gateway_id = gateway_id
        self.rate_limit_rule_id = rate_limit_rule_id
        self.client_token = client_token
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
        :rtype: UpdateRateLimitRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('rateLimitRuleId') is not None:
            self.rate_limit_rule_id = m.get('rateLimitRuleId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ingressBandwidthInMbps') is not None:
            self.ingress_bandwidth_in_mbps = m.get('ingressBandwidthInMbps')
        if m.get('egressBandwidthInMbps') is not None:
            self.egress_bandwidth_in_mbps = m.get('egressBandwidthInMbps')
        return self
