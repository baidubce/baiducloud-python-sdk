"""
Capabilities information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Capabilities(AbstractModel):
    """
    Capabilities
    """

    def __init__(self, add=None, drop=None):
        """
        Initialize Capabilities instance.

        :param add: 启用安全能力项列表
        :type add: List[str] (optional)

        :param drop: 禁用安全能力项列表
        :type drop: List[str] (optional)
        """
        super().__init__()
        self.add = add
        self.drop = drop

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
        if self.add is not None:
            result['add'] = self.add
        if self.drop is not None:
            result['drop'] = self.drop
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Capabilities

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('add') is not None:
            self.add = m.get('add')
        if m.get('drop') is not None:
            self.drop = m.get('drop')
        return self
