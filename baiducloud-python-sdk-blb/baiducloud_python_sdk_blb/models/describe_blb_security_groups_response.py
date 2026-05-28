"""
Request entity for DescribeBlbSecurityGroupsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_blb.models.blb_security_group_model import BlbSecurityGroupModel


class DescribeBlbSecurityGroupsResponse(BceResponse):
    """
    DescribeBlbSecurityGroupsResponse
    """

    def __init__(self, blb_security_groups=None):
        """
        Initialize DescribeBlbSecurityGroupsResponse response.

        :param blb_security_groups: 普通安全组信息，由BlbSecurityGroupModel组成的集合
        :type blb_security_groups: List[BlbSecurityGroupModel] (optional)
        """
        super().__init__()
        self.blb_security_groups = blb_security_groups

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
        if self.blb_security_groups is not None:
            result['blbSecurityGroups'] = [i.to_dict() for i in self.blb_security_groups]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeBlbSecurityGroupsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbSecurityGroups') is not None:
            self.blb_security_groups = [BlbSecurityGroupModel().from_dict(i) for i in m.get('blbSecurityGroups')]
        return self
