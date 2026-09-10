"""
Request entity for CreateNodeGroupV2Response information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateNodeGroupV2Response(BceResponse):
    """
    CreateNodeGroupV2Response
    """

    def __init__(self, instance_group_id=None, request_id=None):
        """
        Initialize CreateNodeGroupV2Response response.

        :param instance_group_id: 节点组 ID
        :type instance_group_id: str (optional)

        :param request_id: 请求 ID, 问题定位提供该 ID
        :type request_id: str (optional)
        """
        super().__init__()
        self.instance_group_id = instance_group_id
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
        if self.instance_group_id is not None:
            result['instanceGroupID'] = self.instance_group_id
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
        :rtype: CreateNodeGroupV2Response

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceGroupID') is not None:
            self.instance_group_id = m.get('instanceGroupID')
        if m.get('requestID') is not None:
            self.request_id = m.get('requestID')
        return self
