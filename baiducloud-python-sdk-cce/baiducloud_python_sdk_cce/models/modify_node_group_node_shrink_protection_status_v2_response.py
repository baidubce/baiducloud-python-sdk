"""
Request entity for ModifyNodeGroupNodeShrinkProtectionStatusV2Response information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class ModifyNodeGroupNodeShrinkProtectionStatusV2Response(BceResponse):
    """
    ModifyNodeGroupNodeShrinkProtectionStatusV2Response
    """

    def __init__(self, failed_instances=None, request_id=None):
        """
        Initialize ModifyNodeGroupNodeShrinkProtectionStatusV2Response response.

        :param failed_instances: 修改失败的节点及原因列表，字段见下表
        :type failed_instances: List[object] (optional)

        :param request_id: 请求 ID, 问题定位提供该 ID
        :type request_id: str (optional)
        """
        super().__init__()
        self.failed_instances = failed_instances
        self.request_id = request_id

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
        if self.failed_instances is not None:
            result['failedInstances'] = self.failed_instances
        if self.request_id is not None:
            result['requestID'] = self.request_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyNodeGroupNodeShrinkProtectionStatusV2Response

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('failedInstances') is not None:
            self.failed_instances = m.get('failedInstances')
        if m.get('requestID') is not None:
            self.request_id = m.get('requestID')
        return self
