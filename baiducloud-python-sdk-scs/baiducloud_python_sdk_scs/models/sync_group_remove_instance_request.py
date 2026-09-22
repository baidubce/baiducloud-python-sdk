"""
Request entity for SyncGroupRemoveInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SyncGroupRemoveInstanceRequest(AbstractModel):
    """
    Request entity for SyncGroupRemoveInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, group_id, member_id=None, region=None):
        """
        Initialize SyncGroupRemoveInstanceRequest request entity.

        :param group_id: group_id parameter
        :type group_id: str (required)

        :param member_id: 待移除的成员实例展示ID
        :type member_id: str (optional)

        :param region: 成员实例所在地域
        :type region: str (optional)
        """
        super().__init__()
        self.group_id = group_id
        self.member_id = member_id
        self.region = region

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.member_id is not None:
            result['memberId'] = self.member_id
        if self.region is not None:
            result['region'] = self.region
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SyncGroupRemoveInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('memberId') is not None:
            self.member_id = m.get('memberId')
        if m.get('region') is not None:
            self.region = m.get('region')
        return self
