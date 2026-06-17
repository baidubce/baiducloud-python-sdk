"""
Request entity for UpdateAlarmPolicyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bls.models.log_store import LogStore
from baiducloud_python_sdk_bls.models.target import Target
from baiducloud_python_sdk_bls.models.trigger_condition import TriggerCondition
from baiducloud_python_sdk_bls.models.schedule import Schedule
from baiducloud_python_sdk_bls.models.notice import Notice
from baiducloud_python_sdk_bls.models.notice_raw_log import NoticeRawLog


class UpdateAlarmPolicyRequest(AbstractModel):
    """
    Request entity for UpdateAlarmPolicyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        name,
        targets,
        trigger_conditions,
        schedule,
        pending_count,
        notices,
        objects=None,
        groups=None,
        repeat_interval_minute=None,
        recover_without_notice=None,
        state=None,
        notice_state=None,
        notice_raw_logs=None,
    ):
        """
        Initialize UpdateAlarmPolicyRequest request entity.

        :param name: 报警策略名称，不能重复
        :type name: str (required)

        :param objects: 监控对象列表，当所有日志集共享目标日志集时，填写该字段
        :type objects: List[LogStore] (optional)

        :param targets: 执行语句列表
        :type targets: List[Target] (required)

        :param trigger_conditions: 触发条件列表
        :type trigger_conditions: List[TriggerCondition] (required)

        :param groups: 分组触发
        :type groups: List[str] (optional)

        :param schedule: schedule parameter
        :type schedule: Schedule (required)

        :param pending_count: 连续触发阈值，连续多少次触发阈值则报警
        :type pending_count: int (required)

        :param repeat_interval_minute: 重复报警间隔，单位：分钟，默认值：0，表示关闭重复报警
        :type repeat_interval_minute: int (optional)

        :param recover_without_notice: 恢复后是否通知 true：不通知， false：通知, 默认值为false
        :type recover_without_notice: bool (optional)

        :param state: 策略启用状态，ENABLED: 已启用， DISABLED: 已禁用
        :type state: str (optional)

        :param notice_state: 下通知启用状态，ENABLED: 已启用， DISABLED: 已禁用
        :type notice_state: str (optional)

        :param notices: notices parameter
        :type notices: List[Notice] (required)

        :param notice_raw_logs: 是否在报警通知中添加原始日志
        :type notice_raw_logs: List[NoticeRawLog] (optional)
        """
        super().__init__()
        self.name = name
        self.objects = objects
        self.targets = targets
        self.trigger_conditions = trigger_conditions
        self.groups = groups
        self.schedule = schedule
        self.pending_count = pending_count
        self.repeat_interval_minute = repeat_interval_minute
        self.recover_without_notice = recover_without_notice
        self.state = state
        self.notice_state = notice_state
        self.notices = notices
        self.notice_raw_logs = notice_raw_logs

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.objects is not None:
            result['objects'] = [i.to_dict() for i in self.objects]
        if self.targets is not None:
            result['targets'] = [i.to_dict() for i in self.targets]
        if self.trigger_conditions is not None:
            result['triggerConditions'] = [i.to_dict() for i in self.trigger_conditions]
        if self.groups is not None:
            result['groups'] = self.groups
        if self.schedule is not None:
            result['schedule'] = self.schedule.to_dict()
        if self.pending_count is not None:
            result['pendingCount'] = self.pending_count
        if self.repeat_interval_minute is not None:
            result['repeatIntervalMinute'] = self.repeat_interval_minute
        if self.recover_without_notice is not None:
            result['recoverWithoutNotice'] = self.recover_without_notice
        if self.state is not None:
            result['state'] = self.state
        if self.notice_state is not None:
            result['noticeState'] = self.notice_state
        if self.notices is not None:
            result['notices'] = [i.to_dict() for i in self.notices]
        if self.notice_raw_logs is not None:
            result['noticeRawLogs'] = [i.to_dict() for i in self.notice_raw_logs]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateAlarmPolicyRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('objects') is not None:
            self.objects = [LogStore().from_dict(i) for i in m.get('objects')]
        if m.get('targets') is not None:
            self.targets = [Target().from_dict(i) for i in m.get('targets')]
        if m.get('triggerConditions') is not None:
            self.trigger_conditions = [TriggerCondition().from_dict(i) for i in m.get('triggerConditions')]
        if m.get('groups') is not None:
            self.groups = m.get('groups')
        if m.get('schedule') is not None:
            self.schedule = Schedule().from_dict(m.get('schedule'))
        if m.get('pendingCount') is not None:
            self.pending_count = m.get('pendingCount')
        if m.get('repeatIntervalMinute') is not None:
            self.repeat_interval_minute = m.get('repeatIntervalMinute')
        if m.get('recoverWithoutNotice') is not None:
            self.recover_without_notice = m.get('recoverWithoutNotice')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('noticeState') is not None:
            self.notice_state = m.get('noticeState')
        if m.get('notices') is not None:
            self.notices = [Notice().from_dict(i) for i in m.get('notices')]
        if m.get('noticeRawLogs') is not None:
            self.notice_raw_logs = [NoticeRawLog().from_dict(i) for i in m.get('noticeRawLogs')]
        return self
