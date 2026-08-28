"""
HandwritingGetBBox information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class HandwritingGetBBox(AbstractModel):
    """
    HandwritingGetBBox
    """

    def __init__(self, x=None, y=None, w=None, h=None):
        """
        Initialize HandwritingGetBBox instance.

        :param x: X坐标
        :type x: int (optional)

        :param y: Y坐标
        :type y: int (optional)

        :param w: 宽度
        :type w: int (optional)

        :param h: 高度
        :type h: int (optional)
        """
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h

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
        if self.w is not None:
            result['w'] = self.w
        if self.h is not None:
            result['h'] = self.h
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HandwritingGetBBox

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('x') is not None:
            self.x = m.get('x')
        if m.get('y') is not None:
            self.y = m.get('y')
        if m.get('w') is not None:
            self.w = m.get('w')
        if m.get('h') is not None:
            self.h = m.get('h')
        return self
