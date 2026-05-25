"""
Request entity for AddIpv6OnlyOutboundAndNoInboundPolicyResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class AddIpv6OnlyOutboundAndNoInboundPolicyResponse(BceResponse):
    """
    AddIpv6OnlyOutboundAndNoInboundPolicyResponse
    """

    def __init__(self, egress_only_rule_id=None):
        """
        Initialize AddIpv6OnlyOutboundAndNoInboundPolicyResponse response.

        :param egress_only_rule_id: IPv6网关的只出不进的规则Id
        :type egress_only_rule_id: str (optional)
        """
        super().__init__()
        self.egress_only_rule_id = egress_only_rule_id

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
        if self.egress_only_rule_id is not None:
            result['egressOnlyRuleId'] = self.egress_only_rule_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AddIpv6OnlyOutboundAndNoInboundPolicyResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('egressOnlyRuleId') is not None:
            self.egress_only_rule_id = m.get('egressOnlyRuleId')
        return self
