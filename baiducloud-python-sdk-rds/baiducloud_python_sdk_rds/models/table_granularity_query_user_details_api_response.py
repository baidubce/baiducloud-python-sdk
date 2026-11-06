"""
Request entity for TableGranularityQueryUserDetailsApiResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rds.models.table_level_privilege_request import TableLevelPrivilegeRequest


class TableGranularityQueryUserDetailsApiResponse(BceResponse):
    """
    TableGranularityQueryUserDetailsApiResponse
    """

    def __init__(
        self, user=None, host=None, password=None, type=None, super_user_flag=None, remark=None, privilege=None
    ):
        """
        Initialize TableGranularityQueryUserDetailsApiResponse response.

        :param user: 账号名
        :type user: str (optional)

        :param host: 来源主机
        :type host: str (optional)

        :param password: 密码（一般不返回明文）
        :type password: str (optional)

        :param type: 账号类型
        :type type: str (optional)

        :param super_user_flag: 是否超级用户
        :type super_user_flag: str (optional)

        :param remark: 备注
        :type remark: str (optional)

        :param privilege: privilege field
        :type privilege: TableLevelPrivilegeRequest (optional)
        """
        super().__init__()
        self.user = user
        self.host = host
        self.password = password
        self.type = type
        self.super_user_flag = super_user_flag
        self.remark = remark
        self.privilege = privilege

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.user is not None:
            result['user'] = self.user
        if self.host is not None:
            result['host'] = self.host
        if self.password is not None:
            result['password'] = self.password
        if self.type is not None:
            result['type'] = self.type
        if self.super_user_flag is not None:
            result['superUserFlag'] = self.super_user_flag
        if self.remark is not None:
            result['remark'] = self.remark
        if self.privilege is not None:
            result['privilege'] = self.privilege.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TableGranularityQueryUserDetailsApiResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('user') is not None:
            self.user = m.get('user')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('superUserFlag') is not None:
            self.super_user_flag = m.get('superUserFlag')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('privilege') is not None:
            self.privilege = TableLevelPrivilegeRequest().from_dict(m.get('privilege'))
        return self
