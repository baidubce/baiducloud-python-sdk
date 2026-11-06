"""
Para information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Para(AbstractModel):
    """
    Para
    """

    def __init__(
        self,
        key=None,
        value=None,
        range=None,
        dynamic=None,
        desc=None,
        attention=None,
        type=None,
        best_value=None,
        precision=None,
        required=None,
    ):
        """
        Initialize Para instance.

        :param key: 见示例
        :type key: str (optional)

        :param value: 见示例
        :type value: str (optional)

        :param range: 见示例
        :type range: str (optional)

        :param dynamic: 见示例
        :type dynamic: int (optional)

        :param desc: 见示例
        :type desc: str (optional)

        :param attention: 见示例
        :type attention: str (optional)

        :param type: 见示例
        :type type: str (optional)

        :param best_value: 见示例
        :type best_value: str (optional)

        :param precision: 见示例
        :type precision: int (optional)

        :param required: 见示例
        :type required: bool (optional)
        """
        super().__init__()
        self.key = key
        self.value = value
        self.range = range
        self.dynamic = dynamic
        self.desc = desc
        self.attention = attention
        self.type = type
        self.best_value = best_value
        self.precision = precision
        self.required = required

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
        if self.value is not None:
            result['value'] = self.value
        if self.range is not None:
            result['range'] = self.range
        if self.dynamic is not None:
            result['dynamic'] = self.dynamic
        if self.desc is not None:
            result['desc'] = self.desc
        if self.attention is not None:
            result['attention'] = self.attention
        if self.type is not None:
            result['type'] = self.type
        if self.best_value is not None:
            result['bestValue'] = self.best_value
        if self.precision is not None:
            result['precision'] = self.precision
        if self.required is not None:
            result['required'] = self.required
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Para

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('range') is not None:
            self.range = m.get('range')
        if m.get('dynamic') is not None:
            self.dynamic = m.get('dynamic')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('attention') is not None:
            self.attention = m.get('attention')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('bestValue') is not None:
            self.best_value = m.get('bestValue')
        if m.get('precision') is not None:
            self.precision = m.get('precision')
        if m.get('required') is not None:
            self.required = m.get('required')
        return self
