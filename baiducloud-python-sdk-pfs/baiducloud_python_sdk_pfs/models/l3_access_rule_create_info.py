"""
L3AccessRuleCreateInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class L3AccessRuleCreateInfo(AbstractModel):
    """
    L3AccessRuleCreateInfo
    """

    def __init__(self, ip, write_access, user_access, priority, mask=None):
        """
        Initialize L3AccessRuleCreateInfo instance.

        :param ip: 授权地址
        :type ip: str (required)

        :param write_access: 读写权限
        :type write_access: str (required)

        :param user_access: 用户权限
        :type user_access: str (required)

        :param priority: 优先级
        :type priority: int (required)

        :param mask: 掩码位数，未传时服务端按 IP 类型补默认值（IPv4 32，IPv6 128）
        :type mask: int (optional)
        """
        super().__init__()
        self.ip = ip
        self.write_access = write_access
        self.user_access = user_access
        self.priority = priority
        self.mask = mask

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
        if self.ip is not None:
            result['ip'] = self.ip
        if self.mask is not None:
            result['mask'] = self.mask
        if self.write_access is not None:
            result['writeAccess'] = self.write_access
        if self.user_access is not None:
            result['userAccess'] = self.user_access
        if self.priority is not None:
            result['priority'] = self.priority
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: L3AccessRuleCreateInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('mask') is not None:
            self.mask = m.get('mask')
        if m.get('writeAccess') is not None:
            self.write_access = m.get('writeAccess')
        if m.get('userAccess') is not None:
            self.user_access = m.get('userAccess')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        return self
