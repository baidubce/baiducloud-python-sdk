"""
Category information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Category(AbstractModel):
    """
    Category
    """

    def __init__(self, level_1=None, level_2=None, level_3=None):
        """
        Initialize Category instance.

        :param level_1: 一级概念
        :type level_1: str (optional)

        :param level_2: 二级概念
        :type level_2: str (optional)

        :param level_3: 三级概念
        :type level_3: str (optional)
        """
        super().__init__()
        self.level_1 = level_1
        self.level_2 = level_2
        self.level_3 = level_3

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
        if self.level_1 is not None:
            result['level_1'] = self.level_1
        if self.level_2 is not None:
            result['level_2'] = self.level_2
        if self.level_3 is not None:
            result['level_3'] = self.level_3
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Category

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('level_1') is not None:
            self.level_1 = m.get('level_1')
        if m.get('level_2') is not None:
            self.level_2 = m.get('level_2')
        if m.get('level_3') is not None:
            self.level_3 = m.get('level_3')
        return self
