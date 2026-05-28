"""
Request entity for DescribeBlbEnterpriseSecurityGroupsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_blb.models.blb_enterprise_security_group_model import BlbEnterpriseSecurityGroupModel


class DescribeBlbEnterpriseSecurityGroupsResponse(BceResponse):
    """
    DescribeBlbEnterpriseSecurityGroupsResponse
    """

    def __init__(self, enterprise_security_groups=None):
        """
        Initialize DescribeBlbEnterpriseSecurityGroupsResponse response.

        :param enterprise_security_groups: 企业安全组信息，由BlbEnterpriseSecurityGroupModel组成的集合
        :type enterprise_security_groups: List[BlbEnterpriseSecurityGroupModel] (optional)
        """
        super().__init__()
        self.enterprise_security_groups = enterprise_security_groups

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
        if self.enterprise_security_groups is not None:
            result['enterpriseSecurityGroups'] = [i.to_dict() for i in self.enterprise_security_groups]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeBlbEnterpriseSecurityGroupsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('enterpriseSecurityGroups') is not None:
            self.enterprise_security_groups = [
                BlbEnterpriseSecurityGroupModel().from_dict(i) for i in m.get('enterpriseSecurityGroups')
            ]
        return self
