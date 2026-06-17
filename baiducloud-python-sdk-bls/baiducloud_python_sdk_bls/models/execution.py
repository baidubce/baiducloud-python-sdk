"""
Execution information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bls.models.notice import Notice

from baiducloud_python_sdk_bls.models.raw_log import RawLog


class Execution(AbstractModel):
    """
    Execution
    """

    def __init__(
        self, time=None, state=None, notice_state=None, reason=None, values=None, notices=None, raw_logs=None
    ):
        """
        Initialize Execution instance.

        :param time: 执行时间，UTC时间
        :type time: str (optional)

        :param state: 执行状态，取值：OK: 恢复正常, ALERT: 报警中
        :type state: str (optional)

        :param notice_state: 通知状态，取值：NOT_SENT: 未通知, SENT: 已通知，FAIL: 通知发送失败
        :type notice_state: str (optional)

        :param reason: 若发送失败，填写失败原因
        :type reason: str (optional)

        :param values: 触发报警时的查询结果数据
        :type values: Dict[str, object] (optional)

        :param notices: notices attribute
        :type notices: List[Notice] (optional)

        :param raw_logs: 报警通知中原始日志
        :type raw_logs: List[RawLog] (optional)
        """
        super().__init__()
        self.time = time
        self.state = state
        self.notice_state = notice_state
        self.reason = reason
        self.values = values
        self.notices = notices
        self.raw_logs = raw_logs

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
        if self.time is not None:
            result['time'] = self.time
        if self.state is not None:
            result['state'] = self.state
        if self.notice_state is not None:
            result['noticeState'] = self.notice_state
        if self.reason is not None:
            result['reason'] = self.reason
        if self.values is not None:
            result['values'] = self.values
        if self.notices is not None:
            result['notices'] = [i.to_dict() for i in self.notices]
        if self.raw_logs is not None:
            result['rawLogs'] = [i.to_dict() for i in self.raw_logs]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Execution

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('noticeState') is not None:
            self.notice_state = m.get('noticeState')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('values') is not None:
            self.values = m.get('values')
        if m.get('notices') is not None:
            self.notices = [Notice().from_dict(i) for i in m.get('notices')]
        if m.get('rawLogs') is not None:
            self.raw_logs = [RawLog().from_dict(i) for i in m.get('rawLogs')]
        return self
