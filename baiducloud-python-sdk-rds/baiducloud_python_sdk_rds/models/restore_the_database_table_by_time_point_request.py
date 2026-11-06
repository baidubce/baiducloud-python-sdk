"""
Request entity for RestoreTheDatabaseTableByTimePointRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_rds.models.recovery_to_source_instance_model import RecoveryToSourceInstanceModel
from baiducloud_python_sdk_rds.models.recovery_to_source_instance_table_model import RecoveryToSourceInstanceTableModel


class RestoreTheDatabaseTableByTimePointRequest(AbstractModel):
    """
    Request entity for RestoreTheDatabaseTableByTimePointRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        datetime,
        data,
        db_name,
        new_dbname,
        restore_mode,
        table_name,
        new_tablename,
        source_instance_id=None,
        target_instance_id=None,
        tables=None,
    ):
        """
        Initialize RestoreTheDatabaseTableByTimePointRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param source_instance_id: 与instanceId是一样的，此项不用填写
        :type source_instance_id: str (optional)

        :param target_instance_id: 要恢复的实例ID。 恢复到指定实例时，必填，值为指定的实例ID，如果恢复到原有实例，可以不写
        :type target_instance_id: str (optional)

        :param datetime: 备份时间点
        :type datetime: str (required)

        :param data: 要恢复的数据信息
        :type data: List[RecoveryToSourceInstanceModel] (required)

        :param db_name: 需要恢复的库名称
        :type db_name: str (required)

        :param new_dbname: new_dbname parameter
        :type new_dbname: str (required)

        :param restore_mode: 恢复模式，database（数据库），table（表）任选其一
        :type restore_mode: str (required)

        :param tables: 表的对象集合，当restoreMode为table必填项，恢复目标实例 为database必项为非填项
        :type tables: List[RecoveryToSourceInstanceTableModel] (optional)

        :param table_name: 需要恢复的表名
        :type table_name: str (required)

        :param new_tablename: 恢复后表名
        :type new_tablename: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.source_instance_id = source_instance_id
        self.target_instance_id = target_instance_id
        self.datetime = datetime
        self.data = data
        self.db_name = db_name
        self.new_dbname = new_dbname
        self.restore_mode = restore_mode
        self.tables = tables
        self.table_name = table_name
        self.new_tablename = new_tablename

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
        if self.source_instance_id is not None:
            result['sourceInstanceId'] = self.source_instance_id
        if self.target_instance_id is not None:
            result['targetInstanceId'] = self.target_instance_id
        if self.datetime is not None:
            result['datetime'] = self.datetime
        if self.data is not None:
            result['data'] = [i.to_dict() for i in self.data]
        if self.db_name is not None:
            result['dbName'] = self.db_name
        if self.new_dbname is not None:
            result['newDbname'] = self.new_dbname
        if self.restore_mode is not None:
            result['restoreMode'] = self.restore_mode
        if self.tables is not None:
            result['tables'] = [i.to_dict() for i in self.tables]
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.new_tablename is not None:
            result['newTablename'] = self.new_tablename
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RestoreTheDatabaseTableByTimePointRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('sourceInstanceId') is not None:
            self.source_instance_id = m.get('sourceInstanceId')
        if m.get('targetInstanceId') is not None:
            self.target_instance_id = m.get('targetInstanceId')
        if m.get('datetime') is not None:
            self.datetime = m.get('datetime')
        if m.get('data') is not None:
            self.data = [RecoveryToSourceInstanceModel().from_dict(i) for i in m.get('data')]
        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')
        if m.get('newDbname') is not None:
            self.new_dbname = m.get('newDbname')
        if m.get('restoreMode') is not None:
            self.restore_mode = m.get('restoreMode')
        if m.get('tables') is not None:
            self.tables = [RecoveryToSourceInstanceTableModel().from_dict(i) for i in m.get('tables')]
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('newTablename') is not None:
            self.new_tablename = m.get('newTablename')
        return self
