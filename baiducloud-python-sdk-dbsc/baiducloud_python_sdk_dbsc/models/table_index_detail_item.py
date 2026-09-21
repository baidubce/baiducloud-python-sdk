"""
TableIndexDetailItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_dbsc.models.table_index_column_item import TableIndexColumnItem


class TableIndexDetailItem(AbstractModel):
    """
    TableIndexDetailItem
    """

    def __init__(
        self,
        schema_name=None,
        table_name=None,
        index_name=None,
        column_name=None,
        non_unique=None,
        index_type=None,
        comment=None,
        columns=None,
    ):
        """
        Initialize TableIndexDetailItem instance.

        :param schema_name: 数据库名称
        :type schema_name: str (optional)

        :param table_name: 表名称
        :type table_name: str (optional)

        :param index_name: 索引名称
        :type index_name: str (optional)

        :param column_name: 索引包含的字段名称（以逗号分隔）
        :type column_name: str (optional)

        :param non_unique: 是否唯一索引（0=唯一索引,1=非唯一索引）
        :type non_unique: int (optional)

        :param index_type: 索引类型（如BTREE、HASH等）
        :type index_type: str (optional)

        :param comment: 索引注释
        :type comment: str (optional)

        :param columns: 索引字段详情列表
        :type columns: List[TableIndexColumnItem] (optional)
        """
        super().__init__()
        self.schema_name = schema_name
        self.table_name = table_name
        self.index_name = index_name
        self.column_name = column_name
        self.non_unique = non_unique
        self.index_type = index_type
        self.comment = comment
        self.columns = columns

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
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.index_name is not None:
            result['indexName'] = self.index_name
        if self.column_name is not None:
            result['columnName'] = self.column_name
        if self.non_unique is not None:
            result['nonUnique'] = self.non_unique
        if self.index_type is not None:
            result['indexType'] = self.index_type
        if self.comment is not None:
            result['comment'] = self.comment
        if self.columns is not None:
            result['columns'] = [i.to_dict() for i in self.columns]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TableIndexDetailItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        if m.get('columnName') is not None:
            self.column_name = m.get('columnName')
        if m.get('nonUnique') is not None:
            self.non_unique = m.get('nonUnique')
        if m.get('indexType') is not None:
            self.index_type = m.get('indexType')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('columns') is not None:
            self.columns = [TableIndexColumnItem().from_dict(i) for i in m.get('columns')]
        return self
