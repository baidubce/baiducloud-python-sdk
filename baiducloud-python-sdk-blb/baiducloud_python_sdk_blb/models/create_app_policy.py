"""
CreateAppPolicy information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_blb.models.create_app_rule import CreateAppRule


class CreateAppPolicy(AbstractModel):
    """
    CreateAppPolicy
    """

    def __init__(
        self,
        app_server_group_id=None,
        app_ip_group_id=None,
        backend_port=None,
        port_type=None,
        priority=None,
        rule_list=None,
        desc=None,
    ):
        """
        Initialize CreateAppPolicy instance.

        :param app_server_group_id: 策略绑定服务器组标识符，当绑定的目标组类型为服务器组时该字段必传
        :type app_server_group_id: str (optional)

        :param app_ip_group_id: 策略绑定IP组标识符，当绑定的目标组类型为IP组时该字段必传
        :type app_ip_group_id: str (optional)

        :param backend_port: backend_port attribute
        :type backend_port: int (optional)

        :param port_type: 目标端口类型，当目标组是服务器组时默认为目标端口号所使用的协议
        :type port_type: str (optional)

        :param priority: 策略优先级，有效取值范围是1-32768
        :type priority: int (optional)

        :param rule_list: 策略规则列表
        :type rule_list: List[CreateAppRule] (optional)

        :param desc: 策略描述默认为空
        :type desc: str (optional)
        """
        super().__init__()
        self.app_server_group_id = app_server_group_id
        self.app_ip_group_id = app_ip_group_id
        self.backend_port = backend_port
        self.port_type = port_type
        self.priority = priority
        self.rule_list = rule_list
        self.desc = desc

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
        if self.app_server_group_id is not None:
            result['appServerGroupId'] = self.app_server_group_id
        if self.app_ip_group_id is not None:
            result['appIpGroupId'] = self.app_ip_group_id
        if self.backend_port is not None:
            result['backendPort'] = self.backend_port
        if self.port_type is not None:
            result['portType'] = self.port_type
        if self.priority is not None:
            result['priority'] = self.priority
        if self.rule_list is not None:
            result['ruleList'] = [i.to_dict() for i in self.rule_list]
        if self.desc is not None:
            result['desc'] = self.desc
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAppPolicy

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('appServerGroupId') is not None:
            self.app_server_group_id = m.get('appServerGroupId')
        if m.get('appIpGroupId') is not None:
            self.app_ip_group_id = m.get('appIpGroupId')
        if m.get('backendPort') is not None:
            self.backend_port = m.get('backendPort')
        if m.get('portType') is not None:
            self.port_type = m.get('portType')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('ruleList') is not None:
            self.rule_list = [CreateAppRule().from_dict(i) for i in m.get('ruleList')]
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        return self
