"""
Parameter information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Parameter(AbstractModel):
    """
    Parameter
    """

    def __init__(self, default=None, force_restart=None, name=None, value=None):
        """
        Initialize Parameter instance.

        :param default: 参数默认值
        :type default: str (optional)

        :param force_restart: 是否需要重启生效：1（重启生效,当前需要提交工单重启）0（无需重启，提交后即生效）
        :type force_restart: int (optional)

        :param name: 参数名称
        :type name: str (optional)

        :param value: 设置参数值
        :type value: str (optional)
        """
        super().__init__()
        self.default = default
        self.force_restart = force_restart
        self.name = name
        self.value = value

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
        if self.default is not None:
            result['default'] = self.default
        if self.force_restart is not None:
            result['forceRestart'] = self.force_restart
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Parameter

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('default') is not None:
            self.default = m.get('default')
        if m.get('forceRestart') is not None:
            self.force_restart = m.get('forceRestart')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self
