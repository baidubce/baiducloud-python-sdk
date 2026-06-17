"""
Request entity for GetStatelessCfwResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetStatelessCfwResponse(BceResponse):
    """
    GetStatelessCfwResponse
    """

    def __init__(
        self,
        cfw_id=None,
        name=None,
        description=None,
        created_time=None,
        bind_instance_num=None,
        type=None,
        border=None,
        default_action=None,
        protocol=None,
        ip_list=None,
    ):
        """
        Initialize GetStatelessCfwResponse response.

        :param cfw_id: CFW的id
        :type cfw_id: str (optional)

        :param name: CFW的名称
        :type name: str (optional)

        :param description: CFW的描述
        :type description: str (optional)

        :param created_time: CFW的创建时间，标准UTC时间
        :type created_time: date (optional)

        :param bind_instance_num: CFW绑定实例的数量
        :type bind_instance_num: int (optional)

        :param type: CFW类型，0表示网络型防火墙
        :type type: int (optional)

        :param border: CFW防护边界，取值1，表示vpc边界
        :type border: int (optional)

        :param default_action: 无状态防火墙默认策略，白名单模式取值deny、黑名单模式取值allow
        :type default_action: str (optional)

        :param protocol: 无状态防火墙协议，取值 [ TCP
        :type protocol: str (optional)

        :param ip_list: 无状态防火墙IP列表
        :type ip_list: List[str] (optional)
        """
        super().__init__()
        self.cfw_id = cfw_id
        self.name = name
        self.description = description
        self.created_time = created_time
        self.bind_instance_num = bind_instance_num
        self.type = type
        self.border = border
        self.default_action = default_action
        self.protocol = protocol
        self.ip_list = ip_list

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.cfw_id is not None:
            result['cfwId'] = self.cfw_id
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.bind_instance_num is not None:
            result['bindInstanceNum'] = self.bind_instance_num
        if self.type is not None:
            result['type'] = self.type
        if self.border is not None:
            result['border'] = self.border
        if self.default_action is not None:
            result['defaultAction'] = self.default_action
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.ip_list is not None:
            result['ipList'] = self.ip_list
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetStatelessCfwResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cfwId') is not None:
            self.cfw_id = m.get('cfwId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('bindInstanceNum') is not None:
            self.bind_instance_num = m.get('bindInstanceNum')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('border') is not None:
            self.border = m.get('border')
        if m.get('defaultAction') is not None:
            self.default_action = m.get('defaultAction')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('ipList') is not None:
            self.ip_list = m.get('ipList')
        return self
