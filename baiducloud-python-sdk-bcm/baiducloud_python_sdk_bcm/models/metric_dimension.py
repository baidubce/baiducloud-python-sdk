"""
MetricDimension information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MetricDimension(AbstractModel):
    """
    MetricDimension
    """

    def __init__(self, key=None, operator=None, values=None):
        """
        Initialize MetricDimension instance.

        :param key: 维度key
        :type key: str (optional)

        :param operator: 操作符，可选值：= / !=
        :type operator: str (optional)

        :param values: 维度值列表
        :type values: List[str] (optional)
        """
        super().__init__()
        self.key = key
        self.operator = operator
        self.values = values

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
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MetricDimension

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self
