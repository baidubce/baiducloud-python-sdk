"""
Request entity for BatchAddSnatRulesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.snat_rule_request import SnatRuleRequest


class BatchAddSnatRulesRequest(AbstractModel):
    """
    Request entity for BatchAddSnatRulesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, nat_id, snat_rules, client_token=None):
        """
        Initialize BatchAddSnatRulesRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param nat_id: NAT网关的ID
        :type nat_id: str (required)

        :param snat_rules: 内网IP/网段
        :type snat_rules: List[SnatRuleRequest] (required)
        """
        super().__init__()
        self.client_token = client_token
        self.nat_id = nat_id
        self.snat_rules = snat_rules

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
        if self.nat_id is not None:
            result['natId'] = self.nat_id
        if self.snat_rules is not None:
            result['snatRules'] = [i.to_dict() for i in self.snat_rules]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchAddSnatRulesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('natId') is not None:
            self.nat_id = m.get('natId')
        if m.get('snatRules') is not None:
            self.snat_rules = [SnatRuleRequest().from_dict(i) for i in m.get('snatRules')]
        return self
