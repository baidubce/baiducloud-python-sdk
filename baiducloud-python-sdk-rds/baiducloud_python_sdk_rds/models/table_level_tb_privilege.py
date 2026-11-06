"""
TableLevelTbPrivilege information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TableLevelTbPrivilege(AbstractModel):
    """
    TableLevelTbPrivilege
    """

    def __init__(self, db=None, table=None, privs=None):
        """
        Initialize TableLevelTbPrivilege instance.

        :param db: 数据库名
        :type db: str (optional)

        :param table: 表名
        :type table: str (optional)

        :param privs: 该表授予的权限项列表
        :type privs: List[str] (optional)
        """
        super().__init__()
        self.db = db
        self.table = table
        self.privs = privs

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
        if self.db is not None:
            result['db'] = self.db
        if self.table is not None:
            result['table'] = self.table
        if self.privs is not None:
            result['privs'] = self.privs
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TableLevelTbPrivilege

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('db') is not None:
            self.db = m.get('db')
        if m.get('table') is not None:
            self.table = m.get('table')
        if m.get('privs') is not None:
            self.privs = m.get('privs')
        return self
