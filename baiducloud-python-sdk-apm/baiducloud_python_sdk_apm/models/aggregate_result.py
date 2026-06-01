"""
AggregateResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AggregateResult(AbstractModel):
    """
    AggregateResult
    """

    def __init__(self, sum=None, sum_per_second=None):
        """
        Initialize AggregateResult instance.

        :param sum: 求和值
        :type sum: float (optional)

        :param sum_per_second: 求和后计算的每秒平均值
        :type sum_per_second: float (optional)
        """
        super().__init__()
        self.sum = sum
        self.sum_per_second = sum_per_second

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
        if self.sum is not None:
            result['sum'] = self.sum
        if self.sum_per_second is not None:
            result['sumPerSecond'] = self.sum_per_second
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AggregateResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sum') is not None:
            self.sum = m.get('sum')
        if m.get('sumPerSecond') is not None:
            self.sum_per_second = m.get('sumPerSecond')
        return self
