"""
Request entity for BatchGetLogStoreResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bls.models.log_store_detail import LogStoreDetail


class BatchGetLogStoreResponse(BceResponse):
    """
    BatchGetLogStoreResponse
    """

    def __init__(self, code=None, success=None, result=None):
        """
        Initialize BatchGetLogStoreResponse response.

        :param code: 状态码
        :type code: str (optional)

        :param success: 返回是否成功
        :type success: bool (optional)

        :param result: LogStore 列表
        :type result: List[LogStoreDetail] (optional)
        """
        super().__init__()
        self.code = code
        self.success = success
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
        if self.code is not None:
            result['code'] = self.code
        if self.success is not None:
            result['success'] = self.success
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
        :rtype: BatchGetLogStoreResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('result') is not None:
            self.result = [LogStoreDetail().from_dict(i) for i in m.get('result')]
        return self
