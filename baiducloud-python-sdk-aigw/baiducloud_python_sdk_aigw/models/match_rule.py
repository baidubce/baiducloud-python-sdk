"""
MatchRule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_aigw.models.path_rule import PathRule

from baiducloud_python_sdk_aigw.models.matcher_rule import MatcherRule

from baiducloud_python_sdk_aigw.models.matcher_rule import MatcherRule


class MatchRule(AbstractModel):
    """
    MatchRule
    """

    def __init__(self, path_rule=None, methods=None, headers=None, var_query_params=None):
        """
        Initialize MatchRule instance.

        :param path_rule: path_rule attribute
        :type path_rule: PathRule (optional)

        :param methods: HTTP 方法列表
        :type methods: List[str] (optional)

        :param headers: 请求头匹配规则，每项包含 key、matchType、value
        :type headers: List[MatcherRule] (optional)

        :param var_query_params: Query 参数匹配规则，每项包含 key、matchType、value
        :type var_query_params: List[MatcherRule] (optional)
        """
        super().__init__()
        self.path_rule = path_rule
        self.methods = methods
        self.headers = headers
        self.var_query_params = var_query_params

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
        if self.path_rule is not None:
            result['pathRule'] = self.path_rule.to_dict()
        if self.methods is not None:
            result['methods'] = self.methods
        if self.headers is not None:
            result['headers'] = [i.to_dict() for i in self.headers]
        if self.var_query_params is not None:
            result['queryParams'] = [i.to_dict() for i in self.var_query_params]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MatchRule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('pathRule') is not None:
            self.path_rule = PathRule().from_dict(m.get('pathRule'))
        if m.get('methods') is not None:
            self.methods = m.get('methods')
        if m.get('headers') is not None:
            self.headers = [MatcherRule().from_dict(i) for i in m.get('headers')]
        if m.get('queryParams') is not None:
            self.var_query_params = [MatcherRule().from_dict(i) for i in m.get('queryParams')]
        return self
