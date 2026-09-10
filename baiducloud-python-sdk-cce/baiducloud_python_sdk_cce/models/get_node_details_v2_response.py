"""
Request entity for GetNodeDetailsV2Response information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_cce.models.instance import Instance


class GetNodeDetailsV2Response(BceResponse):
    """
    GetNodeDetailsV2Response
    """

    def __init__(self, instance=None, request_id=None):
        """
        Initialize GetNodeDetailsV2Response response.

        :param instance: instance field
        :type instance: Instance (optional)

        :param request_id: 请求 ID, 问题定位提供该 ID
        :type request_id: str (optional)
        """
        super().__init__()
        self.instance = instance
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
        if self.instance is not None:
            result['instance'] = self.instance.to_dict()
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
        :rtype: GetNodeDetailsV2Response

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instance') is not None:
            self.instance = Instance().from_dict(m.get('instance'))
        if m.get('requestID') is not None:
            self.request_id = m.get('requestID')
        return self
