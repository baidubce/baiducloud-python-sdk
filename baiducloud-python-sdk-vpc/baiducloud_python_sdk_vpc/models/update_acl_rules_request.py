"""
Request entity for UpdateAclRulesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateAclRulesRequest(AbstractModel):
    """
    Request entity for UpdateAclRulesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        acl_rule_id,
        client_token=None,
        description=None,
        protocol=None,
        source_ip_address=None,
        destination_ip_address=None,
        source_port=None,
        destination_port=None,
        position=None,
        action=None,
    ):
        """
        Initialize UpdateAclRulesRequest request entity.

        :param acl_rule_id: acl_rule_id parameter
        :type acl_rule_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param description: 备注
        :type description: str (optional)

        :param protocol: 协议，包括all/tcp/udp/icmp
        :type protocol: str (optional)

        :param source_ip_address: 源IP
        :type source_ip_address: str (optional)

        :param destination_ip_address: 目的IP
        :type destination_ip_address: str (optional)

        :param source_port: 源端口
        :type source_port: str (optional)

        :param destination_port: 目的端口
        :type destination_port: str (optional)

        :param position: 优先级 1-5000且不能与已有条目重复；数值越小，优先级越高，规则匹配顺序为按优先级由高到低匹配
        :type position: int (optional)

        :param action: 策略，包括allow和deny
        :type action: str (optional)
        """
        super().__init__()
        self.acl_rule_id = acl_rule_id
        self.client_token = client_token
        self.description = description
        self.protocol = protocol
        self.source_ip_address = source_ip_address
        self.destination_ip_address = destination_ip_address
        self.source_port = source_port
        self.destination_port = destination_port
        self.position = position
        self.action = action

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
        if self.description is not None:
            result['description'] = self.description
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.source_ip_address is not None:
            result['sourceIpAddress'] = self.source_ip_address
        if self.destination_ip_address is not None:
            result['destinationIpAddress'] = self.destination_ip_address
        if self.source_port is not None:
            result['sourcePort'] = self.source_port
        if self.destination_port is not None:
            result['destinationPort'] = self.destination_port
        if self.position is not None:
            result['position'] = self.position
        if self.action is not None:
            result['action'] = self.action
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateAclRulesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('aclRuleId') is not None:
            self.acl_rule_id = m.get('aclRuleId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('sourceIpAddress') is not None:
            self.source_ip_address = m.get('sourceIpAddress')
        if m.get('destinationIpAddress') is not None:
            self.destination_ip_address = m.get('destinationIpAddress')
        if m.get('sourcePort') is not None:
            self.source_port = m.get('sourcePort')
        if m.get('destinationPort') is not None:
            self.destination_port = m.get('destinationPort')
        if m.get('position') is not None:
            self.position = m.get('position')
        if m.get('action') is not None:
            self.action = m.get('action')
        return self
