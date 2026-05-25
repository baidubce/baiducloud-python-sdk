"""
SnatRule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SnatRule(AbstractModel):
    """
    SnatRule
    """

    def __init__(self, rule_id=None, rule_name=None, public_ips_address=None, source_cidr=None, status=None):
        """
        Initialize SnatRule instance.

        :param rule_id: 规则ID
        :type rule_id: str (optional)

        :param rule_name: 规则名称，由大小写字母、数字以及-_ /.特殊字符组成，必须以字母开头，长度1-65
        :type rule_name: str (optional)

        :param public_ips_address: 公网IP列表，关联在NAT网关SNAT上的EIP或共享带宽中的IPs
        :type public_ips_address: List[str] (optional)

        :param source_cidr: 内网IP/网段
        :type source_cidr: str (optional)

        :param status: 规则状态
        :type status: str (optional)
        """
        super().__init__()
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.public_ips_address = public_ips_address
        self.source_cidr = source_cidr
        self.status = status

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
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.public_ips_address is not None:
            result['publicIpsAddress'] = self.public_ips_address
        if self.source_cidr is not None:
            result['sourceCIDR'] = self.source_cidr
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SnatRule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('publicIpsAddress') is not None:
            self.public_ips_address = m.get('publicIpsAddress')
        if m.get('sourceCIDR') is not None:
            self.source_cidr = m.get('sourceCIDR')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
