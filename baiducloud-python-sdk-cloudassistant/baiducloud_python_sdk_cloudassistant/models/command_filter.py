"""
CommandFilter information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CommandFilter(AbstractModel):
    """
    CommandFilter
    """

    def __init__(self, scope=None, name=None, type=None):
        """
        Initialize CommandFilter instance.

        :param scope: 按命令可见范围筛选。枚举值：INDIVIDUAL（个人命令），GLOBAL（公共命令）
        :type scope: str (optional)

        :param name: 按命令名称筛选
        :type name: str (optional)

        :param type: 按命令类型筛选。枚举值：SHELL，POWERSHELL
        :type type: str (optional)
        """
        super().__init__()
        self.scope = scope
        self.name = name
        self.type = type

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
        if self.scope is not None:
            result['scope'] = self.scope
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CommandFilter

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self
