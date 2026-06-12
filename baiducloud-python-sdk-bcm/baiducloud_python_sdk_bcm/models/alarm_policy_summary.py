"""
AlarmPolicySummary information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AlarmPolicySummary(AbstractModel):
    """
    AlarmPolicySummary
    """

    def __init__(self, id=None, name=None, content=None, level=None):
        """
        Initialize AlarmPolicySummary instance.

        :param id: 策略ID
        :type id: str (optional)

        :param name: 策略名称
        :type name: str (optional)

        :param content: 策略内容描述，当locale=en时返回英文内容
        :type content: str (optional)

        :param level: 报警级别，可选值：NOTICE / WARNING / MAJOR / CRITICAL
        :type level: str (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.content = content
        self.level = level

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
        if self.content is not None:
            result['content'] = self.content
        if self.level is not None:
            result['level'] = self.level
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AlarmPolicySummary

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('level') is not None:
            self.level = m.get('level')
        return self
