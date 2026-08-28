"""
Points information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Points(AbstractModel):
    """
    Points
    """

    def __init__(self, start_x=None, start_y=None, end_x=None, end_y=None):
        """
        Initialize Points instance.

        :param start_x: 下划线起点x坐标
        :type start_x: int (optional)

        :param start_y: 下划线起点y坐标
        :type start_y: int (optional)

        :param end_x: 下划线终点x坐标
        :type end_x: int (optional)

        :param end_y: 下划线终点y坐标
        :type end_y: int (optional)
        """
        super().__init__()
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y

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
        if self.start_x is not None:
            result['start_x'] = self.start_x
        if self.start_y is not None:
            result['start_y'] = self.start_y
        if self.end_x is not None:
            result['end_x'] = self.end_x
        if self.end_y is not None:
            result['end_y'] = self.end_y
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Points

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('start_x') is not None:
            self.start_x = m.get('start_x')
        if m.get('start_y') is not None:
            self.start_y = m.get('start_y')
        if m.get('end_x') is not None:
            self.end_x = m.get('end_x')
        if m.get('end_y') is not None:
            self.end_y = m.get('end_y')
        return self
