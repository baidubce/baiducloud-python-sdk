"""
Policy information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bls.models.log_store import LogStore

from baiducloud_python_sdk_bls.models.target import Target

from baiducloud_python_sdk_bls.models.trigger_condition import TriggerCondition

from baiducloud_python_sdk_bls.models.schedule import Schedule

from baiducloud_python_sdk_bls.models.notice import Notice

from baiducloud_python_sdk_bls.models.notice_raw_log import NoticeRawLog


class Policy(AbstractModel):
    """
    Policy
    """

    def __init__(
        self,
        name=None,
        id=None,
        state=None,
        notice_state=None,
        created_time=None,
        updated_time=None,
        objects=None,
        targets=None,
        trigger_conditions=None,
        groups=None,
        schedule=None,
        pending_count=None,
        repeat_interval_minute=None,
        recover_alarm_notice=None,
        notices=None,
        notice_with_raw_log=None,
        notice_raw_configs=None,
    ):
        """
        Initialize Policy instance.

        :param name: 报警策略名称，同user下唯一
        :type name: str (optional)

        :param id: 策略ID，同user下唯一
        :type id: str (optional)

        :param state: 策略启用状态
        :type state: str (optional)

        :param notice_state: 通知启用状态
        :type notice_state: str (optional)

        :param created_time: 创建时间，UTC时间
        :type created_time: str (optional)

        :param updated_time: 更新时间，UTC时间
        :type updated_time: str (optional)

        :param objects: 监控对象列表
        :type objects: List[LogStore] (optional)

        :param targets: 执行语句列表
        :type targets: List[Target] (optional)

        :param trigger_conditions: 触发条件列表
        :type trigger_conditions: List[TriggerCondition] (optional)

        :param groups: 分组触发
        :type groups: List[str] (optional)

        :param schedule: schedule attribute
        :type schedule: Schedule (optional)

        :param pending_count: 连续触发阈值
        :type pending_count: int (optional)

        :param repeat_interval_minute: 重复报警间隔，单位：分钟
        :type repeat_interval_minute: int (optional)

        :param recover_alarm_notice: 恢复后是否通知
        :type recover_alarm_notice: bool (optional)

        :param notices: 报警通知模板列表
        :type notices: List[Notice] (optional)

        :param notice_with_raw_log: 报警内容是否增加日志原文
        :type notice_with_raw_log: bool (optional)

        :param notice_raw_configs: 报警通知内容配置
        :type notice_raw_configs: List[NoticeRawLog] (optional)
        """
        super().__init__()
        self.name = name
        self.id = id
        self.state = state
        self.notice_state = notice_state
        self.created_time = created_time
        self.updated_time = updated_time
        self.objects = objects
        self.targets = targets
        self.trigger_conditions = trigger_conditions
        self.groups = groups
        self.schedule = schedule
        self.pending_count = pending_count
        self.repeat_interval_minute = repeat_interval_minute
        self.recover_alarm_notice = recover_alarm_notice
        self.notices = notices
        self.notice_with_raw_log = notice_with_raw_log
        self.notice_raw_configs = notice_raw_configs

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
        if self.name is not None:
            result['name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        if self.state is not None:
            result['state'] = self.state
        if self.notice_state is not None:
            result['noticeState'] = self.notice_state
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.updated_time is not None:
            result['updatedTime'] = self.updated_time
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
        if self.recover_alarm_notice is not None:
            result['recoverAlarmNotice'] = self.recover_alarm_notice
        if self.notices is not None:
            result['notices'] = [i.to_dict() for i in self.notices]
        if self.notice_with_raw_log is not None:
            result['noticeWithRawLog'] = self.notice_with_raw_log
        if self.notice_raw_configs is not None:
            result['noticeRawConfigs'] = [i.to_dict() for i in self.notice_raw_configs]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Policy

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('noticeState') is not None:
            self.notice_state = m.get('noticeState')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')
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
        if m.get('recoverAlarmNotice') is not None:
            self.recover_alarm_notice = m.get('recoverAlarmNotice')
        if m.get('notices') is not None:
            self.notices = [Notice().from_dict(i) for i in m.get('notices')]
        if m.get('noticeWithRawLog') is not None:
            self.notice_with_raw_log = m.get('noticeWithRawLog')
        if m.get('noticeRawConfigs') is not None:
            self.notice_raw_configs = [NoticeRawLog().from_dict(i) for i in m.get('noticeRawConfigs')]
        return self
