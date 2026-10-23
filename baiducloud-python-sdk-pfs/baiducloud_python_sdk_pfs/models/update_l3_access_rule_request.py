"""
Request entity for UpdateL3AccessRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateL3AccessRuleRequest(AbstractModel):
    """
    Request entity for UpdateL3AccessRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        access_group_name,
        zone_name,
        access_rule_id,
        ip=None,
        mask=None,
        write_access=None,
        user_access=None,
        priority=None,
    ):
        """
        Initialize UpdateL3AccessRuleRequest request entity.

        :param access_group_name: 权限组名称（定位键）
        :type access_group_name: str (required)

        :param zone_name: 可用区名称（定位键）
        :type zone_name: str (required)

        :param access_rule_id: 要修改的访问规则 ID（定位键）
        :type access_rule_id: int (required)

        :param ip: IP 地址，例如 192.168.1.0
        :type ip: str (optional)

        :param mask: 子网掩码长度，例如 24
        :type mask: int (optional)

        :param write_access: 读写权限，read_only（只读）/ read_write（读写）
        :type write_access: str (optional)

        :param user_access: 用户权限，no_squash / root_squash / all_squash
        :type user_access: str (optional)

        :param priority: 规则优先级
        :type priority: int (optional)
        """
        super().__init__()
        self.access_group_name = access_group_name
        self.zone_name = zone_name
        self.access_rule_id = access_rule_id
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
        if self.access_group_name is not None:
            result['accessGroupName'] = self.access_group_name
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.access_rule_id is not None:
            result['accessRuleId'] = self.access_rule_id
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
        :rtype: UpdateL3AccessRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accessGroupName') is not None:
            self.access_group_name = m.get('accessGroupName')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('accessRuleId') is not None:
            self.access_rule_id = m.get('accessRuleId')
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
