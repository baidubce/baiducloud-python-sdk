"""
Request entity for UpdateSecurityGroupResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class UpdateSecurityGroupResponse(BceResponse):
    """
    UpdateSecurityGroupResponse
    """

    def __init__(self, success=None):
        """
        Initialize UpdateSecurityGroupResponse response.

        :param success: 是否成功。
        :type success: bool (optional)
        """
        super().__init__()
        self.success = success

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
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateSecurityGroupResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        return self
