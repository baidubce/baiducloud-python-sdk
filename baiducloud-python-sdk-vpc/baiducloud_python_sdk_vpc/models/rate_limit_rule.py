"""
RateLimitRule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RateLimitRule(AbstractModel):
    """
    RateLimitRule
    """

    def __init__(
        self, rate_limit_rule_id=None, ipv6_address=None, ingress_bandwidth_in_mbps=None, egress_bandwidth_in_mbps=None
    ):
        """
        Initialize RateLimitRule instance.

        :param rate_limit_rule_id: IPv6限速策略的ID
        :type rate_limit_rule_id: str (optional)

        :param ipv6_address: 限速的IPv6地址
        :type ipv6_address: str (optional)

        :param ingress_bandwidth_in_mbps: 入口带宽
        :type ingress_bandwidth_in_mbps: int (optional)

        :param egress_bandwidth_in_mbps: 出口带宽
        :type egress_bandwidth_in_mbps: int (optional)
        """
        super().__init__()
        self.rate_limit_rule_id = rate_limit_rule_id
        self.ipv6_address = ipv6_address
        self.ingress_bandwidth_in_mbps = ingress_bandwidth_in_mbps
        self.egress_bandwidth_in_mbps = egress_bandwidth_in_mbps

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
        if self.rate_limit_rule_id is not None:
            result['rateLimitRuleId'] = self.rate_limit_rule_id
        if self.ipv6_address is not None:
            result['ipv6Address'] = self.ipv6_address
        if self.ingress_bandwidth_in_mbps is not None:
            result['ingressBandwidthInMbps'] = self.ingress_bandwidth_in_mbps
        if self.egress_bandwidth_in_mbps is not None:
            result['egressBandwidthInMbps'] = self.egress_bandwidth_in_mbps
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RateLimitRule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('rateLimitRuleId') is not None:
            self.rate_limit_rule_id = m.get('rateLimitRuleId')
        if m.get('ipv6Address') is not None:
            self.ipv6_address = m.get('ipv6Address')
        if m.get('ingressBandwidthInMbps') is not None:
            self.ingress_bandwidth_in_mbps = m.get('ingressBandwidthInMbps')
        if m.get('egressBandwidthInMbps') is not None:
            self.egress_bandwidth_in_mbps = m.get('egressBandwidthInMbps')
        return self
