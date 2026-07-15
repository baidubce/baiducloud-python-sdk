"""
Statistics information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Statistics(AbstractModel):
    """
    Statistics
    """

    def __init__(self, total_target_count=None, failed_target_count=None):
        """
        Initialize Statistics instance.

        :param total_target_count: 执行的实例总数
        :type total_target_count: int (optional)

        :param failed_target_count: 已失败的执行实例总数
        :type failed_target_count: int (optional)
        """
        super().__init__()
        self.total_target_count = total_target_count
        self.failed_target_count = failed_target_count

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
        if self.total_target_count is not None:
            result['totalTargetCount'] = self.total_target_count
        if self.failed_target_count is not None:
            result['failedTargetCount'] = self.failed_target_count
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
        if m.get('totalTargetCount') is not None:
            self.total_target_count = m.get('totalTargetCount')
        if m.get('failedTargetCount') is not None:
            self.failed_target_count = m.get('failedTargetCount')
        return self
