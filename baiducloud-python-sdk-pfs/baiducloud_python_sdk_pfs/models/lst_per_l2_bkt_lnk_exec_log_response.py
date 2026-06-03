"""
Request entity for LstPerL2BktLnkExecLogResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_pfs.models.execute_info import ExecuteInfo


class LstPerL2BktLnkExecLogResponse(BceResponse):
    """
    LstPerL2BktLnkExecLogResponse
    """

    def __init__(self, request_id=None, bucket_link_id=None, instance_id=None, execute_infos=None):
        """
        Initialize LstPerL2BktLnkExecLogResponse response.

        :param request_id: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type request_id: str (optional)

        :param bucket_link_id: 数据流动ID
        :type bucket_link_id: str (optional)

        :param instance_id: PFS实例ID
        :type instance_id: str (optional)

        :param execute_infos: 执行详情列表
        :type execute_infos: List[ExecuteInfo] (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.bucket_link_id = bucket_link_id
        self.instance_id = instance_id
        self.execute_infos = execute_infos

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
        if self.bucket_link_id is not None:
            result['bucketLinkId'] = self.bucket_link_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.execute_infos is not None:
            result['executeInfos'] = [i.to_dict() for i in self.execute_infos]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LstPerL2BktLnkExecLogResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('bucketLinkId') is not None:
            self.bucket_link_id = m.get('bucketLinkId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('executeInfos') is not None:
            self.execute_infos = [ExecuteInfo().from_dict(i) for i in m.get('executeInfos')]
        return self
