"""
NamespaceSelector information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class NamespaceSelector(AbstractModel):
    """
    NamespaceSelector
    """

    def __init__(self, match_names=None):
        """
        Initialize NamespaceSelector instance.

        :param match_names: 命名空间列表
        :type match_names: List[str] (optional)
        """
        super().__init__()
        self.match_names = match_names

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
        if self.match_names is not None:
            result['matchNames'] = self.match_names
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: NamespaceSelector

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('matchNames') is not None:
            self.match_names = m.get('matchNames')
        return self
