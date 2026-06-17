"""
SharedUser information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SharedUser(AbstractModel):
    """
    SharedUser
    """

    def __init__(self, account=None, account_id=None, uc_account=None):
        """
        Initialize SharedUser instance.

        :param account: 共享用户名
        :type account: str (optional)

        :param account_id: 共享用户ID
        :type account_id: str (optional)

        :param uc_account: uc账号
        :type uc_account: str (optional)
        """
        super().__init__()
        self.account = account
        self.account_id = account_id
        self.uc_account = uc_account

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
        if self.account is not None:
            result['account'] = self.account
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.uc_account is not None:
            result['ucAccount'] = self.uc_account
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SharedUser

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('account') is not None:
            self.account = m.get('account')
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('ucAccount') is not None:
            self.uc_account = m.get('ucAccount')
        return self
