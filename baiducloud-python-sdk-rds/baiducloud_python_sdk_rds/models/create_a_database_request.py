"""
Request entity for CreateADatabaseRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_rds.models.account_privilege import AccountPrivilege


class CreateADatabaseRequest(AbstractModel):
    """
    Request entity for CreateADatabaseRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        character_set_name,
        db_name,
        remark=None,
        account_privileges=None,
        ctype=None,
        collate=None,
        owner=None,
    ):
        """
        Initialize CreateADatabaseRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param character_set_name: character_set_name parameter
        :type character_set_name: str (required)

        :param db_name: db_name parameter
        :type db_name: str (required)

        :param remark: 备注
        :type remark: str (optional)

        :param account_privileges: 账户权限由 [AccountPrivilege](#AccountPrivilege) 对象组成
        :type account_privileges: List[AccountPrivilege] (optional)

        :param ctype: ctype parameter
        :type ctype: str (optional)

        :param collate: collate parameter
        :type collate: str (optional)

        :param owner: 授权账号
        :type owner: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.character_set_name = character_set_name
        self.db_name = db_name
        self.remark = remark
        self.account_privileges = account_privileges
        self.ctype = ctype
        self.collate = collate
        self.owner = owner

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
        if self.character_set_name is not None:
            result['characterSetName'] = self.character_set_name
        if self.db_name is not None:
            result['dbName'] = self.db_name
        if self.remark is not None:
            result['remark'] = self.remark
        if self.account_privileges is not None:
            result['accountPrivileges'] = [i.to_dict() for i in self.account_privileges]
        if self.ctype is not None:
            result['ctype'] = self.ctype
        if self.collate is not None:
            result['collate'] = self.collate
        if self.owner is not None:
            result['owner'] = self.owner
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateADatabaseRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('characterSetName') is not None:
            self.character_set_name = m.get('characterSetName')
        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('accountPrivileges') is not None:
            self.account_privileges = [AccountPrivilege().from_dict(i) for i in m.get('accountPrivileges')]
        if m.get('ctype') is not None:
            self.ctype = m.get('ctype')
        if m.get('collate') is not None:
            self.collate = m.get('collate')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        return self
