"""
SessionKillHistory information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SessionKillHistory(AbstractModel):
    """
    SessionKillHistory
    """

    def __init__(
        self,
        session_id=None,
        session_user=None,
        session_host=None,
        session_db=None,
        session_command=None,
        session_execute_time=None,
        session_state=None,
        session_sql=None,
        status=None,
        status_desc=None,
        status_info=None,
        operate_time=None,
    ):
        """
        Initialize SessionKillHistory instance.

        :param session_id: 会话ID
        :type session_id: int (optional)

        :param session_user: 会话连接用户
        :type session_user: str (optional)

        :param session_host: 会话客户端Host
        :type session_host: str (optional)

        :param session_db: 会话连接DB
        :type session_db: str (optional)

        :param session_command: 会话执行的命令类型
        :type session_command: str (optional)

        :param session_execute_time: 会话持续的时间，单位秒
        :type session_execute_time: int (optional)

        :param session_state: 会话状态
        :type session_state: str (optional)

        :param session_sql: 会话执行的SQL
        :type session_sql: str (optional)

        :param status: 查杀会话任务的状态值
        :type status: int (optional)

        :param status_desc: 查杀会话任务的状态描述
        :type status_desc: str (optional)

        :param status_info: 查杀会话任务的详情，一般查杀失败时会展示
        :type status_info: str (optional)

        :param operate_time: 操作时间
        :type operate_time: datetime (optional)
        """
        super().__init__()
        self.session_id = session_id
        self.session_user = session_user
        self.session_host = session_host
        self.session_db = session_db
        self.session_command = session_command
        self.session_execute_time = session_execute_time
        self.session_state = session_state
        self.session_sql = session_sql
        self.status = status
        self.status_desc = status_desc
        self.status_info = status_info
        self.operate_time = operate_time

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
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.session_user is not None:
            result['sessionUser'] = self.session_user
        if self.session_host is not None:
            result['sessionHost'] = self.session_host
        if self.session_db is not None:
            result['sessionDb'] = self.session_db
        if self.session_command is not None:
            result['sessionCommand'] = self.session_command
        if self.session_execute_time is not None:
            result['sessionExecuteTime'] = self.session_execute_time
        if self.session_state is not None:
            result['sessionState'] = self.session_state
        if self.session_sql is not None:
            result['sessionSql'] = self.session_sql
        if self.status is not None:
            result['status'] = self.status
        if self.status_desc is not None:
            result['statusDesc'] = self.status_desc
        if self.status_info is not None:
            result['statusInfo'] = self.status_info
        if self.operate_time is not None:
            result['operateTime'] = self.operate_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SessionKillHistory

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('sessionUser') is not None:
            self.session_user = m.get('sessionUser')
        if m.get('sessionHost') is not None:
            self.session_host = m.get('sessionHost')
        if m.get('sessionDb') is not None:
            self.session_db = m.get('sessionDb')
        if m.get('sessionCommand') is not None:
            self.session_command = m.get('sessionCommand')
        if m.get('sessionExecuteTime') is not None:
            self.session_execute_time = m.get('sessionExecuteTime')
        if m.get('sessionState') is not None:
            self.session_state = m.get('sessionState')
        if m.get('sessionSql') is not None:
            self.session_sql = m.get('sessionSql')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusDesc') is not None:
            self.status_desc = m.get('statusDesc')
        if m.get('statusInfo') is not None:
            self.status_info = m.get('statusInfo')
        if m.get('operateTime') is not None:
            self.operate_time = m.get('operateTime')
        return self
