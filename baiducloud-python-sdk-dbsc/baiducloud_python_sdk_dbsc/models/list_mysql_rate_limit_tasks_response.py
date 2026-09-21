"""
Request entity for ListMysqlRateLimitTasksResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_dbsc.models.my_sql_filter_item import MySQLFilterItem


class ListMysqlRateLimitTasksResponse(BceResponse):
    """
    ListMysqlRateLimitTasksResponse
    """

    def __init__(self, total_count=None, items=None):
        """
        Initialize ListMysqlRateLimitTasksResponse response.

        :param total_count: 限流任务总数
        :type total_count: int (optional)

        :param items: 限流任务详情
        :type items: List[MySQLFilterItem] (optional)
        """
        super().__init__()
        self.total_count = total_count
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
        if self.total_count is not None:
            result['totalCount'] = self.total_count
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
        :rtype: ListMysqlRateLimitTasksResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('items') is not None:
            self.items = [MySQLFilterItem().from_dict(i) for i in m.get('items')]
        return self
