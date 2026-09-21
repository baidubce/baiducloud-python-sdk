"""
MysqlDatabaseSpaceModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MysqlDatabaseSpaceModel(AbstractModel):
    """
    MysqlDatabaseSpaceModel
    """

    def __init__(
        self,
        database_name=None,
        total_space=None,
        data_space=None,
        index_space=None,
        free_space=None,
        free_rate=None,
        usage_rate=None,
        rows=None,
        physical_space=None,
        table_count=None,
    ):
        """
        Initialize MysqlDatabaseSpaceModel instance.

        :param database_name: 数据库名称
        :type database_name: str (optional)

        :param total_space: 数据库总空间
        :type total_space: int (optional)

        :param data_space: 数据库数据空间
        :type data_space: int (optional)

        :param index_space: 数据库索引空间
        :type index_space: int (optional)

        :param free_space: 数据库可用空间
        :type free_space: int (optional)

        :param free_rate: 数据库可用空间占比（如\"0.0004\"）
        :type free_rate: float (optional)

        :param usage_rate: 数据库已用空间占比（如\"0.9996\"）
        :type usage_rate: float (optional)

        :param rows: 数据库总行数
        :type rows: int (optional)

        :param physical_space: 数据库物理空间
        :type physical_space: int (optional)

        :param table_count: 数据库表数量
        :type table_count: int (optional)
        """
        super().__init__()
        self.database_name = database_name
        self.total_space = total_space
        self.data_space = data_space
        self.index_space = index_space
        self.free_space = free_space
        self.free_rate = free_rate
        self.usage_rate = usage_rate
        self.rows = rows
        self.physical_space = physical_space
        self.table_count = table_count

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
        if self.database_name is not None:
            result['databaseName'] = self.database_name
        if self.total_space is not None:
            result['totalSpace'] = self.total_space
        if self.data_space is not None:
            result['dataSpace'] = self.data_space
        if self.index_space is not None:
            result['indexSpace'] = self.index_space
        if self.free_space is not None:
            result['freeSpace'] = self.free_space
        if self.free_rate is not None:
            result['freeRate'] = self.free_rate
        if self.usage_rate is not None:
            result['usageRate'] = self.usage_rate
        if self.rows is not None:
            result['rows'] = self.rows
        if self.physical_space is not None:
            result['physicalSpace'] = self.physical_space
        if self.table_count is not None:
            result['tableCount'] = self.table_count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MysqlDatabaseSpaceModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('databaseName') is not None:
            self.database_name = m.get('databaseName')
        if m.get('totalSpace') is not None:
            self.total_space = m.get('totalSpace')
        if m.get('dataSpace') is not None:
            self.data_space = m.get('dataSpace')
        if m.get('indexSpace') is not None:
            self.index_space = m.get('indexSpace')
        if m.get('freeSpace') is not None:
            self.free_space = m.get('freeSpace')
        if m.get('freeRate') is not None:
            self.free_rate = m.get('freeRate')
        if m.get('usageRate') is not None:
            self.usage_rate = m.get('usageRate')
        if m.get('rows') is not None:
            self.rows = m.get('rows')
        if m.get('physicalSpace') is not None:
            self.physical_space = m.get('physicalSpace')
        if m.get('tableCount') is not None:
            self.table_count = m.get('tableCount')
        return self
