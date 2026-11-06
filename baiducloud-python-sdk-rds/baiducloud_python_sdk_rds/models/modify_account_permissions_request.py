"""
Request entity for ModifyAccountPermissionsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_rds.models.database_privilege import DatabasePrivilege


class ModifyAccountPermissionsRequest(AbstractModel):
    """
    Request entity for ModifyAccountPermissionsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, account_name, database_privileges):
        """
        Initialize ModifyAccountPermissionsRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param account_name: account_name parameter
        :type account_name: str (required)

        :param database_privileges: 具体的数据库权，为具体的一个库添加权限。MySQL和SQL Server实例可设置此项。
        :type database_privileges: List[DatabasePrivilege] (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.account_name = account_name
        self.database_privileges = database_privileges

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
        if self.database_privileges is not None:
            result['databasePrivileges'] = [i.to_dict() for i in self.database_privileges]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyAccountPermissionsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')
        if m.get('databasePrivileges') is not None:
            self.database_privileges = [DatabasePrivilege().from_dict(i) for i in m.get('databasePrivileges')]
        return self
