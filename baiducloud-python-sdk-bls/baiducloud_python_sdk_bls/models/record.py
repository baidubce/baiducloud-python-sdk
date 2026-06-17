"""
Record information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Record(AbstractModel):
    """
    Record
    """

    def __init__(self, start_time=None, end_time=None, finished_count=None):
        """
        Initialize Record instance.

        :param start_time:
        :type start_time: str (optional)

        :param end_time:
        :type end_time: str (optional)

        :param finished_count:
        :type finished_count: int (optional)
        """
        super().__init__()
        self.start_time = start_time
        self.end_time = end_time
        self.finished_count = finished_count

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
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.finished_count is not None:
            result['finishedCount'] = self.finished_count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Record

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('finishedCount') is not None:
            self.finished_count = m.get('finishedCount')
        return self
