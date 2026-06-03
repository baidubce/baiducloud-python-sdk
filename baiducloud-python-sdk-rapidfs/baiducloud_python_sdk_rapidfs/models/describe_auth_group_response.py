"""
Request entity for DescribeAuthGroupResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rapidfs.models.auth_group_info import AuthGroupInfo


class DescribeAuthGroupResponse(BceResponse):
    """
    DescribeAuthGroupResponse
    """

    def __init__(self, auth_group_info=None):
        """
        Initialize DescribeAuthGroupResponse response.

        :param auth_group_info: auth_group_info field
        :type auth_group_info: AuthGroupInfo (optional)
        """
        super().__init__()
        self.auth_group_info = auth_group_info

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
        if self.auth_group_info is not None:
            result['authGroupInfo'] = self.auth_group_info.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeAuthGroupResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('authGroupInfo') is not None:
            self.auth_group_info = AuthGroupInfo().from_dict(m.get('authGroupInfo'))
        return self
