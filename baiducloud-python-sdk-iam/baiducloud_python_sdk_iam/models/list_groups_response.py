"""
Request entity for ListGroupsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_iam.models.group_model import GroupModel


class ListGroupsResponse(BceResponse):
    """
    ListGroupsResponse
    """

    def __init__(self, groups=None):
        """
        Initialize ListGroupsResponse response.

        :param groups: 组对象的列表
        :type groups: List[GroupModel] (optional)
        """
        super().__init__()
        self.groups = groups

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
        if self.groups is not None:
            result['groups'] = [i.to_dict() for i in self.groups]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListGroupsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groups') is not None:
            self.groups = [GroupModel().from_dict(i) for i in m.get('groups')]
        return self
