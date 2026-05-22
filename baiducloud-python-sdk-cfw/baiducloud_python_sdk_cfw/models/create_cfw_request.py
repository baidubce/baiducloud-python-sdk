"""
Request entity for CreateCfwRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_cfw.models.create_rule import CreateRule


class CreateCfwRequest(AbstractModel):
    """
    Request entity for CreateCfwRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, type, border=None, description=None, cfw_rules=None):
        """
        Initialize CreateCfwRequest request entity.

        :param name: CFW名称，长度不超过65个字符，可由数字、字符、下划线组成
        :type name: str (required)

        :param type: CFW类型，取值1，表示有状态防火墙
        :type type: int (required)

        :param border: CFW防护边界，取值0、1、2，分别表示互联网边界、vpc边界、nat边界，有状态防火墙默认为互联网边界
        :type border: int (optional)

        :param description: CFW描述，不超过200字符
        :type description: str (optional)

        :param cfw_rules: CFW规则
        :type cfw_rules: List[CreateRule] (optional)
        """
        super().__init__()
        self.name = name
        self.type = type
        self.border = border
        self.description = description
        self.cfw_rules = cfw_rules

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
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.border is not None:
            result['border'] = self.border
        if self.description is not None:
            result['description'] = self.description
        if self.cfw_rules is not None:
            result['cfwRules'] = [i.to_dict() for i in self.cfw_rules]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateCfwRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('border') is not None:
            self.border = m.get('border')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('cfwRules') is not None:
            self.cfw_rules = [CreateRule().from_dict(i) for i in m.get('cfwRules')]
        return self
