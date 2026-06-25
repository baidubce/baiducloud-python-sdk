"""
Request entity for ListServiceMonitorsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_cprom.models.service_monitor_item import ServiceMonitorItem


class ListServiceMonitorsResponse(BceResponse):
    """
    ListServiceMonitorsResponse
    """

    def __init__(
        self,
        order_by=None,
        order=None,
        keyword_type=None,
        keyword=None,
        page_no=None,
        page_size=None,
        total_count=None,
        status=None,
        items=None,
    ):
        """
        Initialize ListServiceMonitorsResponse response.

        :param order_by: 排序字段
        :type order_by: str (optional)

        :param order: 排序方式
        :type order: str (optional)

        :param keyword_type: 筛选条件类型
        :type keyword_type: str (optional)

        :param keyword: 筛选关键字
        :type keyword: str (optional)

        :param page_no: 当前页码
        :type page_no: int (optional)

        :param page_size: 每页数量
        :type page_size: int (optional)

        :param total_count: 总数量
        :type total_count: int (optional)

        :param status: Service Monitor 服务状态：running/terminated
        :type status: str (optional)

        :param items: Service Monitor 列表
        :type items: List[ServiceMonitorItem] (optional)
        """
        super().__init__()
        self.order_by = order_by
        self.order = order
        self.keyword_type = keyword_type
        self.keyword = keyword
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count
        self.status = status
        self.items = items

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
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.order is not None:
            result['order'] = self.order
        if self.keyword_type is not None:
            result['keywordType'] = self.keyword_type
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.status is not None:
            result['status'] = self.status
        if self.items is not None:
            result['items'] = [i.to_dict() for i in self.items]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListServiceMonitorsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('keywordType') is not None:
            self.keyword_type = m.get('keywordType')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('items') is not None:
            self.items = [ServiceMonitorItem().from_dict(i) for i in m.get('items')]
        return self
