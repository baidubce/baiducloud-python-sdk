"""
Request entity for ApmUpdateAlarmPolicyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_apm.models.alarm_target import AlarmTarget
from baiducloud_python_sdk_apm.models.alarm_rule import AlarmRule
from baiducloud_python_sdk_apm.models.alarm_filter import AlarmFilter
from baiducloud_python_sdk_apm.models.alarm_action import AlarmAction


class ApmUpdateAlarmPolicyRequest(AbstractModel):
    """
    Request entity for ApmUpdateAlarmPolicyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        id,
        name,
        target,
        metric_kind,
        rule,
        pending_count,
        renotify_interval_in_minutes,
        renotify_count,
        notify_recovery,
        on_missing_data,
        no_data_notify_pending_interval_in_minutes,
        actions,
        filters=None,
        level=None,
    ):
        """
        Initialize ApmUpdateAlarmPolicyRequest request entity.

        :param id: 策略ID
        :type id: str (required)

        :param name: 报警策略名称
        :type name: str (required)

        :param target: target parameter
        :type target: AlarmTarget (required)

        :param metric_kind: metric_kind parameter
        :type metric_kind: str (required)

        :param rule: rule parameter
        :type rule: AlarmRule (required)

        :param filters: 维度过滤条件列表
        :type filters: List[AlarmFilter] (optional)

        :param pending_count: 连续触发阈值，连续多少次触发阈值则报警
        :type pending_count: int (required)

        :param renotify_interval_in_minutes: 重复报警间隔，单位：分钟，设置为0表示关闭重复报警
        :type renotify_interval_in_minutes: int (required)

        :param renotify_count: 最大重复次数，设置为0表示关闭重复报警
        :type renotify_count: int (required)

        :param notify_recovery: 恢复后是否通知
        :type notify_recovery: bool (required)

        :param on_missing_data: on_missing_data parameter
        :type on_missing_data: str (required)

        :param no_data_notify_pending_interval_in_minutes: no_data_notify_pending_interval_in_minutes parameter
        :type no_data_notify_pending_interval_in_minutes: int (required)

        :param level: level parameter
        :type level: str (optional)

        :param actions: 通知模板列表，统一用于异常通知、恢复通知、重复报警通知
        :type actions: List[AlarmAction] (required)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.target = target
        self.metric_kind = metric_kind
        self.rule = rule
        self.filters = filters
        self.pending_count = pending_count
        self.renotify_interval_in_minutes = renotify_interval_in_minutes
        self.renotify_count = renotify_count
        self.notify_recovery = notify_recovery
        self.on_missing_data = on_missing_data
        self.no_data_notify_pending_interval_in_minutes = no_data_notify_pending_interval_in_minutes
        self.level = level
        self.actions = actions

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
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.target is not None:
            result['target'] = self.target.to_dict()
        if self.metric_kind is not None:
            result['metricKind'] = self.metric_kind
        if self.rule is not None:
            result['rule'] = self.rule.to_dict()
        if self.filters is not None:
            result['filters'] = [i.to_dict() for i in self.filters]
        if self.pending_count is not None:
            result['pendingCount'] = self.pending_count
        if self.renotify_interval_in_minutes is not None:
            result['renotifyIntervalInMinutes'] = self.renotify_interval_in_minutes
        if self.renotify_count is not None:
            result['renotifyCount'] = self.renotify_count
        if self.notify_recovery is not None:
            result['notifyRecovery'] = self.notify_recovery
        if self.on_missing_data is not None:
            result['onMissingData'] = self.on_missing_data
        if self.no_data_notify_pending_interval_in_minutes is not None:
            result['noDataNotifyPendingIntervalInMinutes'] = self.no_data_notify_pending_interval_in_minutes
        if self.level is not None:
            result['level'] = self.level
        if self.actions is not None:
            result['actions'] = [i.to_dict() for i in self.actions]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ApmUpdateAlarmPolicyRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('target') is not None:
            self.target = AlarmTarget().from_dict(m.get('target'))
        if m.get('metricKind') is not None:
            self.metric_kind = m.get('metricKind')
        if m.get('rule') is not None:
            self.rule = AlarmRule().from_dict(m.get('rule'))
        if m.get('filters') is not None:
            self.filters = [AlarmFilter().from_dict(i) for i in m.get('filters')]
        if m.get('pendingCount') is not None:
            self.pending_count = m.get('pendingCount')
        if m.get('renotifyIntervalInMinutes') is not None:
            self.renotify_interval_in_minutes = m.get('renotifyIntervalInMinutes')
        if m.get('renotifyCount') is not None:
            self.renotify_count = m.get('renotifyCount')
        if m.get('notifyRecovery') is not None:
            self.notify_recovery = m.get('notifyRecovery')
        if m.get('onMissingData') is not None:
            self.on_missing_data = m.get('onMissingData')
        if m.get('noDataNotifyPendingIntervalInMinutes') is not None:
            self.no_data_notify_pending_interval_in_minutes = m.get('noDataNotifyPendingIntervalInMinutes')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('actions') is not None:
            self.actions = [AlarmAction().from_dict(i) for i in m.get('actions')]
        return self
