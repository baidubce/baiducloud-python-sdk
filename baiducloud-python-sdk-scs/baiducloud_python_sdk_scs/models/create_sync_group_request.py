"""
Request entity for CreateSyncGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_scs.models.member import Member


class CreateSyncGroupRequest(AbstractModel):
    """
    Request entity for CreateSyncGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, sync_group_name, members):
        """
        Initialize CreateSyncGroupRequest request entity.

        :param sync_group_name: 多活实例组名称。规则：支持大小写字母、数字以及-_.等特殊字符，以字母开头，长度6~32位
        :type sync_group_name: str (required)

        :param members: 多活实例组成员。最多支持5个成员。
        :type members: List[Member] (required)
        """
        super().__init__()
        self.sync_group_name = sync_group_name
        self.members = members

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
        if self.sync_group_name is not None:
            result['syncGroupName'] = self.sync_group_name
        if self.members is not None:
            result['members'] = [i.to_dict() for i in self.members]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateSyncGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('syncGroupName') is not None:
            self.sync_group_name = m.get('syncGroupName')
        if m.get('members') is not None:
            self.members = [Member().from_dict(i) for i in m.get('members')]
        return self
