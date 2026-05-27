"""
Request entity for CreateIpSetResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateIpSetResponse(BceResponse):
    """
    CreateIpSetResponse
    """

    def __init__(self, ip_group_id=None):
        """
        Initialize CreateIpSetResponse response.

        :param ip_group_id: IP地址族的ID
        :type ip_group_id: str (optional)
        """
        super().__init__()
        self.ip_group_id = ip_group_id

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
        if self.ip_group_id is not None:
            result['ipGroupId'] = self.ip_group_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateIpSetResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ipGroupId') is not None:
            self.ip_group_id = m.get('ipGroupId')
        return self
