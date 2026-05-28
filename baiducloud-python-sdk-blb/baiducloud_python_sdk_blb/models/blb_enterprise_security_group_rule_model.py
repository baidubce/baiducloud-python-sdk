"""
BlbEnterpriseSecurityGroupRuleModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BlbEnterpriseSecurityGroupRuleModel(AbstractModel):
    """
    BlbEnterpriseSecurityGroupRuleModel
    """

    def __init__(
        self,
        remark=None,
        direction=None,
        ethertype=None,
        port_range=None,
        protocol=None,
        source_ip=None,
        dest_ip=None,
        action=None,
        priority=None,
        enterprise_security_group_rule_id=None,
    ):
        """
        Initialize BlbEnterpriseSecurityGroupRuleModel instance.

        :param remark: 备注，长度1-255。
        :type remark: str (optional)

        :param direction: 入站/出站，取值ingress或egress。
        :type direction: str (optional)

        :param ethertype: 网络类型，取值IPv4或IPv6。值为空时表示默认取值IPv4。
        :type ethertype: str (optional)

        :param port_range: port_range attribute
        :type port_range: str (optional)

        :param protocol: 协议类型，tcp、udp或icmp，值为空时默认取值all。
        :type protocol: str (optional)

        :param source_ip: 源IP地址，all表示全部。
        :type source_ip: str (optional)

        :param dest_ip: 目的IP地址，all表示全部。
        :type dest_ip: str (optional)

        :param action: 允许/拒绝，取值allow或deny。
        :type action: str (optional)

        :param priority: 优先级，取值范围1-1000。
        :type priority: int (optional)

        :param enterprise_security_group_rule_id: 企业安全组规则ID
        :type enterprise_security_group_rule_id: str (optional)
        """
        super().__init__()
        self.remark = remark
        self.direction = direction
        self.ethertype = ethertype
        self.port_range = port_range
        self.protocol = protocol
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.action = action
        self.priority = priority
        self.enterprise_security_group_rule_id = enterprise_security_group_rule_id

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
        if self.remark is not None:
            result['remark'] = self.remark
        if self.direction is not None:
            result['direction'] = self.direction
        if self.ethertype is not None:
            result['ethertype'] = self.ethertype
        if self.port_range is not None:
            result['portRange'] = self.port_range
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.source_ip is not None:
            result['sourceIp'] = self.source_ip
        if self.dest_ip is not None:
            result['destIp'] = self.dest_ip
        if self.action is not None:
            result['action'] = self.action
        if self.priority is not None:
            result['priority'] = self.priority
        if self.enterprise_security_group_rule_id is not None:
            result['enterpriseSecurityGroupRuleId'] = self.enterprise_security_group_rule_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BlbEnterpriseSecurityGroupRuleModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('ethertype') is not None:
            self.ethertype = m.get('ethertype')
        if m.get('portRange') is not None:
            self.port_range = m.get('portRange')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('sourceIp') is not None:
            self.source_ip = m.get('sourceIp')
        if m.get('destIp') is not None:
            self.dest_ip = m.get('destIp')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('enterpriseSecurityGroupRuleId') is not None:
            self.enterprise_security_group_rule_id = m.get('enterpriseSecurityGroupRuleId')
        return self
