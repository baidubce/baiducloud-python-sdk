"""
Request entity for CreateEnterpriseSecurityGroupResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateEnterpriseSecurityGroupResponse(BceResponse):
    """
    CreateEnterpriseSecurityGroupResponse
    """

    def __init__(self, enterprise_security_group_id=None):
        """
        Initialize CreateEnterpriseSecurityGroupResponse response.

        :param enterprise_security_group_id: 已创建的企业安全组的ID
        :type enterprise_security_group_id: str (optional)
        """
        super().__init__()
        self.enterprise_security_group_id = enterprise_security_group_id

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
        if self.enterprise_security_group_id is not None:
            result['enterpriseSecurityGroupId'] = self.enterprise_security_group_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateEnterpriseSecurityGroupResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('enterpriseSecurityGroupId') is not None:
            self.enterprise_security_group_id = m.get('enterpriseSecurityGroupId')
        return self
