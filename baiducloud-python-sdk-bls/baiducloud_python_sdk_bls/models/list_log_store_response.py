"""
Request entity for ListLogStoreResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bls.models.log_store_detail import LogStoreDetail


class ListLogStoreResponse(BceResponse):
    """
    ListLogStoreResponse
    """

    def __init__(
        self,
        code=None,
        success=None,
        order=None,
        order_by=None,
        page_no=None,
        page_size=None,
        result=None,
        total_count=None,
    ):
        """
        Initialize ListLogStoreResponse response.

        :param code: 接口返回码
        :type code: str (optional)

        :param success: 请求是否成功
        :type success: bool (optional)

        :param order: 列表排序方式
        :type order: str (optional)

        :param order_by: 列表排序列
        :type order_by: str (optional)

        :param page_no: 页码
        :type page_no: int (optional)

        :param page_size: 每页数量
        :type page_size: int (optional)

        :param result: 接口返回码
        :type result: List[LogStoreDetail] (optional)

        :param total_count: 日志集总数
        :type total_count: int (optional)
        """
        super().__init__()
        self.code = code
        self.success = success
        self.order = order
        self.order_by = order_by
        self.page_no = page_no
        self.page_size = page_size
        self.result = result
        self.total_count = total_count

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
        if self.code is not None:
            result['code'] = self.code
        if self.success is not None:
            result['success'] = self.success
        if self.order is not None:
            result['order'] = self.order
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.result is not None:
            result['result'] = [i.to_dict() for i in self.result]
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListLogStoreResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('result') is not None:
            self.result = [LogStoreDetail().from_dict(i) for i in m.get('result')]
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self
