"""
LineSegment information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LineSegment(AbstractModel):
    """
    LineSegment
    """

    def __init__(self, line_id=None, start_index=None, end_index=None):
        """
        Initialize LineSegment instance.

        :param line_id: 对应lines里的lineId
        :type line_id: str (optional)

        :param start_index: 该句在行中的起始位置标识
        :type start_index: int (optional)

        :param end_index: 该句在行中的结束位置标识
        :type end_index: int (optional)
        """
        super().__init__()
        self.line_id = line_id
        self.start_index = start_index
        self.end_index = end_index

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
        if self.line_id is not None:
            result['lineId'] = self.line_id
        if self.start_index is not None:
            result['startIndex'] = self.start_index
        if self.end_index is not None:
            result['endIndex'] = self.end_index
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LineSegment

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('lineId') is not None:
            self.line_id = m.get('lineId')
        if m.get('startIndex') is not None:
            self.start_index = m.get('startIndex')
        if m.get('endIndex') is not None:
            self.end_index = m.get('endIndex')
        return self
