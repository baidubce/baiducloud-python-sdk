"""
MetricFilter information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MetricFilter(AbstractModel):
    """
    MetricFilter
    """

    def __init__(self, key=None, op=None, value=None):
        """
        Initialize MetricFilter instance.

        :param key: 过滤字段名
        :type key: str (optional)

        :param op: 过滤操作，可选项：`=` - 等于，`!=` - 不等于，`contains` - 包含
        :type op: str (optional)

        :param value: 过滤值
        :type value: str (optional)
        """
        super().__init__()
        self.key = key
        self.op = op
        self.value = value

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
        if self.op is not None:
            result['op'] = self.op
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MetricFilter

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('op') is not None:
            self.op = m.get('op')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self
