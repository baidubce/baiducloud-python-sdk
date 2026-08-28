"""
WebImageLocLocation information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class WebImageLocLocation(AbstractModel):
    """
    WebImageLocLocation
    """

    def __init__(self, left=None, top=None, width=None, height=None):
        """
        Initialize WebImageLocLocation instance.

        :param left: 表示定位位置的长方形左上顶点的水平坐标
        :type left: int (optional)

        :param top: 表示定位位置的长方形左上顶点的垂直坐标
        :type top: int (optional)

        :param width: 表示定位位置的长方形的宽度
        :type width: int (optional)

        :param height: 表示定位位置的长方形的高度
        :type height: int (optional)
        """
        super().__init__()
        self.left = left
        self.top = top
        self.width = width
        self.height = height

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
        if self.left is not None:
            result['left'] = self.left
        if self.top is not None:
            result['top'] = self.top
        if self.width is not None:
            result['width'] = self.width
        if self.height is not None:
            result['height'] = self.height
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: WebImageLocLocation

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('left') is not None:
            self.left = m.get('left')
        if m.get('top') is not None:
            self.top = m.get('top')
        if m.get('width') is not None:
            self.width = m.get('width')
        if m.get('height') is not None:
            self.height = m.get('height')
        return self
