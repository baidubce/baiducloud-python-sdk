"""
Request entity for GetCfwResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_cfw.models.cfw_rule import CfwRule


class GetCfwResponse(BceResponse):
    """
    GetCfwResponse
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
        cfw_rules=None,
    ):
        """
        Initialize GetCfwResponse response.

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

        :param type: CFW类型，1表示应用型防火墙
        :type type: int (optional)

        :param border: CFW防护边界，取值\\[ 0 \\| 1 \\| 2 \\]，分别表示互联网边界、vpc边界、nat边界
        :type border: int (optional)

        :param cfw_rules: CFW规则
        :type cfw_rules: List[CfwRule] (optional)
        """
        super().__init__()
        self.cfw_id = cfw_id
        self.name = name
        self.description = description
        self.created_time = created_time
        self.bind_instance_num = bind_instance_num
        self.type = type
        self.border = border
        self.cfw_rules = cfw_rules

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
        if self.cfw_rules is not None:
            result['cfwRules'] = [i.to_dict() for i in self.cfw_rules]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetCfwResponse

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
        if m.get('cfwRules') is not None:
            self.cfw_rules = [CfwRule().from_dict(i) for i in m.get('cfwRules')]
        return self
