"""
TargetInstance information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcm.models.dimension import Dimension


class TargetInstance(AbstractModel):
    """
    TargetInstance
    """

    def __init__(self, dimensions=None):
        """
        Initialize TargetInstance instance.

        :param dimensions: 实例维度键值对列表
        :type dimensions: List[Dimension] (optional)
        """
        super().__init__()
        self.dimensions = dimensions

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
        if self.dimensions is not None:
            result['dimensions'] = [i.to_dict() for i in self.dimensions]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TargetInstance

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('dimensions') is not None:
            self.dimensions = [Dimension().from_dict(i) for i in m.get('dimensions')]
        return self
