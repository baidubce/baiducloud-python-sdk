"""
Request entity for GetMysqlActiveSessionsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_dbsc.models.my_sql_session import MySQLSession
from baiducloud_python_sdk_dbsc.models.mysql_session_db_summary import MysqlSessionDBSummary
from baiducloud_python_sdk_dbsc.models.mysql_session_host_summary import MysqlSessionHostSummary
from baiducloud_python_sdk_dbsc.models.mysql_session_user_summary import MysqlSessionUserSummary
from baiducloud_python_sdk_dbsc.models.my_sql_session_summary import MySQLSessionSummary


class GetMysqlActiveSessionsResponse(BceResponse):
    """
    GetMysqlActiveSessionsResponse
    """

    def __init__(self, items=None, database_statistics=None, host_statistics=None, user_statistics=None, summary=None):
        """
        Initialize GetMysqlActiveSessionsResponse response.

        :param items: 实时会话列表信息
        :type items: List[MySQLSession] (optional)

        :param database_statistics: 数据库统计信息
        :type database_statistics: List[MysqlSessionDBSummary] (optional)

        :param host_statistics: 源端Host统计信息
        :type host_statistics: List[MysqlSessionHostSummary] (optional)

        :param user_statistics: 用户统计信息
        :type user_statistics: List[MysqlSessionUserSummary] (optional)

        :param summary: 整体统计信息
        :type summary: List[MySQLSessionSummary] (optional)
        """
        super().__init__()
        self.items = items
        self.database_statistics = database_statistics
        self.host_statistics = host_statistics
        self.user_statistics = user_statistics
        self.summary = summary

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.items is not None:
            result['items'] = [i.to_dict() for i in self.items]
        if self.database_statistics is not None:
            result['databaseStatistics'] = [i.to_dict() for i in self.database_statistics]
        if self.host_statistics is not None:
            result['hostStatistics'] = [i.to_dict() for i in self.host_statistics]
        if self.user_statistics is not None:
            result['userStatistics'] = [i.to_dict() for i in self.user_statistics]
        if self.summary is not None:
            result['summary'] = [i.to_dict() for i in self.summary]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetMysqlActiveSessionsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('items') is not None:
            self.items = [MySQLSession().from_dict(i) for i in m.get('items')]
        if m.get('databaseStatistics') is not None:
            self.database_statistics = [MysqlSessionDBSummary().from_dict(i) for i in m.get('databaseStatistics')]
        if m.get('hostStatistics') is not None:
            self.host_statistics = [MysqlSessionHostSummary().from_dict(i) for i in m.get('hostStatistics')]
        if m.get('userStatistics') is not None:
            self.user_statistics = [MysqlSessionUserSummary().from_dict(i) for i in m.get('userStatistics')]
        if m.get('summary') is not None:
            self.summary = [MySQLSessionSummary().from_dict(i) for i in m.get('summary')]
        return self
