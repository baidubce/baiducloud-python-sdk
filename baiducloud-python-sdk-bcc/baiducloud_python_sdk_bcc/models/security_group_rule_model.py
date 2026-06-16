"""
SecurityGroupRuleModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SecurityGroupRuleModel(AbstractModel):
    """
    SecurityGroupRuleModel
    """

    def __init__(
        self,
        remark=None,
        direction=None,
        ethertype=None,
        port_range=None,
        protocol=None,
        source_group_id=None,
        source_ip=None,
        dest_group_id=None,
        dest_ip=None,
        security_group_id=None,
        security_group_rule_id=None,
        created_time=None,
        updated_time=None,
    ):
        """
        Initialize SecurityGroupRuleModel instance.

        :param remark: 规则备注（创建安全组、查询安全组列表、授权安全组规则、撤销安全组规则）
        :type remark: str (optional)

        :param direction: 规则方向，取值：ingress/egress（创建安全组、查询安全组列表、授权安全组规则、撤销安全组规则）
        :type direction: str (optional)

        :param ethertype: 以太网协议类型（创建安全组、查询安全组列表、授权安全组规则、撤销安全组规则）
        :type ethertype: str (optional)

        :param port_range: 端口范围，如1-65535，空字符串表示所有端口（创建安全组、查询安全组列表、授权安全组规则、撤销安全组规则）
        :type port_range: str (optional)

        :param protocol: protocol attribute
        :type protocol: str (optional)

        :param source_group_id: 源安全组ID，仅direction为ingress时有效（创建安全组、查询安全组列表、授权安全组规则、撤销安全组规则）
        :type source_group_id: str (optional)

        :param source_ip: source_ip attribute
        :type source_ip: str (optional)

        :param dest_group_id: 目标安全组ID，仅direction为egress时有效（创建安全组、查询安全组列表、授权安全组规则、撤销安全组规则）
        :type dest_group_id: str (optional)

        :param dest_ip: dest_ip attribute
        :type dest_ip: str (optional)

        :param security_group_id: 规则所属安全组ID（查询安全组列表）
        :type security_group_id: str (optional)

        :param security_group_rule_id: 安全组规则ID（查询安全组列表）
        :type security_group_rule_id: str (optional)

        :param created_time: 规则创建时间（查询安全组列表）
        :type created_time: str (optional)

        :param updated_time: 规则更新时间（查询安全组列表）
        :type updated_time: str (optional)
        """
        super().__init__()
        self.remark = remark
        self.direction = direction
        self.ethertype = ethertype
        self.port_range = port_range
        self.protocol = protocol
        self.source_group_id = source_group_id
        self.source_ip = source_ip
        self.dest_group_id = dest_group_id
        self.dest_ip = dest_ip
        self.security_group_id = security_group_id
        self.security_group_rule_id = security_group_rule_id
        self.created_time = created_time
        self.updated_time = updated_time

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
        if self.source_group_id is not None:
            result['sourceGroupId'] = self.source_group_id
        if self.source_ip is not None:
            result['sourceIp'] = self.source_ip
        if self.dest_group_id is not None:
            result['destGroupId'] = self.dest_group_id
        if self.dest_ip is not None:
            result['destIp'] = self.dest_ip
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.security_group_rule_id is not None:
            result['securityGroupRuleId'] = self.security_group_rule_id
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.updated_time is not None:
            result['updatedTime'] = self.updated_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SecurityGroupRuleModel

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
        if m.get('sourceGroupId') is not None:
            self.source_group_id = m.get('sourceGroupId')
        if m.get('sourceIp') is not None:
            self.source_ip = m.get('sourceIp')
        if m.get('destGroupId') is not None:
            self.dest_group_id = m.get('destGroupId')
        if m.get('destIp') is not None:
            self.dest_ip = m.get('destIp')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('securityGroupRuleId') is not None:
            self.security_group_rule_id = m.get('securityGroupRuleId')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')
        return self
