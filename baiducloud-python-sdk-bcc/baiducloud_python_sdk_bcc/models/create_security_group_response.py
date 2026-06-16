"""
Request entity for CreateSecurityGroupResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateSecurityGroupResponse(BceResponse):
    """
    CreateSecurityGroupResponse
    """

    def __init__(self, security_group_id=None):
        """
        Initialize CreateSecurityGroupResponse response.

        :param security_group_id: 已创建的安全组ID
        :type security_group_id: str (optional)
        """
        super().__init__()
        self.security_group_id = security_group_id

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
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateSecurityGroupResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        return self
