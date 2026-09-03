"""
CarLocationResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CarLocationResult(AbstractModel):
    """
    CarLocationResult
    """

    def __init__(self, width=None, height=None, left=None, top=None):
        """
        Initialize CarLocationResult instance.

        :param width: 车辆区域的宽度
        :type width: float (optional)

        :param height: 车辆区域的高度
        :type height: float (optional)

        :param left: 车辆区域离左边界的距离
        :type left: float (optional)

        :param top: 车辆区域离上边界的距离
        :type top: float (optional)
        """
        super().__init__()
        self.width = width
        self.height = height
        self.left = left
        self.top = top

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
        if self.width is not None:
            result['width'] = self.width
        if self.height is not None:
            result['height'] = self.height
        if self.left is not None:
            result['left'] = self.left
        if self.top is not None:
            result['top'] = self.top
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CarLocationResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('width') is not None:
            self.width = m.get('width')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('left') is not None:
            self.left = m.get('left')
        if m.get('top') is not None:
            self.top = m.get('top')
        return self
