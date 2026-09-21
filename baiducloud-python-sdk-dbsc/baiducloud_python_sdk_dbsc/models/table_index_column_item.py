"""
TableIndexColumnItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TableIndexColumnItem(AbstractModel):
    """
    TableIndexColumnItem
    """

    def __init__(self, column_name=None, sequence=None, collation=None, cardinality=None, nullable=None):
        """
        Initialize TableIndexColumnItem instance.

        :param column_name: 字段名称
        :type column_name: str (optional)

        :param sequence: 索引顺序
        :type sequence: int (optional)

        :param collation: 字段排序方式
        :type collation: str (optional)

        :param cardinality: 基数
        :type cardinality: int (optional)

        :param nullable: 字段是否为空
        :type nullable: str (optional)
        """
        super().__init__()
        self.column_name = column_name
        self.sequence = sequence
        self.collation = collation
        self.cardinality = cardinality
        self.nullable = nullable

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
        if self.column_name is not None:
            result['columnName'] = self.column_name
        if self.sequence is not None:
            result['sequence'] = self.sequence
        if self.collation is not None:
            result['collation'] = self.collation
        if self.cardinality is not None:
            result['cardinality'] = self.cardinality
        if self.nullable is not None:
            result['nullable'] = self.nullable
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TableIndexColumnItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('columnName') is not None:
            self.column_name = m.get('columnName')
        if m.get('sequence') is not None:
            self.sequence = m.get('sequence')
        if m.get('collation') is not None:
            self.collation = m.get('collation')
        if m.get('cardinality') is not None:
            self.cardinality = m.get('cardinality')
        if m.get('nullable') is not None:
            self.nullable = m.get('nullable')
        return self
