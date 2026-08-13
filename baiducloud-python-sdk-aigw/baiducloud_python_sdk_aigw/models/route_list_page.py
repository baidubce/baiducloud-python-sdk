"""
RouteListPage information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_aigw.models.route_summary import RouteSummary


class RouteListPage(AbstractModel):
    """
    RouteListPage
    """

    def __init__(self, order_by=None, order=None, page_no=None, page_size=None, total_count=None, result=None):
        """
        Initialize RouteListPage instance.

        :param order_by: 排序字段
        :type order_by: str (optional)

        :param order: 排序方向：asc、desc
        :type order: str (optional)

        :param page_no: 当前页码
        :type page_no: int (optional)

        :param page_size: 每页条数
        :type page_size: int (optional)

        :param total_count: 总记录数
        :type total_count: int (optional)

        :param result: 路由摘要列表
        :type result: List[RouteSummary] (optional)
        """
        super().__init__()
        self.order_by = order_by
        self.order = order
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count
        self.result = result

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
        if self.result is not None:
            result['result'] = [i.to_dict() for i in self.result]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RouteListPage

        :raises TypeError: If input is not a dictionary type
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
        if m.get('result') is not None:
            self.result = [RouteSummary().from_dict(i) for i in m.get('result')]
        return self
