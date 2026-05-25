"""
Request entity for UpdateCfwRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateCfwRuleRequest(AbstractModel):
    """
    Request entity for UpdateCfwRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        cfw_id,
        cfw_rule_id,
        ip_version=None,
        priority=None,
        protocol=None,
        direction=None,
        source_address=None,
        dest_address=None,
        source_port=None,
        dest_port=None,
        action=None,
        description=None,
    ):
        """
        Initialize UpdateCfwRuleRequest request entity.

        :param cfw_id: cfw_id parameter
        :type cfw_id: str (required)

        :param cfw_rule_id: cfw_rule_id parameter
        :type cfw_rule_id: str (required)

        :param ip_version: IP协议类型，取值 \\[ 4 \\| 6 ]
        :type ip_version: int (optional)

        :param priority: 规则优先级，取值 [ 1-1000 ]
        :type priority: int (optional)

        :param protocol: 协议类型，取值 \\[ TCP \\| UDP \\| ICMP \\| ALL ]
        :type protocol: str (optional)

        :param direction: 方向，取值 \\[ in \\| out ]
        :type direction: str (optional)

        :param source_address: 源IP，0.0.0.0/0表示所有
        :type source_address: str (optional)

        :param dest_address: 目的IP，0.0.0.0/0表示所有
        :type dest_address: str (optional)

        :param source_port: 源端口，0-65535表示所有
        :type source_port: str (optional)

        :param dest_port: 目的端口，0-65535表示所有
        :type dest_port: str (optional)

        :param action: 策略，取值 \\[ allow \\| deny ]
        :type action: str (optional)

        :param description: CFW规则的描述
        :type description: str (optional)
        """
        super().__init__()
        self.cfw_id = cfw_id
        self.cfw_rule_id = cfw_rule_id
        self.ip_version = ip_version
        self.priority = priority
        self.protocol = protocol
        self.direction = direction
        self.source_address = source_address
        self.dest_address = dest_address
        self.source_port = source_port
        self.dest_port = dest_port
        self.action = action
        self.description = description

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
        if self.ip_version is not None:
            result['ipVersion'] = self.ip_version
        if self.priority is not None:
            result['priority'] = self.priority
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.direction is not None:
            result['direction'] = self.direction
        if self.source_address is not None:
            result['sourceAddress'] = self.source_address
        if self.dest_address is not None:
            result['destAddress'] = self.dest_address
        if self.source_port is not None:
            result['sourcePort'] = self.source_port
        if self.dest_port is not None:
            result['destPort'] = self.dest_port
        if self.action is not None:
            result['action'] = self.action
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateCfwRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cfwId') is not None:
            self.cfw_id = m.get('cfwId')
        if m.get('cfwRuleId') is not None:
            self.cfw_rule_id = m.get('cfwRuleId')
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('sourceAddress') is not None:
            self.source_address = m.get('sourceAddress')
        if m.get('destAddress') is not None:
            self.dest_address = m.get('destAddress')
        if m.get('sourcePort') is not None:
            self.source_port = m.get('sourcePort')
        if m.get('destPort') is not None:
            self.dest_port = m.get('destPort')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
