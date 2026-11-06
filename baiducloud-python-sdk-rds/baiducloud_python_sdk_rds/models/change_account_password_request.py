"""
Request entity for ChangeAccountPasswordRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ChangeAccountPasswordRequest(AbstractModel):
    """
    Request entity for ChangeAccountPasswordRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, account_name, password):
        """
        Initialize ChangeAccountPasswordRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param account_name: account_name parameter
        :type account_name: str (required)

        :param password: 账号的密码，由字母、数字或下划线组成，长度6～32位 密码需要加密传输，禁止明文传输，详情请参考密码加密传输规范定义
        :type password: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.account_name = account_name
        self.password = password

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
        if self.password is not None:
            result['password'] = self.password
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ChangeAccountPasswordRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')
        if m.get('password') is not None:
            self.password = m.get('password')
        return self
