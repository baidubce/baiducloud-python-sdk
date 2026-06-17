"""
Request entity for AsyncSearchRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bls.models.highlight import Highlight


class AsyncSearchRequest(AbstractModel):
    """
    Request entity for AsyncSearchRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, query, aggs=None, fields=None, sort=None, search_after=None, highlight=None, size=None):
        """
        Initialize AsyncSearchRequest request entity.

        :param name: name parameter
        :type name: str (required)

        :param query: query parameter
        :type query: object (required)

        :param aggs: aggs parameter
        :type aggs: object (optional)

        :param fields: 返回的字段列表，默认全部字段
        :type fields: List[str] (optional)

        :param sort: 排序，目前仅支持按照@timestamp排序，默认按时间倒序
        :type sort: Dict[str, Dict[str, str]] (optional)

        :param search_after: 下一页游标，目前只支持数组的第一个元素，默认从指定时间的第一个开始查询
        :type search_after: List[str] (optional)

        :param highlight: highlight parameter
        :type highlight: Highlight (optional)

        :param size: 查询返回多少条命中的日志，默认1000
        :type size: int (optional)
        """
        super().__init__()
        self.name = name
        self.query = query
        self.aggs = aggs
        self.fields = fields
        self.sort = sort
        self.search_after = search_after
        self.highlight = highlight
        self.size = size

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.query is not None:
            result['query'] = self.query
        if self.aggs is not None:
            result['aggs'] = self.aggs
        if self.fields is not None:
            result['fields'] = self.fields
        if self.sort is not None:
            result['sort'] = self.sort
        if self.search_after is not None:
            result['searchAfter'] = self.search_after
        if self.highlight is not None:
            result['highlight'] = self.highlight.to_dict()
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AsyncSearchRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('aggs') is not None:
            self.aggs = m.get('aggs')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('sort') is not None:
            self.sort = m.get('sort')
        if m.get('searchAfter') is not None:
            self.search_after = m.get('searchAfter')
        if m.get('highlight') is not None:
            self.highlight = Highlight().from_dict(m.get('highlight'))
        if m.get('size') is not None:
            self.size = m.get('size')
        return self
