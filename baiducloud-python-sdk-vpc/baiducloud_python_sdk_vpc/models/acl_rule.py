"""
AclRule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AclRule(AbstractModel):
    """
    AclRule
    """

    def __init__(
        self,
        id=None,
        subnet_id=None,
        description=None,
        protocol=None,
        source_ip_address=None,
        destination_ip_address=None,
        source_port=None,
        destination_port=None,
        position=None,
        direction=None,
        ip_version=None,
        action=None,
    ):
        """
        Initialize AclRule instance.

        :param id: ACL规则ID
        :type id: str (optional)

        :param subnet_id: 子网的ID
        :type subnet_id: str (optional)

        :param description: 备注
        :type description: str (optional)

        :param protocol: 协议，包括all tcp udp icmp
        :type protocol: str (optional)

        :param source_ip_address: 源IP,可以为all
        :type source_ip_address: str (optional)

        :param destination_ip_address: 目的IP,可以为all
        :type destination_ip_address: str (optional)

        :param source_port: 源端口,例如1-65535，或8080
        :type source_port: str (optional)

        :param destination_port: 目的端口,例如1-65535，或8080
        :type destination_port: str (optional)

        :param position: 优先级 1-32768且不能与已有条目重复。数值越小，优先级越高，规则匹配顺序为按优先级由高到低匹配
        :type position: str (optional)

        :param direction: 规则的入站ingress 规则的出站egress
        :type direction: str (optional)

        :param ip_version: acl规则的版本。4表示IPv4 6表示IPv6
        :type ip_version: int (optional)

        :param action: 策略，包括allow和deny
        :type action: str (optional)
        """
        super().__init__()
        self.id = id
        self.subnet_id = subnet_id
        self.description = description
        self.protocol = protocol
        self.source_ip_address = source_ip_address
        self.destination_ip_address = destination_ip_address
        self.source_port = source_port
        self.destination_port = destination_port
        self.position = position
        self.direction = direction
        self.ip_version = ip_version
        self.action = action

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
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
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
        if self.direction is not None:
            result['direction'] = self.direction
        if self.ip_version is not None:
            result['ipVersion'] = self.ip_version
        if self.action is not None:
            result['action'] = self.action
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AclRule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
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
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        if m.get('action') is not None:
            self.action = m.get('action')
        return self
