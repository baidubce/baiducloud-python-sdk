"""
QueryItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QueryItem(AbstractModel):
    """
    QueryItem
    """

    def __init__(self, query=None):
        """
        Initialize QueryItem instance.

        :param query: 用户自定义的短语或问题
        :type query: str (optional)
        """
        super().__init__()
        self.query = query

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
        if self.query is not None:
            result['query'] = self.query
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')
        return self
