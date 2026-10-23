"""
Request entity for ListL3AccessGroupResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_pfs.models.l3_access_group import L3AccessGroup


class ListL3AccessGroupResponse(BceResponse):
    """
    ListL3AccessGroupResponse
    """

    def __init__(
        self,
        request_id=None,
        result=None,
        page_no=None,
        page_size=None,
        total_count=None,
        real_total_count=None,
        order=None,
        order_by=None,
    ):
        """
        Initialize ListL3AccessGroupResponse response.

        :param request_id: 唯一请求 ID，每次请求都会返回
        :type request_id: str (optional)

        :param result: result field
        :type result: list[L3AccessGroup] (optional)

        :param page_no: 当前页码
        :type page_no: int (optional)

        :param page_size: 每页条数
        :type page_size: int (optional)

        :param total_count: 过滤后的总条数，用于计算总页数
        :type total_count: int (optional)

        :param real_total_count: 过滤前的全量总条数，用于配额展示
        :type real_total_count: int (optional)

        :param order: 排序方向
        :type order: str (optional)

        :param order_by: 排序字段
        :type order_by: str (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.result = result
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count
        self.real_total_count = real_total_count
        self.order = order
        self.order_by = order_by

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = [item.to_dict() for item in self.result]
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.real_total_count is not None:
            result['realTotalCount'] = self.real_total_count
        if self.order is not None:
            result['order'] = self.order
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListL3AccessGroupResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = [L3AccessGroup().from_dict(item) for item in m.get('result')]
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('realTotalCount') is not None:
            self.real_total_count = m.get('realTotalCount')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        return self
