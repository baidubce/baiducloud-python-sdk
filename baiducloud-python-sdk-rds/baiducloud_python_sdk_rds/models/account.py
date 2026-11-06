"""
Account information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rds.models.database_privilege import DatabasePrivilege


class Account(AbstractModel):
    """
    Account
    """

    def __init__(
        self,
        account_name=None,
        database_privileges=None,
        type=None,
        account_status=None,
        super_user_flag=None,
        account_type=None,
        desc=None,
        status=None,
        e_tag=None,
    ):
        """
        Initialize Account instance.

        :param account_name: 账号名称，不能为保留关键字
        :type account_name: str (optional)

        :param database_privileges: MySQL和SQL Server实例可设置此项
        :type database_privileges: List[DatabasePrivilege] (optional)

        :param type: type attribute
        :type type: str (optional)

        :param account_status: 账号状态，同status
        :type account_status: str (optional)

        :param super_user_flag: 同accountType字段值
        :type super_user_flag: str (optional)

        :param account_type: 账号权限类型。 Common：普通账号,Super：super账号。默认为普通账号，详情参考
        :type account_type: str (optional)

        :param desc: 账号的描述信息
        :type desc: str (optional)

        :param status: 账号状态，Available：可用
        :type status: str (optional)

        :param e_tag: 账号操作时间， 如：\"2023-07-28 02:45:53\"
        :type e_tag: str (optional)
        """
        super().__init__()
        self.account_name = account_name
        self.database_privileges = database_privileges
        self.type = type
        self.account_status = account_status
        self.super_user_flag = super_user_flag
        self.account_type = account_type
        self.desc = desc
        self.status = status
        self.e_tag = e_tag

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
        if self.account_name is not None:
            result['accountName'] = self.account_name
        if self.database_privileges is not None:
            result['databasePrivileges'] = [i.to_dict() for i in self.database_privileges]
        if self.type is not None:
            result['type'] = self.type
        if self.account_status is not None:
            result['accountStatus'] = self.account_status
        if self.super_user_flag is not None:
            result['superUserFlag'] = self.super_user_flag
        if self.account_type is not None:
            result['accountType'] = self.account_type
        if self.desc is not None:
            result['desc'] = self.desc
        if self.status is not None:
            result['status'] = self.status
        if self.e_tag is not None:
            result['ETag'] = self.e_tag
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Account

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')
        if m.get('databasePrivileges') is not None:
            self.database_privileges = [DatabasePrivilege().from_dict(i) for i in m.get('databasePrivileges')]
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('accountStatus') is not None:
            self.account_status = m.get('accountStatus')
        if m.get('superUserFlag') is not None:
            self.super_user_flag = m.get('superUserFlag')
        if m.get('accountType') is not None:
            self.account_type = m.get('accountType')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('ETag') is not None:
            self.e_tag = m.get('ETag')
        return self
