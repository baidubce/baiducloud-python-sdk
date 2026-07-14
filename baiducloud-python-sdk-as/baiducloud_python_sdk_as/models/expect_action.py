"""
ExpectAction information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ExpectAction(AbstractModel):
    """
    ExpectAction
    """

    def __init__(self, action_type=None, action_num=None, adjust_to_num=None):
        """
        Initialize ExpectAction instance.

        :param action_type: 动作类型。包括：INCREASE(扩容),DECREASE(缩容),ADJUST(调整至)
        :type action_type: str (optional)

        :param action_num: 动作数量
        :type action_num: int (optional)

        :param adjust_to_num: 调整到的数量
        :type adjust_to_num: int (optional)
        """
        super().__init__()
        self.action_type = action_type
        self.action_num = action_num
        self.adjust_to_num = adjust_to_num

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
        if self.action_type is not None:
            result['actionType'] = self.action_type
        if self.action_num is not None:
            result['actionNum'] = self.action_num
        if self.adjust_to_num is not None:
            result['adjustToNum'] = self.adjust_to_num
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ExpectAction

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('actionType') is not None:
            self.action_type = m.get('actionType')
        if m.get('actionNum') is not None:
            self.action_num = m.get('actionNum')
        if m.get('adjustToNum') is not None:
            self.adjust_to_num = m.get('adjustToNum')
        return self
