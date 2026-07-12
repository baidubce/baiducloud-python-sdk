"""
Category information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Category(AbstractModel):
    """
    Category
    """

    def __init__(self, name=None, sequence=None):
        """
        Initialize Category instance.

        :param name: 分类名
        :type name: str (optional)

        :param sequence: 排序序号
        :type sequence: int (optional)
        """
        super().__init__()
        self.name = name
        self.sequence = sequence

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
        if self.name is not None:
            result['name'] = self.name
        if self.sequence is not None:
            result['sequence'] = self.sequence
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
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sequence') is not None:
            self.sequence = m.get('sequence')
        return self
