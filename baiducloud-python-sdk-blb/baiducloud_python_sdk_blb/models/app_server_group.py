"""
AppServerGroup information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_blb.models.app_server_group_port import AppServerGroupPort


class AppServerGroup(AbstractModel):
    """
    AppServerGroup
    """

    def __init__(self, id=None, name=None, desc=None, status=None, preserve_client_ip_enabled=None, port_list=None):
        """
        Initialize AppServerGroup instance.

        :param id: 后端服务器组标识符
        :type id: str (optional)

        :param name: 后端服务器组名称
        :type name: str (optional)

        :param desc: 后端服务器组描述
        :type desc: str (optional)

        :param status: 服务器组状态，详见[blbStatus](#blbStatus)
        :type status: str (optional)

        :param preserve_client_ip_enabled: 是否开启客户端地址保持功能,仅应用型实例支持，应用型IPv6不支持该功能
        :type preserve_client_ip_enabled: bool (optional)

        :param port_list: 服务器组开放的端口列表
        :type port_list: List[AppServerGroupPort] (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.desc = desc
        self.status = status
        self.preserve_client_ip_enabled = preserve_client_ip_enabled
        self.port_list = port_list

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
        if self.name is not None:
            result['name'] = self.name
        if self.desc is not None:
            result['desc'] = self.desc
        if self.status is not None:
            result['status'] = self.status
        if self.preserve_client_ip_enabled is not None:
            result['preserveClientIpEnabled'] = self.preserve_client_ip_enabled
        if self.port_list is not None:
            result['portList'] = [i.to_dict() for i in self.port_list]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AppServerGroup

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('preserveClientIpEnabled') is not None:
            self.preserve_client_ip_enabled = m.get('preserveClientIpEnabled')
        if m.get('portList') is not None:
            self.port_list = [AppServerGroupPort().from_dict(i) for i in m.get('portList')]
        return self
