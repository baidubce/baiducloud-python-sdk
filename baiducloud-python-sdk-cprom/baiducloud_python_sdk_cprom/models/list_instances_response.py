"""
Request entity for ListInstancesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_cprom.models.monitor_instance import MonitorInstance


class ListInstancesResponse(BceResponse):
    """
    ListInstancesResponse
    """

    def __init__(self, order_by=None, order=None, page_no=None, page_size=None, total_count=None, instances=None):
        """
        Initialize ListInstancesResponse response.

        :param order_by: 监控实例列表排序依据字段
        :type order_by: str (optional)

        :param order: 监控实例列表排序方式：desc倒序，asc升序
        :type order: str (optional)

        :param page_no: 实例列表分页当前页码数
        :type page_no: int (optional)

        :param page_size: 当前页页监控实例个数
        :type page_size: int (optional)

        :param total_count: 监控实例总个数
        :type total_count: int (optional)

        :param instances: 监控实例列表
        :type instances: List[MonitorInstance] (optional)
        """
        super().__init__()
        self.order_by = order_by
        self.order = order
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count
        self.instances = instances

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
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.instances is not None:
            result['instances'] = [i.to_dict() for i in self.instances]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListInstancesResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('instances') is not None:
            self.instances = [MonitorInstance().from_dict(i) for i in m.get('instances')]
        return self
