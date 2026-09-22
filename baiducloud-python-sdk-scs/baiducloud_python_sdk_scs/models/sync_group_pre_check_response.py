"""
Request entity for SyncGroupPreCheckResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_scs.models.check_sync_group_result_item import CheckSyncGroupResultItem
from baiducloud_python_sdk_scs.models.sync_group_instance_connection_result import SyncGroupInstanceConnectionResult


class SyncGroupPreCheckResponse(BceResponse):
    """
    SyncGroupPreCheckResponse
    """

    def __init__(self, check_result=None, connection_results=None):
        """
        Initialize SyncGroupPreCheckResponse response.

        :param check_result: 各成员校验结果列表
        :type check_result: List[CheckSyncGroupResultItem] (optional)

        :param connection_results: 实例间连通性结果列表
        :type connection_results: List[SyncGroupInstanceConnectionResult] (optional)
        """
        super().__init__()
        self.check_result = check_result
        self.connection_results = connection_results

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
        if self.check_result is not None:
            result['checkResult'] = [i.to_dict() for i in self.check_result]
        if self.connection_results is not None:
            result['connectionResults'] = [i.to_dict() for i in self.connection_results]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SyncGroupPreCheckResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('checkResult') is not None:
            self.check_result = [CheckSyncGroupResultItem().from_dict(i) for i in m.get('checkResult')]
        if m.get('connectionResults') is not None:
            self.connection_results = [
                SyncGroupInstanceConnectionResult().from_dict(i) for i in m.get('connectionResults')
            ]
        return self
