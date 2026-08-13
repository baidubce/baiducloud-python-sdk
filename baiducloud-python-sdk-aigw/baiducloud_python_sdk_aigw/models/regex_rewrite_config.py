"""
RegexRewriteConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RegexRewriteConfig(AbstractModel):
    """
    RegexRewriteConfig
    """

    def __init__(self, match=None, rewrite=None):
        """
        Initialize RegexRewriteConfig instance.

        :param match: 正则匹配规则
        :type match: str (optional)

        :param rewrite: 替换规则
        :type rewrite: str (optional)
        """
        super().__init__()
        self.match = match
        self.rewrite = rewrite

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
        if self.match is not None:
            result['match'] = self.match
        if self.rewrite is not None:
            result['rewrite'] = self.rewrite
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RegexRewriteConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('match') is not None:
            self.match = m.get('match')
        if m.get('rewrite') is not None:
            self.rewrite = m.get('rewrite')
        return self
