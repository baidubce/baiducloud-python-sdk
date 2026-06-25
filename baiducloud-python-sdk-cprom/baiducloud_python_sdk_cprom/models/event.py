"""
Event information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_cprom.models.claimed_info import ClaimedInfo


class Event(AbstractModel):
    """
    Event
    """

    def __init__(
        self,
        event_id=None,
        monitor_instance_id=None,
        alerting_rule_id=None,
        alerting_rule_name=None,
        notify_rule_id=None,
        notify_rule_name=None,
        severity=None,
        status=None,
        start_time=None,
        end_time=None,
        duration=None,
        alarm_value=None,
        expr=None,
        description=None,
        alarm_tags=None,
        labels=None,
        annotations=None,
        claimed_info=None,
    ):
        """
        Initialize Event instance.

        :param event_id: 事件 ID
        :type event_id: str (optional)

        :param monitor_instance_id: 监控实例 ID
        :type monitor_instance_id: str (optional)

        :param alerting_rule_id: 告警规则 ID
        :type alerting_rule_id: str (optional)

        :param alerting_rule_name: 告警规则名称
        :type alerting_rule_name: str (optional)

        :param notify_rule_id: 通知规则 ID
        :type notify_rule_id: str (optional)

        :param notify_rule_name: 通知规则名称
        :type notify_rule_name: str (optional)

        :param severity: 告警等级：critical/warning/info
        :type severity: str (optional)

        :param status: 事件状态：abnormal/normal/level1-4
        :type status: str (optional)

        :param start_time: 事件开始时间（Unix 时间戳，秒）
        :type start_time: int (optional)

        :param end_time: 事件结束时间（Unix 时间戳，秒），0 表示未结束
        :type end_time: int (optional)

        :param duration: 事件持续时间（秒）
        :type duration: int (optional)

        :param alarm_value: 告警值
        :type alarm_value: str (optional)

        :param expr: 告警表达式
        :type expr: str (optional)

        :param description: 告警描述
        :type description: str (optional)

        :param alarm_tags: 告警标签
        :type alarm_tags: object (optional)

        :param labels: 告警规则标签
        :type labels: object (optional)

        :param annotations: 告警规则注解
        :type annotations: object (optional)

        :param claimed_info: claimed_info attribute
        :type claimed_info: ClaimedInfo (optional)
        """
        super().__init__()
        self.event_id = event_id
        self.monitor_instance_id = monitor_instance_id
        self.alerting_rule_id = alerting_rule_id
        self.alerting_rule_name = alerting_rule_name
        self.notify_rule_id = notify_rule_id
        self.notify_rule_name = notify_rule_name
        self.severity = severity
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.alarm_value = alarm_value
        self.expr = expr
        self.description = description
        self.alarm_tags = alarm_tags
        self.labels = labels
        self.annotations = annotations
        self.claimed_info = claimed_info

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
        if self.event_id is not None:
            result['eventId'] = self.event_id
        if self.monitor_instance_id is not None:
            result['monitorInstanceId'] = self.monitor_instance_id
        if self.alerting_rule_id is not None:
            result['alertingRuleId'] = self.alerting_rule_id
        if self.alerting_rule_name is not None:
            result['alertingRuleName'] = self.alerting_rule_name
        if self.notify_rule_id is not None:
            result['notifyRuleId'] = self.notify_rule_id
        if self.notify_rule_name is not None:
            result['notifyRuleName'] = self.notify_rule_name
        if self.severity is not None:
            result['severity'] = self.severity
        if self.status is not None:
            result['status'] = self.status
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.duration is not None:
            result['duration'] = self.duration
        if self.alarm_value is not None:
            result['alarmValue'] = self.alarm_value
        if self.expr is not None:
            result['expr'] = self.expr
        if self.description is not None:
            result['description'] = self.description
        if self.alarm_tags is not None:
            result['alarmTags'] = self.alarm_tags
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.claimed_info is not None:
            result['claimedInfo'] = self.claimed_info.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Event

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')
        if m.get('monitorInstanceId') is not None:
            self.monitor_instance_id = m.get('monitorInstanceId')
        if m.get('alertingRuleId') is not None:
            self.alerting_rule_id = m.get('alertingRuleId')
        if m.get('alertingRuleName') is not None:
            self.alerting_rule_name = m.get('alertingRuleName')
        if m.get('notifyRuleId') is not None:
            self.notify_rule_id = m.get('notifyRuleId')
        if m.get('notifyRuleName') is not None:
            self.notify_rule_name = m.get('notifyRuleName')
        if m.get('severity') is not None:
            self.severity = m.get('severity')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('alarmValue') is not None:
            self.alarm_value = m.get('alarmValue')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('alarmTags') is not None:
            self.alarm_tags = m.get('alarmTags')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('claimedInfo') is not None:
            self.claimed_info = ClaimedInfo().from_dict(m.get('claimedInfo'))
        return self
