"""
Table information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Table(AbstractModel):
    """
    Table
    """

    def __init__(self, table_name=None, new_tablename=None):
        """
        Initialize Table instance.

        :param table_name: 需要恢复的表名
        :type table_name: str (optional)

        :param new_tablename: 恢复后表名
        :type new_tablename: str (optional)
        """
        super().__init__()
        self.table_name = table_name
        self.new_tablename = new_tablename

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
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.new_tablename is not None:
            result['newTablename'] = self.new_tablename
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Table

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('newTablename') is not None:
            self.new_tablename = m.get('newTablename')
        return self
