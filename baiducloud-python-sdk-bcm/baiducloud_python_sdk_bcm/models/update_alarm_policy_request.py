"""
Request entity for UpdateAlarmPolicyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcm.models.alarm_target import AlarmTarget
from baiducloud_python_sdk_bcm.models.alarm_rule import AlarmRule
from baiducloud_python_sdk_bcm.models.policy_action import PolicyAction
from baiducloud_python_sdk_bcm.models.callback import Callback


class UpdateAlarmPolicyRequest(AbstractModel):
    """
    Request entity for UpdateAlarmPolicyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        id,
        state,
        name,
        scope,
        resource_type,
        target,
        rules,
        pending_count,
        on_missing_data,
        type,
        level,
        actions,
        notify_enabled,
        no_data_notify_pending_minutes=None,
        callbacks=None,
        renotify_count=None,
        renotify_interval_minutes=None,
        notify_merge_window_seconds=None,
    ):
        """
        Initialize UpdateAlarmPolicyRequest request entity.

        :param id: 策略ID
        :type id: str (required)

        :param state: 策略状态，可选值：ENABLED / DISABLED
        :type state: str (required)

        :param name: 策略名称
        :type name: str (required)

        :param scope: 云产品类型
        :type scope: str (required)

        :param resource_type: 资源类型
        :type resource_type: str (required)

        :param target: target parameter
        :type target: AlarmTarget (required)

        :param rules: 报警规则列表（OR规则）
        :type rules: List[AlarmRule] (required)

        :param pending_count: 连续触发阈值，取值范围：大于0
        :type pending_count: int (required)

        :param on_missing_data: 无数据处理方式，可选值：IGNORE / SHOW_NO_DATA_AND_NOTIFY / SHOW_OK
        :type on_missing_data: str (required)

        :param no_data_notify_pending_minutes: 无数据判定间隔，单位：分钟，onMissingData非IGNORE时必填
        :type no_data_notify_pending_minutes: int (optional)

        :param type: 策略类型，可选值：APP / SITE / CLOUD / CUSTOM
        :type type: str (required)

        :param level: 报警级别，可选值：NOTICE / WARNING / MAJOR / CRITICAL
        :type level: str (required)

        :param actions: 通知配置列表
        :type actions: List[PolicyAction] (required)

        :param notify_enabled: 是否启用通知
        :type notify_enabled: bool (required)

        :param callbacks: 回调地址列表
        :type callbacks: List[Callback] (optional)

        :param renotify_count: 最大重复报警次数，0表示关闭
        :type renotify_count: int (optional)

        :param renotify_interval_minutes: 重复通知间隔，单位：分钟，renotifyCount>0时必填
        :type renotify_interval_minutes: int (optional)

        :param notify_merge_window_seconds: 通知合并窗口，单位：秒，0表示关闭
        :type notify_merge_window_seconds: int (optional)
        """
        super().__init__()
        self.id = id
        self.state = state
        self.name = name
        self.scope = scope
        self.resource_type = resource_type
        self.target = target
        self.rules = rules
        self.pending_count = pending_count
        self.on_missing_data = on_missing_data
        self.no_data_notify_pending_minutes = no_data_notify_pending_minutes
        self.type = type
        self.level = level
        self.actions = actions
        self.notify_enabled = notify_enabled
        self.callbacks = callbacks
        self.renotify_count = renotify_count
        self.renotify_interval_minutes = renotify_interval_minutes
        self.notify_merge_window_seconds = notify_merge_window_seconds

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
        if self.state is not None:
            result['state'] = self.state
        if self.name is not None:
            result['name'] = self.name
        if self.scope is not None:
            result['scope'] = self.scope
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.target is not None:
            result['target'] = self.target.to_dict()
        if self.rules is not None:
            result['rules'] = [i.to_dict() for i in self.rules]
        if self.pending_count is not None:
            result['pendingCount'] = self.pending_count
        if self.on_missing_data is not None:
            result['onMissingData'] = self.on_missing_data
        if self.no_data_notify_pending_minutes is not None:
            result['noDataNotifyPendingMinutes'] = self.no_data_notify_pending_minutes
        if self.type is not None:
            result['type'] = self.type
        if self.level is not None:
            result['level'] = self.level
        if self.actions is not None:
            result['actions'] = [i.to_dict() for i in self.actions]
        if self.notify_enabled is not None:
            result['notifyEnabled'] = self.notify_enabled
        if self.callbacks is not None:
            result['callbacks'] = [i.to_dict() for i in self.callbacks]
        if self.renotify_count is not None:
            result['renotifyCount'] = self.renotify_count
        if self.renotify_interval_minutes is not None:
            result['renotifyIntervalMinutes'] = self.renotify_interval_minutes
        if self.notify_merge_window_seconds is not None:
            result['notifyMergeWindowSeconds'] = self.notify_merge_window_seconds
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
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('target') is not None:
            self.target = AlarmTarget().from_dict(m.get('target'))
        if m.get('rules') is not None:
            self.rules = [AlarmRule().from_dict(i) for i in m.get('rules')]
        if m.get('pendingCount') is not None:
            self.pending_count = m.get('pendingCount')
        if m.get('onMissingData') is not None:
            self.on_missing_data = m.get('onMissingData')
        if m.get('noDataNotifyPendingMinutes') is not None:
            self.no_data_notify_pending_minutes = m.get('noDataNotifyPendingMinutes')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('actions') is not None:
            self.actions = [PolicyAction().from_dict(i) for i in m.get('actions')]
        if m.get('notifyEnabled') is not None:
            self.notify_enabled = m.get('notifyEnabled')
        if m.get('callbacks') is not None:
            self.callbacks = [Callback().from_dict(i) for i in m.get('callbacks')]
        if m.get('renotifyCount') is not None:
            self.renotify_count = m.get('renotifyCount')
        if m.get('renotifyIntervalMinutes') is not None:
            self.renotify_interval_minutes = m.get('renotifyIntervalMinutes')
        if m.get('notifyMergeWindowSeconds') is not None:
            self.notify_merge_window_seconds = m.get('notifyMergeWindowSeconds')
        return self
