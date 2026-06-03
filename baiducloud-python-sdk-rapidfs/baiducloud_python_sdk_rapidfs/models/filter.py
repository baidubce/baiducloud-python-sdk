"""
Filter information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Filter(AbstractModel):
    """
    Filter
    """

    def __init__(self, name=None, values=None):
        """
        Initialize Filter instance.

        :param name: 需要过滤的字段，多组 filter 之间为条件与关系。例如 zone
        :type name: str (optional)

        :param values: 字段的过滤值，多个 values 之间为逻辑或关系。例如：[\"zoneA\", \"zoneB\"]
        :type values: List[str] (optional)
        """
        super().__init__()
        self.name = name
        self.values = values

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
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Filter

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self
