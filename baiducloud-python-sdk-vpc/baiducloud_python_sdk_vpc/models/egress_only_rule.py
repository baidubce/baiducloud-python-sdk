"""
EgressOnlyRule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class EgressOnlyRule(AbstractModel):
    """
    EgressOnlyRule
    """

    def __init__(self, egress_only_rule_id=None, cidr=None):
        """
        Initialize EgressOnlyRule instance.

        :param egress_only_rule_id: 只出不进策略的ID
        :type egress_only_rule_id: str (optional)

        :param cidr: 只出不进策略的cidr
        :type cidr: str (optional)
        """
        super().__init__()
        self.egress_only_rule_id = egress_only_rule_id
        self.cidr = cidr

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
        if self.egress_only_rule_id is not None:
            result['egressOnlyRuleId'] = self.egress_only_rule_id
        if self.cidr is not None:
            result['cidr'] = self.cidr
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EgressOnlyRule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('egressOnlyRuleId') is not None:
            self.egress_only_rule_id = m.get('egressOnlyRuleId')
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        return self
