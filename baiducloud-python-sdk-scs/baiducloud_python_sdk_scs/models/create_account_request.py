"""
Request entity for CreateAccountRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateAccountRequest(AbstractModel):
    """
    Request entity for CreateAccountRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, user_name, client_auth, user_type, extra=None):
        """
        Initialize CreateAccountRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param user_name: 账号名称。由小写字母、数字、下划线组成、字母开头,字母或数字结尾,最长16个字符。
        :type user_name: str (required)

        :param client_auth: 账号密码。详情请参考[密码加密传输规范定义](SCS/API参考/通用说明.md#密码加密传输规范定义)
        :type client_auth: str (required)

        :param extra: 备注
        :type extra: str (optional)

        :param user_type: 账号权限。1：读写；2：只读；
        :type user_type: int (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.user_name = user_name
        self.client_auth = client_auth
        self.extra = extra
        self.user_type = user_type

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
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.client_auth is not None:
            result['clientAuth'] = self.client_auth
        if self.extra is not None:
            result['extra'] = self.extra
        if self.user_type is not None:
            result['userType'] = self.user_type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAccountRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('clientAuth') is not None:
            self.client_auth = m.get('clientAuth')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('userType') is not None:
            self.user_type = m.get('userType')
        return self
