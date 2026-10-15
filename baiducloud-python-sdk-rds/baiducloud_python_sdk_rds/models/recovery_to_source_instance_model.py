"""
RecoveryToSourceInstanceModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rds.models.table import Table


class RecoveryToSourceInstanceModel(AbstractModel):
    """
    RecoveryToSourceInstanceModel
    """

    def __init__(self, restore_mode=None, db_name=None, new_dbname=None, tables=None):
        """
        Initialize RecoveryToSourceInstanceModel instance.

        :param restore_mode: 表示恢复模式，支持database和table两种
        :type restore_mode: str (optional)

        :param db_name: 要恢复库的名称
        :type db_name: str (optional)

        :param new_dbname: 表示恢复后库的名称
        :type new_dbname: str (optional)

        :param tables: 表示恢复后库的名称
        :type tables: List[Table] (optional)
        """
        super().__init__()
        self.restore_mode = restore_mode
        self.db_name = db_name
        self.new_dbname = new_dbname
        self.tables = tables

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
        if self.restore_mode is not None:
            result['restoreMode'] = self.restore_mode
        if self.db_name is not None:
            result['dbName'] = self.db_name
        if self.new_dbname is not None:
            result['newDbname'] = self.new_dbname
        if self.tables is not None:
            result['tables'] = [i.to_dict() for i in self.tables]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RecoveryToSourceInstanceModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('restoreMode') is not None:
            self.restore_mode = m.get('restoreMode')
        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')
        if m.get('newDbname') is not None:
            self.new_dbname = m.get('newDbname')
        if m.get('tables') is not None:
            self.tables = [Table().from_dict(i) for i in m.get('tables')]
        return self
