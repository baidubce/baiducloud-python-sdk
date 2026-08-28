"""
Area information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Area(AbstractModel):
    """
    Area
    """

    def __init__(self, left_x=None, left_y=None, right_x=None, right_y=None):
        """
        Initialize Area instance.

        :param left_x: 左上角X坐标
        :type left_x: int (optional)

        :param left_y: 左上角Y坐标
        :type left_y: int (optional)

        :param right_x: 右下角X坐标
        :type right_x: int (optional)

        :param right_y: 右下角Y坐标
        :type right_y: int (optional)
        """
        super().__init__()
        self.left_x = left_x
        self.left_y = left_y
        self.right_x = right_x
        self.right_y = right_y

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
        if self.left_x is not None:
            result['left_x'] = self.left_x
        if self.left_y is not None:
            result['left_y'] = self.left_y
        if self.right_x is not None:
            result['right_x'] = self.right_x
        if self.right_y is not None:
            result['right_y'] = self.right_y
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Area

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('left_x') is not None:
            self.left_x = m.get('left_x')
        if m.get('left_y') is not None:
            self.left_y = m.get('left_y')
        if m.get('right_x') is not None:
            self.right_x = m.get('right_x')
        if m.get('right_y') is not None:
            self.right_y = m.get('right_y')
        return self
