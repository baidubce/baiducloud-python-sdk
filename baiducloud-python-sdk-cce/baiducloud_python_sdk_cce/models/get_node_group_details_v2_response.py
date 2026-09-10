"""
Request entity for GetNodeGroupDetailsV2Response information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_cce.models.instance_group import InstanceGroup


class GetNodeGroupDetailsV2Response(BceResponse):
    """
    GetNodeGroupDetailsV2Response
    """

    def __init__(self, request_id=None, instance_group=None):
        """
        Initialize GetNodeGroupDetailsV2Response response.

        :param request_id: 请求 ID, 问题定位提供该 ID
        :type request_id: str (optional)

        :param instance_group: instance_group field
        :type instance_group: InstanceGroup (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.instance_group = instance_group

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
            result['requestID'] = self.request_id
        if self.instance_group is not None:
            result['instanceGroup'] = self.instance_group.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetNodeGroupDetailsV2Response

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestID') is not None:
            self.request_id = m.get('requestID')
        if m.get('instanceGroup') is not None:
            self.instance_group = InstanceGroup().from_dict(m.get('instanceGroup'))
        return self
