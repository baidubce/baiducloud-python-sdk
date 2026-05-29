"""
Request entity for UpdatePermissionGroupRulesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdatePermissionGroupRulesRequest(AbstractModel):
    """
    Request entity for UpdatePermissionGroupRulesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, ag_name, ar_id, ip, mask, write_access, user_access, priority):
        """
        Initialize UpdatePermissionGroupRulesRequest request entity.

        :param ag_name: ag_name parameter
        :type ag_name: str (required)

        :param ar_id: ar_id parameter
        :type ar_id: str (required)

        :param ip: ip parameter
        :type ip: str (required)

        :param mask: 结合ip参数实现指定网段，如果单IP则设置为32（IPV4）或128（IPV6）
        :type mask: int (required)

        :param write_access: 读写规则，支持\"read_only\"表示只读, \"read_write\"表示读写
        :type write_access: str (required)

        :param user_access: user_access parameter
        :type user_access: str (required)

        :param priority: 规则优先级，优先级可选范围为1-100，1为最高优先级
        :type priority: int (required)
        """
        super().__init__()
        self.ag_name = ag_name
        self.ar_id = ar_id
        self.ip = ip
        self.mask = mask
        self.write_access = write_access
        self.user_access = user_access
        self.priority = priority

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
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdatePermissionGroupRulesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('agName') is not None:
            self.ag_name = m.get('agName')
        if m.get('arId') is not None:
            self.ar_id = m.get('arId')
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
