"""
Request entity for ListLogStoreViewResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bls.models.log_store_view import LogStoreView


class ListLogStoreViewResponse(BceResponse):
    """
    ListLogStoreViewResponse
    """

    def __init__(self, order=None, order_by=None, page_no=None, page_size=None, total_count=None, views=None):
        """
        Initialize ListLogStoreViewResponse response.

        :param order: 排序规则，desc为降序，asc为升序
        :type order: str (optional)

        :param order_by: 排序字段
        :type order_by: str (optional)

        :param page_no: 起始页码
        :type page_no: int (optional)

        :param page_size: 每页显示数据大小
        :type page_size: int (optional)

        :param total_count: 总数目
        :type total_count: int (optional)

        :param views: LogStore 列表
        :type views: List[LogStoreView] (optional)
        """
        super().__init__()
        self.order = order
        self.order_by = order_by
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count
        self.views = views

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.order is not None:
            result['order'] = self.order
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.views is not None:
            result['views'] = [i.to_dict() for i in self.views]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListLogStoreViewResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('views') is not None:
            self.views = [LogStoreView().from_dict(i) for i in m.get('views')]
        return self
