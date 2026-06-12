"""
Filter information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Filter(AbstractModel):
    """
    Filter
    """

    def __init__(self, key=None, op=None, value=None, values=None):
        """
        Initialize Filter instance.

        :param key: 过滤字段名，如 InstanceId
        :type key: str (optional)

        :param op: 过滤操作，可选值：= / != / in
        :type op: str (optional)

        :param value: 单值，可用于操作符: =, !=
        :type value: str (optional)

        :param values: 多值，可用于操作符：in
        :type values: List[str] (optional)
        """
        super().__init__()
        self.key = key
        self.op = op
        self.value = value
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
        if self.op is not None:
            result['op'] = self.op
        if self.value is not None:
            result['value'] = self.value
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
        :rtype: Filter

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
        if m.get('values') is not None:
            self.values = m.get('values')
        return self
