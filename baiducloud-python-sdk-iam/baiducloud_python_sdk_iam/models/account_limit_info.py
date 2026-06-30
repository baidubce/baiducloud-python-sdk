"""
AccountLimitInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AccountLimitInfo(AbstractModel):
    """
    AccountLimitInfo
    """

    def __init__(
        self,
        user_limit=None,
        policy_limit=None,
        contacts_limit=None,
        group_limit=None,
        sub_user_of_group_limit=None,
        group_max_attach_policy_limit=None,
        user_role_per_account_limit=None,
        role_max_attach_system_policy_limit=None,
        role_max_attach_custom_policy_limit=None,
        aksk_limit=None,
    ):
        """
        Initialize AccountLimitInfo instance.

        :param user_limit: 子用户上限数量
        :type user_limit: int (optional)

        :param policy_limit: 自定义策略上限数量
        :type policy_limit: int (optional)

        :param contacts_limit: 消息接收人上限数量
        :type contacts_limit: int (optional)

        :param group_limit: 用户组上限数量
        :type group_limit: int (optional)

        :param sub_user_of_group_limit: 单个用户组可添加的子用户上限数量
        :type sub_user_of_group_limit: int (optional)

        :param group_max_attach_policy_limit: 关联到用户组的策略上限数量
        :type group_max_attach_policy_limit: int (optional)

        :param user_role_per_account_limit: 角色上限数量
        :type user_role_per_account_limit: int (optional)

        :param role_max_attach_system_policy_limit: 关系到角色的系统策略上限数量
        :type role_max_attach_system_policy_limit: int (optional)

        :param role_max_attach_custom_policy_limit: 关系到角色的自定义策略上限数量
        :type role_max_attach_custom_policy_limit: int (optional)

        :param aksk_limit: 每个子用户可以创建的AK上限数量
        :type aksk_limit: int (optional)
        """
        super().__init__()
        self.user_limit = user_limit
        self.policy_limit = policy_limit
        self.contacts_limit = contacts_limit
        self.group_limit = group_limit
        self.sub_user_of_group_limit = sub_user_of_group_limit
        self.group_max_attach_policy_limit = group_max_attach_policy_limit
        self.user_role_per_account_limit = user_role_per_account_limit
        self.role_max_attach_system_policy_limit = role_max_attach_system_policy_limit
        self.role_max_attach_custom_policy_limit = role_max_attach_custom_policy_limit
        self.aksk_limit = aksk_limit

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
        if self.user_limit is not None:
            result['userLimit'] = self.user_limit
        if self.policy_limit is not None:
            result['policyLimit'] = self.policy_limit
        if self.contacts_limit is not None:
            result['contactsLimit'] = self.contacts_limit
        if self.group_limit is not None:
            result['groupLimit'] = self.group_limit
        if self.sub_user_of_group_limit is not None:
            result['subUserOfGroupLimit'] = self.sub_user_of_group_limit
        if self.group_max_attach_policy_limit is not None:
            result['groupMaxAttachPolicyLimit'] = self.group_max_attach_policy_limit
        if self.user_role_per_account_limit is not None:
            result['userRolePerAccountLimit'] = self.user_role_per_account_limit
        if self.role_max_attach_system_policy_limit is not None:
            result['roleMaxAttachSystemPolicyLimit'] = self.role_max_attach_system_policy_limit
        if self.role_max_attach_custom_policy_limit is not None:
            result['roleMaxAttachCustomPolicyLimit'] = self.role_max_attach_custom_policy_limit
        if self.aksk_limit is not None:
            result['akskLimit'] = self.aksk_limit
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AccountLimitInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userLimit') is not None:
            self.user_limit = m.get('userLimit')
        if m.get('policyLimit') is not None:
            self.policy_limit = m.get('policyLimit')
        if m.get('contactsLimit') is not None:
            self.contacts_limit = m.get('contactsLimit')
        if m.get('groupLimit') is not None:
            self.group_limit = m.get('groupLimit')
        if m.get('subUserOfGroupLimit') is not None:
            self.sub_user_of_group_limit = m.get('subUserOfGroupLimit')
        if m.get('groupMaxAttachPolicyLimit') is not None:
            self.group_max_attach_policy_limit = m.get('groupMaxAttachPolicyLimit')
        if m.get('userRolePerAccountLimit') is not None:
            self.user_role_per_account_limit = m.get('userRolePerAccountLimit')
        if m.get('roleMaxAttachSystemPolicyLimit') is not None:
            self.role_max_attach_system_policy_limit = m.get('roleMaxAttachSystemPolicyLimit')
        if m.get('roleMaxAttachCustomPolicyLimit') is not None:
            self.role_max_attach_custom_policy_limit = m.get('roleMaxAttachCustomPolicyLimit')
        if m.get('akskLimit') is not None:
            self.aksk_limit = m.get('akskLimit')
        return self
