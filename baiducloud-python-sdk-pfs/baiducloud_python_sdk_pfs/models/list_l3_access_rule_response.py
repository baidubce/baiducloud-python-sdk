"""
Request entity for ListL3AccessRuleResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_pfs.models.l3_access_rule import L3AccessRule


class ListL3AccessRuleResponse(BceResponse):
    """
    ListL3AccessRuleResponse
    """

    def __init__(self, request_id=None, result=None, total_count=None, page_no=None, page_size=None):
        """
        Initialize ListL3AccessRuleResponse response.

        :param request_id: 唯一请求 ID，每次请求都会返回
        :type request_id: str (optional)

        :param result: result field
        :type result: list[L3AccessRule] (optional)

        :param total_count: 总条数
        :type total_count: int (optional)

        :param page_no: 当前页码
        :type page_no: int (optional)

        :param page_size: 每页条数
        :type page_size: int (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.result = result
        self.total_count = total_count
        self.page_no = page_no
        self.page_size = page_size

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
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListL3AccessRuleResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = [L3AccessRule().from_dict(item) for item in m.get('result')]
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
