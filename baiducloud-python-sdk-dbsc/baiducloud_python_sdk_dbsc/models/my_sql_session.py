"""
MySQLSession information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MySQLSession(AbstractModel):
    """
    MySQLSession
    """

    def __init__(
        self,
        command=None,
        db=None,
        host=None,
        id=None,
        sqlstmt=None,
        state=None,
        time=None,
        trx_state=None,
        trx_time=None,
        user=None,
    ):
        """
        Initialize MySQLSession instance.

        :param command: 数据库线程命令
        :type command: str (optional)

        :param db: 数据库名称
        :type db: str (optional)

        :param host: 数据库IP:Port
        :type host: str (optional)

        :param id: 会话ID
        :type id: int (optional)

        :param sqlstmt: 执行的SQL
        :type sqlstmt: str (optional)

        :param state: 数据库线程状态
        :type state: str (optional)

        :param time: SQL执行时间
        :type time: int (optional)

        :param trx_state: 事务状态
        :type trx_state: str (optional)

        :param trx_time: 事务执行时间
        :type trx_time: int (optional)

        :param user: 数据库用户
        :type user: str (optional)
        """
        super().__init__()
        self.command = command
        self.db = db
        self.host = host
        self.id = id
        self.sqlstmt = sqlstmt
        self.state = state
        self.time = time
        self.trx_state = trx_state
        self.trx_time = trx_time
        self.user = user

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
        if self.command is not None:
            result['command'] = self.command
        if self.db is not None:
            result['db'] = self.db
        if self.host is not None:
            result['host'] = self.host
        if self.id is not None:
            result['id'] = self.id
        if self.sqlstmt is not None:
            result['sqlstmt'] = self.sqlstmt
        if self.state is not None:
            result['state'] = self.state
        if self.time is not None:
            result['time'] = self.time
        if self.trx_state is not None:
            result['trxState'] = self.trx_state
        if self.trx_time is not None:
            result['trxTime'] = self.trx_time
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MySQLSession

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('db') is not None:
            self.db = m.get('db')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('sqlstmt') is not None:
            self.sqlstmt = m.get('sqlstmt')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('trxState') is not None:
            self.trx_state = m.get('trxState')
        if m.get('trxTime') is not None:
            self.trx_time = m.get('trxTime')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self
