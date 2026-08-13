"""
OriginRule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class OriginRule(AbstractModel):
    """
    OriginRule
    """

    def __init__(self, match_type=None, value=None):
        """
        Initialize OriginRule instance.

        :param match_type: 匹配类型
        :type match_type: str (optional)

        :param value: 匹配值
        :type value: str (optional)
        """
        super().__init__()
        self.match_type = match_type
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
        if self.match_type is not None:
            result['matchType'] = self.match_type
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
        :rtype: OriginRule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self
