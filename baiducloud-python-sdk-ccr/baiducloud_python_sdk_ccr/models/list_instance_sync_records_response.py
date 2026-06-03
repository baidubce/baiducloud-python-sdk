"""
Request entity for ListInstanceSyncRecordsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ccr.models.execution_result import ExecutionResult


class ListInstanceSyncRecordsResponse(BceResponse):
    """
    ListInstanceSyncRecordsResponse
    """

    def __init__(self, total=None, page_size=None, items=None):
        """
        Initialize ListInstanceSyncRecordsResponse response.

        :param total: 执行记录总数
        :type total: int (optional)

        :param page_size: 每页记录数
        :type page_size: int (optional)

        :param items: 执行记录列表
        :type items: List[ExecutionResult] (optional)
        """
        super().__init__()
        self.total = total
        self.page_size = page_size
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
        if self.total is not None:
            result['total'] = self.total
        if self.page_size is not None:
            result['pageSize'] = self.page_size
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
        :rtype: ListInstanceSyncRecordsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('items') is not None:
            self.items = [ExecutionResult().from_dict(i) for i in m.get('items')]
        return self
