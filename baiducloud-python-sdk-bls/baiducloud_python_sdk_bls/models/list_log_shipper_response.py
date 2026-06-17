"""
Request entity for ListLogShipperResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bls.models.shipper_summary import ShipperSummary


class ListLogShipperResponse(BceResponse):
    """
    ListLogShipperResponse
    """

    def __init__(self, success=None, code=None, total_count=None, result=None):
        """
        Initialize ListLogShipperResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 请求码，成功为OK，错误为具体的错误码
        :type code: str (optional)

        :param total_count: 总数目
        :type total_count: int (optional)

        :param result: 投递任务列表
        :type result: List[ShipperSummary] (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.total_count = total_count
        self.result = result

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
        if self.success is not None:
            result['success'] = self.success
        if self.code is not None:
            result['code'] = self.code
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.result is not None:
            result['result'] = [i.to_dict() for i in self.result]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListLogShipperResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('result') is not None:
            self.result = [ShipperSummary().from_dict(i) for i in m.get('result')]
        return self
