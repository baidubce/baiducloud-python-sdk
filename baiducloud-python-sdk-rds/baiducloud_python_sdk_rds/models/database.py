"""
Database information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rds.models.account_privilege import AccountPrivilege


class Database(AbstractModel):
    """
    Database
    """

    def __init__(
        self, db_name=None, character_set_name=None, account_privileges=None, collate=None, ctype=None, owner=None
    ):
        """
        Initialize Database instance.

        :param db_name: 数据库名称
        :type db_name: str (optional)

        :param character_set_name: 支持字符集。UTF8，LATIN1，SQL\\_ASCII
        :type character_set_name: str (optional)

        :param account_privileges: 账户权限由[AccountPrivilege](#AccountPrivilege)对象组成
        :type account_privileges: List[AccountPrivilege] (optional)

        :param collate: collate attribute
        :type collate: str (optional)

        :param ctype: ctype attribute
        :type ctype: str (optional)

        :param owner: 授权账号
        :type owner: str (optional)
        """
        super().__init__()
        self.db_name = db_name
        self.character_set_name = character_set_name
        self.account_privileges = account_privileges
        self.collate = collate
        self.ctype = ctype
        self.owner = owner

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
        if self.db_name is not None:
            result['dbName'] = self.db_name
        if self.character_set_name is not None:
            result['characterSetName'] = self.character_set_name
        if self.account_privileges is not None:
            result['accountPrivileges'] = [i.to_dict() for i in self.account_privileges]
        if self.collate is not None:
            result['collate'] = self.collate
        if self.ctype is not None:
            result['ctype'] = self.ctype
        if self.owner is not None:
            result['owner'] = self.owner
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Database

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')
        if m.get('characterSetName') is not None:
            self.character_set_name = m.get('characterSetName')
        if m.get('accountPrivileges') is not None:
            self.account_privileges = [AccountPrivilege().from_dict(i) for i in m.get('accountPrivileges')]
        if m.get('collate') is not None:
            self.collate = m.get('collate')
        if m.get('ctype') is not None:
            self.ctype = m.get('ctype')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        return self
