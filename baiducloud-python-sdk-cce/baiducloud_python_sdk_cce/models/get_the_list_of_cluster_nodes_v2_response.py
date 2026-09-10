"""
Request entity for GetTheListOfClusterNodesV2Response information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_cce.models.instance_page import InstancePage


class GetTheListOfClusterNodesV2Response(BceResponse):
    """
    GetTheListOfClusterNodesV2Response
    """

    def __init__(self, instance_page=None, request_id=None):
        """
        Initialize GetTheListOfClusterNodesV2Response response.

        :param instance_page: instance_page field
        :type instance_page: InstancePage (optional)

        :param request_id: 响应的请求的ID
        :type request_id: str (optional)
        """
        super().__init__()
        self.instance_page = instance_page
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
        if self.instance_page is not None:
            result['instancePage'] = self.instance_page.to_dict()
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
        :rtype: GetTheListOfClusterNodesV2Response

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instancePage') is not None:
            self.instance_page = InstancePage().from_dict(m.get('instancePage'))
        if m.get('requestID') is not None:
            self.request_id = m.get('requestID')
        return self
