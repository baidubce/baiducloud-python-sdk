"""
RuleInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RuleInfo(AbstractModel):
    """
    RuleInfo
    """

    def __init__(self, ip=None, mask=None, write_access=None, user_access=None, priority=None):
        """
        Initialize RuleInfo instance.

        :param ip: ip attribute
        :type ip: str (optional)

        :param mask: 结合ip参数实现指定网段，如果单IP则设置为32（IPV4）或128（IPV6）
        :type mask: int (optional)

        :param write_access: 读写规则，支持\"read_only\"表示只读, \"read_write\"表示读写
        :type write_access: str (optional)

        :param user_access: user_access attribute
        :type user_access: str (optional)

        :param priority: 规则优先级，优先级可选范围为1-100，1为最高优先级
        :type priority: int (optional)
        """
        super().__init__()
        self.ip = ip
        self.mask = mask
        self.write_access = write_access
        self.user_access = user_access
        self.priority = priority

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
            result['write_access'] = self.write_access
        if self.user_access is not None:
            result['user_access'] = self.user_access
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
        :rtype: RuleInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('mask') is not None:
            self.mask = m.get('mask')
        if m.get('write_access') is not None:
            self.write_access = m.get('write_access')
        if m.get('user_access') is not None:
            self.user_access = m.get('user_access')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        return self
