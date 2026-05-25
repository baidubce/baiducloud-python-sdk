"""
Request entity for UpdateSnatRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateSnatRuleRequest(AbstractModel):
    """
    Request entity for UpdateSnatRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, nat_id, rule_id, client_token=None, rule_name=None, source_cidr=None, public_ips_address=None):
        """
        Initialize UpdateSnatRuleRequest request entity.

        :param nat_id: nat_id parameter
        :type nat_id: str (required)

        :param rule_id: rule_id parameter
        :type rule_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param rule_name: SNAT规则名字
        :type rule_name: str (optional)

        :param source_cidr: 内网IP/网段
        :type source_cidr: str (optional)

        :param public_ips_address: 公网IPs
        :type public_ips_address: List[str] (optional)
        """
        super().__init__()
        self.nat_id = nat_id
        self.rule_id = rule_id
        self.client_token = client_token
        self.rule_name = rule_name
        self.source_cidr = source_cidr
        self.public_ips_address = public_ips_address

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
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.source_cidr is not None:
            result['sourceCIDR'] = self.source_cidr
        if self.public_ips_address is not None:
            result['publicIpsAddress'] = self.public_ips_address
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateSnatRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('natId') is not None:
            self.nat_id = m.get('natId')
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('sourceCIDR') is not None:
            self.source_cidr = m.get('sourceCIDR')
        if m.get('publicIpsAddress') is not None:
            self.public_ips_address = m.get('publicIpsAddress')
        return self
