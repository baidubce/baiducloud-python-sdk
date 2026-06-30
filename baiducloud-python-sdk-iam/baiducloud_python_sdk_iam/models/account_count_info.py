"""
AccountCountInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AccountCountInfo(AbstractModel):
    """
    AccountCountInfo
    """

    def __init__(self, user_count=None, policy_count=None, group_count=None):
        """
        Initialize AccountCountInfo instance.

        :param user_count: 已创建的用户数量
        :type user_count: int (optional)

        :param policy_count: 已创建的策略数量
        :type policy_count: int (optional)

        :param group_count: 已创建的用户组数量
        :type group_count: int (optional)
        """
        super().__init__()
        self.user_count = user_count
        self.policy_count = policy_count
        self.group_count = group_count

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
        if self.user_count is not None:
            result['userCount'] = self.user_count
        if self.policy_count is not None:
            result['policyCount'] = self.policy_count
        if self.group_count is not None:
            result['groupCount'] = self.group_count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AccountCountInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userCount') is not None:
            self.user_count = m.get('userCount')
        if m.get('policyCount') is not None:
            self.policy_count = m.get('policyCount')
        if m.get('groupCount') is not None:
            self.group_count = m.get('groupCount')
        return self
