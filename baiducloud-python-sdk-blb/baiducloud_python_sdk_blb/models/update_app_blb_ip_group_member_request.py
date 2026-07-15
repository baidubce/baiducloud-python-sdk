"""
Request entity for UpdateAppBlbIpGroupMemberRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_blb.models.app_ip_group_member_for_update import AppIpGroupMemberForUpdate


class UpdateAppBlbIpGroupMemberRequest(AbstractModel):
    """
    Request entity for UpdateAppBlbIpGroupMemberRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, blb_id, ip_group_id, member_list, client_token=None):
        """
        Initialize UpdateAppBlbIpGroupMemberRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param ip_group_id: IP组的id
        :type ip_group_id: str (required)

        :param member_list: IP组成员列表
        :type member_list: List[AppIpGroupMemberForUpdate] (required)
        """
        super().__init__()
        self.blb_id = blb_id
        self.client_token = client_token
        self.ip_group_id = ip_group_id
        self.member_list = member_list

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
        if self.ip_group_id is not None:
            result['ipGroupId'] = self.ip_group_id
        if self.member_list is not None:
            result['memberList'] = [i.to_dict() for i in self.member_list]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateAppBlbIpGroupMemberRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ipGroupId') is not None:
            self.ip_group_id = m.get('ipGroupId')
        if m.get('memberList') is not None:
            self.member_list = [AppIpGroupMemberForUpdate().from_dict(i) for i in m.get('memberList')]
        return self
