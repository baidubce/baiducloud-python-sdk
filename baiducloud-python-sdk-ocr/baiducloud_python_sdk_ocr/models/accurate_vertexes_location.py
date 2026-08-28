"""
AccurateVertexesLocation information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AccurateVertexesLocation(AbstractModel):
    """
    AccurateVertexesLocation
    """

    def __init__(self, x=None, y=None):
        """
        Initialize AccurateVertexesLocation instance.

        :param x: 水平坐标（坐标0点为左上角）
        :type x: int (optional)

        :param y: 垂直坐标（坐标0点为左上角）
        :type y: int (optional)
        """
        super().__init__()
        self.x = x
        self.y = y

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
        if self.x is not None:
            result['x'] = self.x
        if self.y is not None:
            result['y'] = self.y
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AccurateVertexesLocation

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('x') is not None:
            self.x = m.get('x')
        if m.get('y') is not None:
            self.y = m.get('y')
        return self
