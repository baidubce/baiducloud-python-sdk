"""
Request entity for UpdateRegularSecurityGroupRulesV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateRegularSecurityGroupRulesV2Request(AbstractModel):
    """
    Request entity for UpdateRegularSecurityGroupRulesV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        security_group_rule_id,
        client_token=None,
        sg_version=None,
        remark=None,
        port_range=None,
        source_ip=None,
        source_group_id=None,
        dest_ip=None,
        dest_group_id=None,
        protocol=None,
    ):
        """
        Initialize UpdateRegularSecurityGroupRulesV2Request request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param sg_version: sg_version parameter
        :type sg_version: int (optional)

        :param security_group_rule_id: 安全组规则ID
        :type security_group_rule_id: str (required)

        :param remark: 描述
        :type remark: str (optional)

        :param port_range: 端口范围
        :type port_range: str (optional)

        :param source_ip: 入站规则Ip，与sourceGroupId不可同时存在
        :type source_ip: str (optional)

        :param source_group_id: 入站规则安全组ID，与sourceIp不可同时存在
        :type source_group_id: str (optional)

        :param dest_ip: 出站规则Ip，与destGroupId不可同时存在
        :type dest_ip: str (optional)

        :param dest_group_id: 出站规则安全组ID，与destIp不可同时存在
        :type dest_group_id: str (optional)

        :param protocol: 协议，暂不支持tcp/udp转icmp
        :type protocol: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.sg_version = sg_version
        self.security_group_rule_id = security_group_rule_id
        self.remark = remark
        self.port_range = port_range
        self.source_ip = source_ip
        self.source_group_id = source_group_id
        self.dest_ip = dest_ip
        self.dest_group_id = dest_group_id
        self.protocol = protocol

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
        if self.security_group_rule_id is not None:
            result['securityGroupRuleId'] = self.security_group_rule_id
        if self.remark is not None:
            result['remark'] = self.remark
        if self.port_range is not None:
            result['portRange'] = self.port_range
        if self.source_ip is not None:
            result['sourceIp'] = self.source_ip
        if self.source_group_id is not None:
            result['sourceGroupId'] = self.source_group_id
        if self.dest_ip is not None:
            result['destIp'] = self.dest_ip
        if self.dest_group_id is not None:
            result['destGroupId'] = self.dest_group_id
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateRegularSecurityGroupRulesV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('sgVersion') is not None:
            self.sg_version = m.get('sgVersion')
        if m.get('securityGroupRuleId') is not None:
            self.security_group_rule_id = m.get('securityGroupRuleId')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('portRange') is not None:
            self.port_range = m.get('portRange')
        if m.get('sourceIp') is not None:
            self.source_ip = m.get('sourceIp')
        if m.get('sourceGroupId') is not None:
            self.source_group_id = m.get('sourceGroupId')
        if m.get('destIp') is not None:
            self.dest_ip = m.get('destIp')
        if m.get('destGroupId') is not None:
            self.dest_group_id = m.get('destGroupId')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self
