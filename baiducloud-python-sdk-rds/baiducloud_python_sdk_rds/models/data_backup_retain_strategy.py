"""
DataBackupRetainStrategy information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DataBackupRetainStrategy(AbstractModel):
    """
    DataBackupRetainStrategy
    """

    def __init__(self, start_seconds=None, end_seconds=None, retain_count=None, precision=None):
        """
        Initialize DataBackupRetainStrategy instance.

        :param start_seconds: 起始秒数。
        :type start_seconds: int (optional)

        :param end_seconds: 结束秒数。
        :type end_seconds: int (optional)

        :param retain_count: 保留数量。
        :type retain_count: int (optional)

        :param precision: 精度（单位：秒）。
        :type precision: int (optional)
        """
        super().__init__()
        self.start_seconds = start_seconds
        self.end_seconds = end_seconds
        self.retain_count = retain_count
        self.precision = precision

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
        if self.start_seconds is not None:
            result['startSeconds'] = self.start_seconds
        if self.end_seconds is not None:
            result['endSeconds'] = self.end_seconds
        if self.retain_count is not None:
            result['retainCount'] = self.retain_count
        if self.precision is not None:
            result['precision'] = self.precision
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DataBackupRetainStrategy

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('startSeconds') is not None:
            self.start_seconds = m.get('startSeconds')
        if m.get('endSeconds') is not None:
            self.end_seconds = m.get('endSeconds')
        if m.get('retainCount') is not None:
            self.retain_count = m.get('retainCount')
        if m.get('precision') is not None:
            self.precision = m.get('precision')
        return self
