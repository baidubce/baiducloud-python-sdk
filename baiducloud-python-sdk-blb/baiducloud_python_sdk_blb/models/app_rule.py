"""
AppRule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AppRule(AbstractModel):
    """
    AppRule
    """

    def __init__(self, id=None, key=None, value=None):
        """
        Initialize AppRule instance.

        :param id: 规则的标识符
        :type id: str (optional)

        :param key: 规则的类型，host/uri/\\*
        :type key: str (optional)

        :param value: 通配符匹配字符串，详见[ValueExample](#ValueExample)
        :type value: str (optional)
        """
        super().__init__()
        self.id = id
        self.key = key
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
        if self.id is not None:
            result['id'] = self.id
        if self.key is not None:
            result['key'] = self.key
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
        :rtype: AppRule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self
