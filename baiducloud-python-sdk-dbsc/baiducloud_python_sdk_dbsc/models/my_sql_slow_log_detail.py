"""
MySQLSlowLogDetail information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MySQLSlowLogDetail(AbstractModel):
    """
    MySQLSlowLogDetail
    """

    def __init__(
        self,
        client_ip=None,
        client_port=None,
        user=None,
        connection_id=None,
        current_db=None,
        duration=None,
        lock_time=None,
        start=None,
        end=None,
        fingerprint=None,
        fingerprint_md5=None,
        method=None,
        query=None,
        affected_rows=None,
        scan_rows=None,
        return_rows=None,
        sql_type=None,
    ):
        """
        Initialize MySQLSlowLogDetail instance.

        :param client_ip: 客户端IP
        :type client_ip: str (optional)

        :param client_port: 客户端端口
        :type client_port: int (optional)

        :param user: 用户名称
        :type user: str (optional)

        :param connection_id: 会话ID
        :type connection_id: int (optional)

        :param current_db: 连接数据库名称
        :type current_db: str (optional)

        :param duration: SQL执行时间，单位毫秒
        :type duration: int (optional)

        :param lock_time: SQL锁时间
        :type lock_time: int (optional)

        :param start: SQL开始时间
        :type start: str (optional)

        :param end: SQL结束时间
        :type end: str (optional)

        :param fingerprint: 归一化SQL
        :type fingerprint: str (optional)

        :param fingerprint_md5: 归一化SQL指纹
        :type fingerprint_md5: str (optional)

        :param method: 方法名称
        :type method: str (optional)

        :param query: SQL语句
        :type query: str (optional)

        :param affected_rows: 影响行数
        :type affected_rows: int (optional)

        :param scan_rows: 扫描行数
        :type scan_rows: int (optional)

        :param return_rows: 返回行数
        :type return_rows: int (optional)

        :param sql_type: SQL类型：DMLDDL
        :type sql_type: str (optional)
        """
        super().__init__()
        self.client_ip = client_ip
        self.client_port = client_port
        self.user = user
        self.connection_id = connection_id
        self.current_db = current_db
        self.duration = duration
        self.lock_time = lock_time
        self.start = start
        self.end = end
        self.fingerprint = fingerprint
        self.fingerprint_md5 = fingerprint_md5
        self.method = method
        self.query = query
        self.affected_rows = affected_rows
        self.scan_rows = scan_rows
        self.return_rows = return_rows
        self.sql_type = sql_type

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
        if self.client_ip is not None:
            result['clientIp'] = self.client_ip
        if self.client_port is not None:
            result['clientPort'] = self.client_port
        if self.user is not None:
            result['user'] = self.user
        if self.connection_id is not None:
            result['connectionId'] = self.connection_id
        if self.current_db is not None:
            result['currentDB'] = self.current_db
        if self.duration is not None:
            result['duration'] = self.duration
        if self.lock_time is not None:
            result['lockTime'] = self.lock_time
        if self.start is not None:
            result['start'] = self.start
        if self.end is not None:
            result['end'] = self.end
        if self.fingerprint is not None:
            result['fingerprint'] = self.fingerprint
        if self.fingerprint_md5 is not None:
            result['fingerprintMd5'] = self.fingerprint_md5
        if self.method is not None:
            result['method'] = self.method
        if self.query is not None:
            result['query'] = self.query
        if self.affected_rows is not None:
            result['affectedRows'] = self.affected_rows
        if self.scan_rows is not None:
            result['scanRows'] = self.scan_rows
        if self.return_rows is not None:
            result['returnRows'] = self.return_rows
        if self.sql_type is not None:
            result['sqlType'] = self.sql_type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MySQLSlowLogDetail

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientIp') is not None:
            self.client_ip = m.get('clientIp')
        if m.get('clientPort') is not None:
            self.client_port = m.get('clientPort')
        if m.get('user') is not None:
            self.user = m.get('user')
        if m.get('connectionId') is not None:
            self.connection_id = m.get('connectionId')
        if m.get('currentDB') is not None:
            self.current_db = m.get('currentDB')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('lockTime') is not None:
            self.lock_time = m.get('lockTime')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('fingerprint') is not None:
            self.fingerprint = m.get('fingerprint')
        if m.get('fingerprintMd5') is not None:
            self.fingerprint_md5 = m.get('fingerprintMd5')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('affectedRows') is not None:
            self.affected_rows = m.get('affectedRows')
        if m.get('scanRows') is not None:
            self.scan_rows = m.get('scanRows')
        if m.get('returnRows') is not None:
            self.return_rows = m.get('returnRows')
        if m.get('sqlType') is not None:
            self.sql_type = m.get('sqlType')
        return self
