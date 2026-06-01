"""
MetricQuery information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_apm.models.filter import Filter


class MetricQuery(AbstractModel):
    """
    MetricQuery
    """

    def __init__(self, name=None, compare_to=None, filters=None):
        """
        Initialize MetricQuery instance.

        :param name: 指标名
        :type name: str (optional)

        :param compare_to: compare_to attribute
        :type compare_to: List[str] (optional)

        :param filters: 该指标的特殊过滤条件，会与全局过滤项合并
        :type filters: List[Filter] (optional)
        """
        super().__init__()
        self.name = name
        self.compare_to = compare_to
        self.filters = filters

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
        if self.name is not None:
            result['name'] = self.name
        if self.compare_to is not None:
            result['compareTo'] = self.compare_to
        if self.filters is not None:
            result['filters'] = [i.to_dict() for i in self.filters]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MetricQuery

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('compareTo') is not None:
            self.compare_to = m.get('compareTo')
        if m.get('filters') is not None:
            self.filters = [Filter().from_dict(i) for i in m.get('filters')]
        return self
