"""
AppPolicy information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_blb.models.app_rule import AppRule


class AppPolicy(AbstractModel):
    """
    AppPolicy
    """

    def __init__(
        self,
        id=None,
        desc=None,
        app_server_group_id=None,
        app_server_group_name=None,
        app_ip_group_id=None,
        app_ip_group_name=None,
        frontend_port=None,
        type=None,
        backend_port=None,
        port_type=None,
        priority=None,
        rule_list=None,
        group_type=None,
    ):
        """
        Initialize AppPolicy instance.

        :param id: 策略标识符
        :type id: str (optional)

        :param desc: 策略描述默认为空
        :type desc: str (optional)

        :param app_server_group_id: 策略绑定服务器组标识符
        :type app_server_group_id: str (optional)

        :param app_server_group_name: 策略绑定服务器组名称
        :type app_server_group_name: str (optional)

        :param app_ip_group_id: 策略绑定IP组标识符
        :type app_ip_group_id: str (optional)

        :param app_ip_group_name: 策略绑定IP组名称
        :type app_ip_group_name: str (optional)

        :param frontend_port: 前端服务器的监听端口
        :type frontend_port: int (optional)

        :param type: 前端服务器的监听端口协议
        :type type: str (optional)

        :param backend_port: backend_port attribute
        :type backend_port: int (optional)

        :param port_type: 端口类型
        :type port_type: str (optional)

        :param priority: 策略优先级，有效取值范围是1-32768
        :type priority: int (optional)

        :param rule_list: 策略规则列表
        :type rule_list: List[AppRule] (optional)

        :param group_type: \"Server\" 表示后端绑定的是服务器组，“IP” 表示后端绑定的是IP组
        :type group_type: str (optional)
        """
        super().__init__()
        self.id = id
        self.desc = desc
        self.app_server_group_id = app_server_group_id
        self.app_server_group_name = app_server_group_name
        self.app_ip_group_id = app_ip_group_id
        self.app_ip_group_name = app_ip_group_name
        self.frontend_port = frontend_port
        self.type = type
        self.backend_port = backend_port
        self.port_type = port_type
        self.priority = priority
        self.rule_list = rule_list
        self.group_type = group_type

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
        if self.desc is not None:
            result['desc'] = self.desc
        if self.app_server_group_id is not None:
            result['appServerGroupId'] = self.app_server_group_id
        if self.app_server_group_name is not None:
            result['appServerGroupName'] = self.app_server_group_name
        if self.app_ip_group_id is not None:
            result['appIpGroupId'] = self.app_ip_group_id
        if self.app_ip_group_name is not None:
            result['appIpGroupName'] = self.app_ip_group_name
        if self.frontend_port is not None:
            result['frontendPort'] = self.frontend_port
        if self.type is not None:
            result['type'] = self.type
        if self.backend_port is not None:
            result['backendPort'] = self.backend_port
        if self.port_type is not None:
            result['portType'] = self.port_type
        if self.priority is not None:
            result['priority'] = self.priority
        if self.rule_list is not None:
            result['ruleList'] = [i.to_dict() for i in self.rule_list]
        if self.group_type is not None:
            result['groupType'] = self.group_type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AppPolicy

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('appServerGroupId') is not None:
            self.app_server_group_id = m.get('appServerGroupId')
        if m.get('appServerGroupName') is not None:
            self.app_server_group_name = m.get('appServerGroupName')
        if m.get('appIpGroupId') is not None:
            self.app_ip_group_id = m.get('appIpGroupId')
        if m.get('appIpGroupName') is not None:
            self.app_ip_group_name = m.get('appIpGroupName')
        if m.get('frontendPort') is not None:
            self.frontend_port = m.get('frontendPort')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('backendPort') is not None:
            self.backend_port = m.get('backendPort')
        if m.get('portType') is not None:
            self.port_type = m.get('portType')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('ruleList') is not None:
            self.rule_list = [AppRule().from_dict(i) for i in m.get('ruleList')]
        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')
        return self
