"""
ResultSet information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ResultSet(AbstractModel):
    """
    ResultSet
    """

    def __init__(self, query_type=None, columns=None, column_types=None, rows=None):
        """
        Initialize ResultSet instance.

        :param query_type: 查询类型
        :type query_type: str (optional)

        :param columns: 列名列表
        :type columns: List[str] (optional)

        :param column_types: 列类型列表
        :type column_types: List[str] (optional)

        :param rows: 结果行数据
        :type rows: List[List[object]] (optional)
        """
        super().__init__()
        self.query_type = query_type
        self.columns = columns
        self.column_types = column_types
        self.rows = rows

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
        if self.query_type is not None:
            result['queryType'] = self.query_type
        if self.columns is not None:
            result['columns'] = self.columns
        if self.column_types is not None:
            result['columnTypes'] = self.column_types
        if self.rows is not None:
            result['rows'] = self.rows
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ResultSet

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('queryType') is not None:
            self.query_type = m.get('queryType')
        if m.get('columns') is not None:
            self.columns = m.get('columns')
        if m.get('columnTypes') is not None:
            self.column_types = m.get('columnTypes')
        if m.get('rows') is not None:
            self.rows = m.get('rows')
        return self
