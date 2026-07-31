"""
Request entity for UpdateAppBlbIpGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateAppBlbIpGroupRequest(AbstractModel):
    """
    Request entity for UpdateAppBlbIpGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, blb_id, ip_group_id, client_token=None, name=None, desc=None):
        """
        Initialize UpdateAppBlbIpGroupRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param ip_group_id: 要更新的IP组id
        :type ip_group_id: str (required)

        :param name: IP组的名称，方便记忆。长度1~65个字节，字母开头，_可包含字母数字-/.字符。
        :type name: str (optional)

        :param desc: IP组的描述，最大支持200字符
        :type desc: str (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.client_token = client_token
        self.ip_group_id = ip_group_id
        self.name = name
        self.desc = desc

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
        if self.name is not None:
            result['name'] = self.name
        if self.desc is not None:
            result['desc'] = self.desc
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateAppBlbIpGroupRequest

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
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        return self
