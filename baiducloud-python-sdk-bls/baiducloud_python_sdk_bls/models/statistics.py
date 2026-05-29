"""
Statistics information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Statistics(AbstractModel):
    """
    Statistics
    """

    def __init__(self, execution_time_in_ms=None, scan_count=None, scan_bytes=None):
        """
        Initialize Statistics instance.

        :param execution_time_in_ms: 执行耗时（毫秒）
        :type execution_time_in_ms: int (optional)

        :param scan_count: 扫描记录数
        :type scan_count: int (optional)

        :param scan_bytes: 扫描数据量（字节）
        :type scan_bytes: int (optional)
        """
        super().__init__()
        self.execution_time_in_ms = execution_time_in_ms
        self.scan_count = scan_count
        self.scan_bytes = scan_bytes

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
        if self.execution_time_in_ms is not None:
            result['executionTimeInMs'] = self.execution_time_in_ms
        if self.scan_count is not None:
            result['scanCount'] = self.scan_count
        if self.scan_bytes is not None:
            result['scanBytes'] = self.scan_bytes
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Statistics

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('executionTimeInMs') is not None:
            self.execution_time_in_ms = m.get('executionTimeInMs')
        if m.get('scanCount') is not None:
            self.scan_count = m.get('scanCount')
        if m.get('scanBytes') is not None:
            self.scan_bytes = m.get('scanBytes')
        return self
