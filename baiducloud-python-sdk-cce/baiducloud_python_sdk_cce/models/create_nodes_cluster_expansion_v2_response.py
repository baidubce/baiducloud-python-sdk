"""
Request entity for CreateNodesClusterExpansionV2Response information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateNodesClusterExpansionV2Response(BceResponse):
    """
    CreateNodesClusterExpansionV2Response
    """

    def __init__(self, cce_instance_ids=None, request_id=None):
        """
        Initialize CreateNodesClusterExpansionV2Response response.

        :param cce_instance_ids: 新增节点的 ID 列表
        :type cce_instance_ids: List[str] (optional)

        :param request_id: 请求 ID, 问题定位提供该 ID
        :type request_id: str (optional)
        """
        super().__init__()
        self.cce_instance_ids = cce_instance_ids
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
        if self.cce_instance_ids is not None:
            result['cceInstanceIDs'] = self.cce_instance_ids
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
        :rtype: CreateNodesClusterExpansionV2Response

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cceInstanceIDs') is not None:
            self.cce_instance_ids = m.get('cceInstanceIDs')
        if m.get('requestID') is not None:
            self.request_id = m.get('requestID')
        return self
