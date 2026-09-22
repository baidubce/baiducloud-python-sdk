"""
Rule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Rule(AbstractModel):
    """
    Rule
    """

    def __init__(
        self,
        id=None,
        security_group_rule_id=None,
        security_group_id=None,
        security_group_uuid=None,
        direction=None,
        ethertype=None,
        protocol=None,
        port_range=None,
        remote_group_id=None,
        remote_group_name=None,
        remote_ip=None,
        name=None,
    ):
        """
        Initialize Rule instance.

        :param id: 安全组规则ID。
        :type id: str (optional)

        :param security_group_rule_id: 安全组规则ID。
        :type security_group_rule_id: str (optional)

        :param security_group_id: 安全组ID。
        :type security_group_id: str (optional)

        :param security_group_uuid: 安全组长ID。
        :type security_group_uuid: str (optional)

        :param direction: 入站/出站，取值ingress/Ingress或egress/Egress。
        :type direction: str (optional)

        :param ethertype: 网络类型，取值IPv4或IPv6。值为空时表示默认取值IPv4。
        :type ethertype: str (optional)

        :param protocol: 协议类型，tcp、udp或icmp，值为空时默认取值all。
        :type protocol: str (optional)

        :param port_range: 端口范围，可以指定80等单个端口，值为空时默认取值1-65535。
        :type port_range: str (optional)

        :param remote_group_id: 源安全组ID。
        :type remote_group_id: str (optional)

        :param remote_group_name: 源安全组名称。
        :type remote_group_name: str (optional)

        :param remote_ip: 源IP地址。
        :type remote_ip: str (optional)

        :param name: 安全组规则名称。
        :type name: str (optional)
        """
        super().__init__()
        self.id = id
        self.security_group_rule_id = security_group_rule_id
        self.security_group_id = security_group_id
        self.security_group_uuid = security_group_uuid
        self.direction = direction
        self.ethertype = ethertype
        self.protocol = protocol
        self.port_range = port_range
        self.remote_group_id = remote_group_id
        self.remote_group_name = remote_group_name
        self.remote_ip = remote_ip
        self.name = name

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
        if self.id is not None:
            result['id'] = self.id
        if self.security_group_rule_id is not None:
            result['securityGroupRuleId'] = self.security_group_rule_id
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.security_group_uuid is not None:
            result['securityGroupUuid'] = self.security_group_uuid
        if self.direction is not None:
            result['direction'] = self.direction
        if self.ethertype is not None:
            result['ethertype'] = self.ethertype
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.port_range is not None:
            result['portRange'] = self.port_range
        if self.remote_group_id is not None:
            result['remoteGroupId'] = self.remote_group_id
        if self.remote_group_name is not None:
            result['remoteGroupName'] = self.remote_group_name
        if self.remote_ip is not None:
            result['remoteIP'] = self.remote_ip
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Rule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('securityGroupRuleId') is not None:
            self.security_group_rule_id = m.get('securityGroupRuleId')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('securityGroupUuid') is not None:
            self.security_group_uuid = m.get('securityGroupUuid')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('ethertype') is not None:
            self.ethertype = m.get('ethertype')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('portRange') is not None:
            self.port_range = m.get('portRange')
        if m.get('remoteGroupId') is not None:
            self.remote_group_id = m.get('remoteGroupId')
        if m.get('remoteGroupName') is not None:
            self.remote_group_name = m.get('remoteGroupName')
        if m.get('remoteIP') is not None:
            self.remote_ip = m.get('remoteIP')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self
