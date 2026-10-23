"""
L3AccessRule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class L3AccessRule(AbstractModel):
    """
    L3AccessRule
    """

    def __init__(
        self,
        access_rule_id=None,
        ip=None,
        mask=None,
        priority=None,
        write_access=None,
        user_access=None,
    ):
        """
        Initialize L3AccessRule instance.

        :param access_rule_id: 规则 ID
        :type access_rule_id: int (optional)

        :param ip: 授权地址
        :type ip: str (optional)

        :param mask: 掩码位数
        :type mask: int (optional)

        :param priority: 优先级
        :type priority: int (optional)

        :param write_access: 读写权限
        :type write_access: str (optional)

        :param user_access: 用户权限
        :type user_access: str (optional)
        """
        super().__init__()
        self.access_rule_id = access_rule_id
        self.ip = ip
        self.mask = mask
        self.priority = priority
        self.write_access = write_access
        self.user_access = user_access

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
        if self.access_rule_id is not None:
            result['accessRuleId'] = self.access_rule_id
        if self.ip is not None:
            result['ip'] = self.ip
        if self.mask is not None:
            result['mask'] = self.mask
        if self.priority is not None:
            result['priority'] = self.priority
        if self.write_access is not None:
            result['writeAccess'] = self.write_access
        if self.user_access is not None:
            result['userAccess'] = self.user_access
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: L3AccessRule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accessRuleId') is not None:
            self.access_rule_id = m.get('accessRuleId')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('mask') is not None:
            self.mask = m.get('mask')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('writeAccess') is not None:
            self.write_access = m.get('writeAccess')
        if m.get('userAccess') is not None:
            self.user_access = m.get('userAccess')
        return self
