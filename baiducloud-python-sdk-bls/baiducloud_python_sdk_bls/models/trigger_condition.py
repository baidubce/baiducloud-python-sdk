"""
TriggerCondition information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TriggerCondition(AbstractModel):
    """
    TriggerCondition
    """

    def __init__(self, level=None, condition=None):
        """
        Initialize TriggerCondition instance.

        :param level: 报警等级，可选项：INFO、WARN、CRITICAL
        :type level: str (optional)

        :param condition: 触发条件表达式
        :type condition: str (optional)
        """
        super().__init__()
        self.level = level
        self.condition = condition

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
        if self.level is not None:
            result['level'] = self.level
        if self.condition is not None:
            result['condition'] = self.condition
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TriggerCondition

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        return self
