"""
Request entity for ListL3AccessGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListL3AccessGroupRequest(AbstractModel):
    """
    Request entity for ListL3AccessGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, keyword=None, keyword_type=None, zone_name=None, order=None, order_by=None, page_no=None, page_size=None
    ):
        """
        Initialize ListL3AccessGroupRequest request entity.

        :param keyword: 搜索关键字，需与 keywordType 同时传才生效
        :type keyword: str (optional)

        :param keyword_type: 搜索字段，当前仅支持 name（按权限组名模糊匹配）
        :type keyword_type: str (optional)

        :param zone_name: 可用区；不传则返回所有可用区
        :type zone_name: str (optional)

        :param order: 排序方向，asc / desc，默认 desc
        :type order: str (optional)

        :param order_by: 排序字段，默认 createTime
        :type order_by: str (optional)

        :param page_no: 页码，从 1 开始；传 ≤ 0 会被纠正为 1，默认 1
        :type page_no: int (optional)

        :param page_size: 每页条数；传 ≤ 0 会被纠正为 10，默认 10
        :type page_size: int (optional)
        """
        super().__init__()
        self.keyword = keyword
        self.keyword_type = keyword_type
        self.zone_name = zone_name
        self.order = order
        self.order_by = order_by
        self.page_no = page_no
        self.page_size = page_size

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
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.keyword_type is not None:
            result['keywordType'] = self.keyword_type
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.order is not None:
            result['order'] = self.order
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListL3AccessGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('keywordType') is not None:
            self.keyword_type = m.get('keywordType')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
