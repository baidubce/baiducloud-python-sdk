"""
SCSSlowLogInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SCSSlowLogInfo(AbstractModel):
    """
    SCSSlowLogInfo
    """

    def __init__(
        self,
        content=None,
        log_duration=None,
        log_key=None,
        log_sql=None,
        log_time=None,
        slow_log_id=None,
        client_ip=None,
    ):
        """
        Initialize SCSSlowLogInfo instance.

        :param content: 慢日志内容
        :type content: str (optional)

        :param log_duration: 执行耗时（单位：微妙）
        :type log_duration: int (optional)

        :param log_key: 操作的key
        :type log_key: str (optional)

        :param log_sql: 命令
        :type log_sql: str (optional)

        :param log_time: 生成日志时间
        :type log_time: str (optional)

        :param slow_log_id: 慢日志ID
        :type slow_log_id: int (optional)

        :param client_ip: IP地址以及端口号
        :type client_ip: str (optional)
        """
        super().__init__()
        self.content = content
        self.log_duration = log_duration
        self.log_key = log_key
        self.log_sql = log_sql
        self.log_time = log_time
        self.slow_log_id = slow_log_id
        self.client_ip = client_ip

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
        if self.content is not None:
            result['content'] = self.content
        if self.log_duration is not None:
            result['logDuration'] = self.log_duration
        if self.log_key is not None:
            result['logKey'] = self.log_key
        if self.log_sql is not None:
            result['logSql'] = self.log_sql
        if self.log_time is not None:
            result['logTime'] = self.log_time
        if self.slow_log_id is not None:
            result['slowLogId'] = self.slow_log_id
        if self.client_ip is not None:
            result['clientIp'] = self.client_ip
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SCSSlowLogInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('logDuration') is not None:
            self.log_duration = m.get('logDuration')
        if m.get('logKey') is not None:
            self.log_key = m.get('logKey')
        if m.get('logSql') is not None:
            self.log_sql = m.get('logSql')
        if m.get('logTime') is not None:
            self.log_time = m.get('logTime')
        if m.get('slowLogId') is not None:
            self.slow_log_id = m.get('slowLogId')
        if m.get('clientIp') is not None:
            self.client_ip = m.get('clientIp')
        return self
