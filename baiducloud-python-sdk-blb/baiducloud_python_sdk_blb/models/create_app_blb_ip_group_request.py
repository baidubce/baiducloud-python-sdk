"""
Request entity for CreateAppBlbIpGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_blb.models.app_ip_group_member import AppIpGroupMember


class CreateAppBlbIpGroupRequest(AbstractModel):
    """
    Request entity for CreateAppBlbIpGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, blb_id, client_token=None, name=None, desc=None, member_list=None):
        """
        Initialize CreateAppBlbIpGroupRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: IP组的名称，方便记忆。长度1~65个字节，字母开头，_可包含字母数字-/.字符。若不传该参数，会自动生成
        :type name: str (optional)

        :param desc: IP组的描述，最大支持200字符
        :type desc: str (optional)

        :param member_list: IP组挂载的IP组成员列表
        :type member_list: List[AppIpGroupMember] (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.client_token = client_token
        self.name = name
        self.desc = desc
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
        if self.name is not None:
            result['name'] = self.name
        if self.desc is not None:
            result['desc'] = self.desc
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
        :rtype: CreateAppBlbIpGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('memberList') is not None:
            self.member_list = [AppIpGroupMember().from_dict(i) for i in m.get('memberList')]
        return self
