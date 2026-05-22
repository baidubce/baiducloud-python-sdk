"""
Request entity for UpdateEnterpriseSecurityGroupRulesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateEnterpriseSecurityGroupRulesRequest(AbstractModel):
    """
    Request entity for UpdateEnterpriseSecurityGroupRulesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        enterprise_security_group_rule_id,
        client_token=None,
        remark=None,
        port_range=None,
        source_port_range=None,
        source_ip=None,
        dest_ip=None,
        local_ip=None,
        remote_ip_set=None,
        remote_ip_group=None,
        action=None,
        priority=None,
        protocol=None,
    ):
        """
        Initialize UpdateEnterpriseSecurityGroupRulesRequest request entity.

        :param enterprise_security_group_rule_id: enterprise_security_group_rule_id parameter
        :type enterprise_security_group_rule_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param remark: 描述
        :type remark: str (optional)

        :param port_range: 目的端口范围
        :type port_range: str (optional)

        :param source_port_range: 源端口范围
        :type source_port_range: str (optional)

        :param source_ip: 入站规则源IP，仅入站规则使用，与remoteIpSet、remoteIpGroup三者选一
        :type source_ip: str (optional)

        :param dest_ip: 出站规则目的IP，仅出站规则使用，与remoteIpSet、remoteIpGroup三者选一
        :type dest_ip: str (optional)

        :param local_ip: 本端IP
        :type local_ip: str (optional)

        :param remote_ip_set: 远端IP地址组，与sourceIp(destIp)、 remoteIpGroup三者选一
        :type remote_ip_set: str (optional)

        :param remote_ip_group: 远端IP地址族，与sourceIp(destIp)、 remoteIpSet三者选一
        :type remote_ip_group: str (optional)

        :param action: 允许/拒绝，取值allow或deny
        :type action: str (optional)

        :param priority: 优先级
        :type priority: int (optional)

        :param protocol: 协议，取值all、tcp、udp或icmp
        :type protocol: str (optional)
        """
        super().__init__()
        self.enterprise_security_group_rule_id = enterprise_security_group_rule_id
        self.client_token = client_token
        self.remark = remark
        self.port_range = port_range
        self.source_port_range = source_port_range
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.local_ip = local_ip
        self.remote_ip_set = remote_ip_set
        self.remote_ip_group = remote_ip_group
        self.action = action
        self.priority = priority
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
        if self.remark is not None:
            result['remark'] = self.remark
        if self.port_range is not None:
            result['portRange'] = self.port_range
        if self.source_port_range is not None:
            result['sourcePortRange'] = self.source_port_range
        if self.source_ip is not None:
            result['sourceIp'] = self.source_ip
        if self.dest_ip is not None:
            result['destIp'] = self.dest_ip
        if self.local_ip is not None:
            result['localIp'] = self.local_ip
        if self.remote_ip_set is not None:
            result['remoteIpSet'] = self.remote_ip_set
        if self.remote_ip_group is not None:
            result['remoteIpGroup'] = self.remote_ip_group
        if self.action is not None:
            result['action'] = self.action
        if self.priority is not None:
            result['priority'] = self.priority
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
        :rtype: UpdateEnterpriseSecurityGroupRulesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('enterpriseSecurityGroupRuleId') is not None:
            self.enterprise_security_group_rule_id = m.get('enterpriseSecurityGroupRuleId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('portRange') is not None:
            self.port_range = m.get('portRange')
        if m.get('sourcePortRange') is not None:
            self.source_port_range = m.get('sourcePortRange')
        if m.get('sourceIp') is not None:
            self.source_ip = m.get('sourceIp')
        if m.get('destIp') is not None:
            self.dest_ip = m.get('destIp')
        if m.get('localIp') is not None:
            self.local_ip = m.get('localIp')
        if m.get('remoteIpSet') is not None:
            self.remote_ip_set = m.get('remoteIpSet')
        if m.get('remoteIpGroup') is not None:
            self.remote_ip_group = m.get('remoteIpGroup')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self
