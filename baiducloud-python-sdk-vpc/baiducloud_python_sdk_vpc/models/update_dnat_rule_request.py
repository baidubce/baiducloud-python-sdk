"""
Request entity for UpdateDnatRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateDnatRuleRequest(AbstractModel):
    """
    Request entity for UpdateDnatRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        nat_id,
        rule_id,
        client_token=None,
        rule_name=None,
        protocol=None,
        public_port=None,
        private_port=None,
        public_port_range=None,
        private_port_range=None,
        private_ip_address=None,
        public_ip_address=None,
    ):
        """
        Initialize UpdateDnatRuleRequest request entity.

        :param nat_id: nat_id parameter
        :type nat_id: str (required)

        :param rule_id: rule_id parameter
        :type rule_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param rule_name: DNAT规则名字
        :type rule_name: str (optional)

        :param protocol: 协议，支持TCP、UDP、all
        :type protocol: str (optional)

        :param public_port: 公网端口
        :type public_port: int (optional)

        :param private_port: 内网端口
        :type private_port: int (optional)

        :param public_port_range: 公网端口范围
        :type public_port_range: str (optional)

        :param private_port_range: 内网端口范围
        :type private_port_range: str (optional)

        :param private_ip_address: 内网IP
        :type private_ip_address: str (optional)

        :param public_ip_address: 公网IP
        :type public_ip_address: str (optional)
        """
        super().__init__()
        self.nat_id = nat_id
        self.rule_id = rule_id
        self.client_token = client_token
        self.rule_name = rule_name
        self.protocol = protocol
        self.public_port = public_port
        self.private_port = private_port
        self.public_port_range = public_port_range
        self.private_port_range = private_port_range
        self.private_ip_address = private_ip_address
        self.public_ip_address = public_ip_address

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
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.public_port is not None:
            result['publicPort'] = self.public_port
        if self.private_port is not None:
            result['privatePort'] = self.private_port
        if self.public_port_range is not None:
            result['publicPortRange'] = self.public_port_range
        if self.private_port_range is not None:
            result['privatePortRange'] = self.private_port_range
        if self.private_ip_address is not None:
            result['privateIpAddress'] = self.private_ip_address
        if self.public_ip_address is not None:
            result['publicIpAddress'] = self.public_ip_address
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateDnatRuleRequest

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
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('publicPort') is not None:
            self.public_port = m.get('publicPort')
        if m.get('privatePort') is not None:
            self.private_port = m.get('privatePort')
        if m.get('publicPortRange') is not None:
            self.public_port_range = m.get('publicPortRange')
        if m.get('privatePortRange') is not None:
            self.private_port_range = m.get('privatePortRange')
        if m.get('privateIpAddress') is not None:
            self.private_ip_address = m.get('privateIpAddress')
        if m.get('publicIpAddress') is not None:
            self.public_ip_address = m.get('publicIpAddress')
        return self
