"""
SearchInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SearchInfo(AbstractModel):
    """
    SearchInfo
    """

    def __init__(self, query_type=None, took=None, hits=None):
        """
        Initialize SearchInfo instance.

        :param query_type: 返回语句类型，match：检索语句，sql：分析语句，match_and_sql：包含检索和分析语句
        :type query_type: str (optional)

        :param took: 统计耗时，单位毫秒
        :type took: int (optional)

        :param hits: 匹配上的总日志条数
        :type hits: int (optional)
        """
        super().__init__()
        self.query_type = query_type
        self.took = took
        self.hits = hits

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
        if self.query_type is not None:
            result['queryType'] = self.query_type
        if self.took is not None:
            result['took'] = self.took
        if self.hits is not None:
            result['hits'] = self.hits
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SearchInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('queryType') is not None:
            self.query_type = m.get('queryType')
        if m.get('took') is not None:
            self.took = m.get('took')
        if m.get('hits') is not None:
            self.hits = m.get('hits')
        return self
