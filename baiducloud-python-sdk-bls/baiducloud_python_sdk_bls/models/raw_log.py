"""
RawLog information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RawLog(AbstractModel):
    """
    RawLog
    """

    def __init__(self, project=None, log_store_name=None, query=None, columns=None, limit=None, logs=None):
        """
        Initialize RawLog instance.

        :param project: 日志集项目
        :type project: str (optional)

        :param log_store_name: 日志集名称
        :type log_store_name: str (optional)

        :param query: 查询语句
        :type query: str (optional)

        :param columns: 指定展示字段
        :type columns: List[str] (optional)

        :param limit: 展示的日志条数
        :type limit: int (optional)

        :param logs: 展示的日志原文
        :type logs: List[Dict[str, object]] (optional)
        """
        super().__init__()
        self.project = project
        self.log_store_name = log_store_name
        self.query = query
        self.columns = columns
        self.limit = limit
        self.logs = logs

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
        if self.project is not None:
            result['project'] = self.project
        if self.log_store_name is not None:
            result['logStoreName'] = self.log_store_name
        if self.query is not None:
            result['query'] = self.query
        if self.columns is not None:
            result['columns'] = self.columns
        if self.limit is not None:
            result['limit'] = self.limit
        if self.logs is not None:
            result['logs'] = self.logs

        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RawLog

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('columns') is not None:
            self.columns = m.get('columns')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('logs') is not None:
            self.logs = m.get('logs')

        return self
