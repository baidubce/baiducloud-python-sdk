"""
DnatRuleRequest information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DnatRuleRequest(AbstractModel):
    """
    DnatRuleRequest
    """

    def __init__(
        self,
        rule_name=None,
        public_ip_address=None,
        private_ip_address=None,
        protocol=None,
        public_port=None,
        private_port=None,
        public_port_range=None,
        private_port_range=None,
    ):
        """
        Initialize DnatRuleRequest instance.

        :param rule_name: 名称，由大小写字母、数字以及-\\_ /.特殊字符组成，必须以字母开头，长度1-65，非必填
        :type rule_name: str (optional)

        :param public_ip_address: 公网IP，关联在NAT网关DNAT上的EIP或共享带宽中的IP
        :type public_ip_address: str (optional)

        :param private_ip_address: 内网IP
        :type private_ip_address: str (optional)

        :param protocol: 协议，支持TCP、UDP、all
        :type protocol: str (optional)

        :param public_port: 公网端口(1-65535)，协议为TCP、UDP时有效，不能与端口范围同时指定
        :type public_port: int (optional)

        :param private_port: 内网端口(1-65535)，协议为TCP、UDP时有效，不能与端口范围同时指定
        :type private_port: int (optional)

        :param public_port_range: 公网端口范围，如“80-90”，协议为TCP、UDP时有效，不能与单个端口同时指定
        :type public_port_range: str (optional)

        :param private_port_range: 内网端口范围，如“80-90”，协议为TCP、UDP时有效，不能与单个端口同时指定
        :type private_port_range: str (optional)
        """
        super().__init__()
        self.rule_name = rule_name
        self.public_ip_address = public_ip_address
        self.private_ip_address = private_ip_address
        self.protocol = protocol
        self.public_port = public_port
        self.private_port = private_port
        self.public_port_range = public_port_range
        self.private_port_range = private_port_range

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
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.public_ip_address is not None:
            result['publicIpAddress'] = self.public_ip_address
        if self.private_ip_address is not None:
            result['privateIpAddress'] = self.private_ip_address
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
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DnatRuleRequest

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('publicIpAddress') is not None:
            self.public_ip_address = m.get('publicIpAddress')
        if m.get('privateIpAddress') is not None:
            self.private_ip_address = m.get('privateIpAddress')
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
        return self
