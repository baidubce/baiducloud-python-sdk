"""
Request entity for ListL3AccessRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListL3AccessRuleRequest(AbstractModel):
    """
    Request entity for ListL3AccessRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, access_group_name, zone_name, page_no=None, page_size=None, order_by=None, order=None, ip_filter=None
    ):
        """
        Initialize ListL3AccessRuleRequest request entity.

        :param access_group_name: 权限组名称
        :type access_group_name: str (required)

        :param zone_name: 可用区名称
        :type zone_name: str (required)

        :param page_no: 页码，默认 1
        :type page_no: int (optional)

        :param page_size: 每页条数，默认 10
        :type page_size: int (optional)

        :param order_by: 排序字段，默认 priority
        :type order_by: str (optional)

        :param order: 排序方向，asc / desc，默认 asc
        :type order: str (optional)

        :param ip_filter: 按 IP 过滤，ipv4 / ipv6，为空时展示所有，默认空字符串
        :type ip_filter: str (optional)
        """
        super().__init__()
        self.access_group_name = access_group_name
        self.zone_name = zone_name
        self.page_no = page_no
        self.page_size = page_size
        self.order_by = order_by
        self.order = order
        self.ip_filter = ip_filter

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
        if self.access_group_name is not None:
            result['accessGroupName'] = self.access_group_name
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.order is not None:
            result['order'] = self.order
        if self.ip_filter is not None:
            result['ipFilter'] = self.ip_filter
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListL3AccessRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accessGroupName') is not None:
            self.access_group_name = m.get('accessGroupName')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('ipFilter') is not None:
            self.ip_filter = m.get('ipFilter')
        return self
