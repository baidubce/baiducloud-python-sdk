"""
ClaimCondition information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ClaimCondition(AbstractModel):
    """
    ClaimCondition
    """

    def __init__(self, condition=None):
        """
        Initialize ClaimCondition instance.

        :param condition: 认领后多久未恢复
        :type condition: int (optional)
        """
        super().__init__()
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
        :rtype: ClaimCondition

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        return self
