"""
PathRule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PathRule(AbstractModel):
    """
    PathRule
    """

    def __init__(self, match_type=None, value=None, case_sensitive=None):
        """
        Initialize PathRule instance.

        :param match_type: 匹配类型
        :type match_type: str (optional)

        :param value: 匹配值
        :type value: str (optional)

        :param case_sensitive: 是否区分大小写
        :type case_sensitive: bool (optional)
        """
        super().__init__()
        self.match_type = match_type
        self.value = value
        self.case_sensitive = case_sensitive

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
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PathRule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')
        return self
