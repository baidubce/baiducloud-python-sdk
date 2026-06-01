"""
Request entity for ApmDescribeAlarmPolicyResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_apm.models.alarm_target import AlarmTarget
from baiducloud_python_sdk_apm.models.alarm_rule import AlarmRule
from baiducloud_python_sdk_apm.models.alarm_filter import AlarmFilter
from baiducloud_python_sdk_apm.models.alarm_action import AlarmAction


class ApmDescribeAlarmPolicyResponse(BceResponse):
    """
    ApmDescribeAlarmPolicyResponse
    """

    def __init__(
        self,
        success=None,
        code=None,
        message=None,
        id=None,
        name=None,
        created_timestamp=None,
        updated_timestamp=None,
        content=None,
        state=None,
        target=None,
        metric_kind=None,
        rule=None,
        rule_content=None,
        filters=None,
        pending_count=None,
        renotify_interval_in_minutes=None,
        renotify_count=None,
        notify_recovery=None,
        on_missing_data=None,
        no_data_notify_pending_interval_in_minutes=None,
        level=None,
        actions=None,
    ):
        """
        Initialize ApmDescribeAlarmPolicyResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 状态码
        :type code: str (optional)

        :param message: 错误信息
        :type message: str (optional)

        :param id: 策略ID
        :type id: str (optional)

        :param name: 策略名称
        :type name: str (optional)

        :param created_timestamp: 创建时间，UTC时间
        :type created_timestamp: str (optional)

        :param updated_timestamp: 更新时间，UTC时间
        :type updated_timestamp: str (optional)

        :param content: 策略内容
        :type content: str (optional)

        :param state: 策略状态，可选值：ENABLED-已启动，DISABLED-已停用
        :type state: str (optional)

        :param target: target field
        :type target: AlarmTarget (optional)

        :param metric_kind: 指标类别
        :type metric_kind: str (optional)

        :param rule: rule field
        :type rule: AlarmRule (optional)

        :param rule_content: 报警内容
        :type rule_content: str (optional)

        :param filters: 维度过滤条件列表
        :type filters: List[AlarmFilter] (optional)

        :param pending_count: 连续触发阈值，连续多少次触发阈值则报警
        :type pending_count: int (optional)

        :param renotify_interval_in_minutes: 重复报警间隔，单位：分钟
        :type renotify_interval_in_minutes: int (optional)

        :param renotify_count: 最大重复次数
        :type renotify_count: int (optional)

        :param notify_recovery: 恢复后是否通知
        :type notify_recovery: bool (optional)

        :param on_missing_data: 无数据处理方式
        :type on_missing_data: str (optional)

        :param no_data_notify_pending_interval_in_minutes: 无数据报警等待间隔，单位：分钟
        :type no_data_notify_pending_interval_in_minutes: int (optional)

        :param level: 报警级别
        :type level: str (optional)

        :param actions: 通知模板列表
        :type actions: List[AlarmAction] (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.message = message
        self.id = id
        self.name = name
        self.created_timestamp = created_timestamp
        self.updated_timestamp = updated_timestamp
        self.content = content
        self.state = state
        self.target = target
        self.metric_kind = metric_kind
        self.rule = rule
        self.rule_content = rule_content
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
        if self.success is not None:
            result['success'] = self.success
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.created_timestamp is not None:
            result['createdTimestamp'] = self.created_timestamp
        if self.updated_timestamp is not None:
            result['updatedTimestamp'] = self.updated_timestamp
        if self.content is not None:
            result['content'] = self.content
        if self.state is not None:
            result['state'] = self.state
        if self.target is not None:
            result['target'] = self.target.to_dict()
        if self.metric_kind is not None:
            result['metricKind'] = self.metric_kind
        if self.rule is not None:
            result['rule'] = self.rule.to_dict()
        if self.rule_content is not None:
            result['ruleContent'] = self.rule_content
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
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ApmDescribeAlarmPolicyResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('createdTimestamp') is not None:
            self.created_timestamp = m.get('createdTimestamp')
        if m.get('updatedTimestamp') is not None:
            self.updated_timestamp = m.get('updatedTimestamp')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('target') is not None:
            self.target = AlarmTarget().from_dict(m.get('target'))
        if m.get('metricKind') is not None:
            self.metric_kind = m.get('metricKind')
        if m.get('rule') is not None:
            self.rule = AlarmRule().from_dict(m.get('rule'))
        if m.get('ruleContent') is not None:
            self.rule_content = m.get('ruleContent')
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
