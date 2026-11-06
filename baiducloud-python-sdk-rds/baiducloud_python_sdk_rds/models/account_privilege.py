"""
AccountPrivilege information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AccountPrivilege(AbstractModel):
    """
    AccountPrivilege
    """

    def __init__(self, account_name=None, auth_type=None):
        """
        Initialize AccountPrivilege instance.

        :param account_name: 账户名称
        :type account_name: str (optional)

        :param auth_type: 授权类型。ReadOnly：只读，ReadWrite：读写
        :type auth_type: str (optional)
        """
        super().__init__()
        self.account_name = account_name
        self.auth_type = auth_type

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.account_name is not None:
            result['accountName'] = self.account_name
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AccountPrivilege

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        return self
