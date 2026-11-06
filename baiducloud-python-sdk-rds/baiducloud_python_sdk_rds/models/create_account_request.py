"""
Request entity for CreateAccountRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_rds.models.database_privilege import DatabasePrivilege


class CreateAccountRequest(AbstractModel):
    """
    Request entity for CreateAccountRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, instance_id, account_name, password, account_type=None, database_privileges=None, desc=None, type=None
    ):
        """
        Initialize CreateAccountRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param account_name: 账号名称，不能为保留关键字，由小写字母、数字、下划线组成、字母开头，字母或数字结尾，最长16个字符。
        :type account_name: str (required)

        :param password: 账号的密码，由字母、数字或下划线组成，长度6～32位。 密码需要加密传输，禁止明文传输，详情请参考密码加密传输规范定义
        :type password: str (required)

        :param account_type: 账号权限类型 Common：普通账号,Super：super账号。不传递此参数默认:普通账号详情参考
        :type account_type: str (optional)

        :param database_privileges: MySQL和SQL Server实例可设置此项
        :type database_privileges: List[DatabasePrivilege] (optional)

        :param desc: 账号的描述信息
        :type desc: str (optional)

        :param type: type parameter
        :type type: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.account_name = account_name
        self.password = password
        self.account_type = account_type
        self.database_privileges = database_privileges
        self.desc = desc
        self.type = type

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
        if self.account_name is not None:
            result['accountName'] = self.account_name
        if self.password is not None:
            result['password'] = self.password
        if self.account_type is not None:
            result['accountType'] = self.account_type
        if self.database_privileges is not None:
            result['databasePrivileges'] = [i.to_dict() for i in self.database_privileges]
        if self.desc is not None:
            result['desc'] = self.desc
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAccountRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('accountType') is not None:
            self.account_type = m.get('accountType')
        if m.get('databasePrivileges') is not None:
            self.database_privileges = [DatabasePrivilege().from_dict(i) for i in m.get('databasePrivileges')]
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self
