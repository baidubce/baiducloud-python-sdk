"""
Alarm information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcm.models.alarm_resource import AlarmResource

from baiducloud_python_sdk_bcm.models.alarm_policy_summary import AlarmPolicySummary

from baiducloud_python_sdk_bcm.models.alarm_action import AlarmAction

from baiducloud_python_sdk_bcm.models.alert_metric import AlertMetric


class Alarm(AbstractModel):
    """
    Alarm
    """

    def __init__(
        self,
        id=None,
        series_id=None,
        state=None,
        init_state=None,
        close_reason=None,
        start_time=None,
        end_time=None,
        type=None,
        resource=None,
        policy=None,
        actions=None,
        alert_metrics=None,
    ):
        """
        Initialize Alarm instance.

        :param id: 报警记录ID
        :type id: str (optional)

        :param series_id: 报警序列ID
        :type series_id: str (optional)

        :param state: 报警状态
        :type state: str (optional)

        :param init_state: 初始状态
        :type init_state: str (optional)

        :param close_reason: 关闭原因
        :type close_reason: str (optional)

        :param start_time: 报警开始时间
        :type start_time: str (optional)

        :param end_time: 报警结束时间
        :type end_time: str (optional)

        :param type: 报警类型
        :type type: str (optional)

        :param resource: resource attribute
        :type resource: AlarmResource (optional)

        :param policy: policy attribute
        :type policy: AlarmPolicySummary (optional)

        :param actions: 报警动作列表
        :type actions: List[AlarmAction] (optional)

        :param alert_metrics: 报警指标详情列表
        :type alert_metrics: List[AlertMetric] (optional)
        """
        super().__init__()
        self.id = id
        self.series_id = series_id
        self.state = state
        self.init_state = init_state
        self.close_reason = close_reason
        self.start_time = start_time
        self.end_time = end_time
        self.type = type
        self.resource = resource
        self.policy = policy
        self.actions = actions
        self.alert_metrics = alert_metrics

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
        if self.id is not None:
            result['id'] = self.id
        if self.series_id is not None:
            result['seriesId'] = self.series_id
        if self.state is not None:
            result['state'] = self.state
        if self.init_state is not None:
            result['initState'] = self.init_state
        if self.close_reason is not None:
            result['closeReason'] = self.close_reason
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.type is not None:
            result['type'] = self.type
        if self.resource is not None:
            result['resource'] = self.resource.to_dict()
        if self.policy is not None:
            result['policy'] = self.policy.to_dict()
        if self.actions is not None:
            result['actions'] = [i.to_dict() for i in self.actions]
        if self.alert_metrics is not None:
            result['alertMetrics'] = [i.to_dict() for i in self.alert_metrics]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Alarm

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('seriesId') is not None:
            self.series_id = m.get('seriesId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('initState') is not None:
            self.init_state = m.get('initState')
        if m.get('closeReason') is not None:
            self.close_reason = m.get('closeReason')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('resource') is not None:
            self.resource = AlarmResource().from_dict(m.get('resource'))
        if m.get('policy') is not None:
            self.policy = AlarmPolicySummary().from_dict(m.get('policy'))
        if m.get('actions') is not None:
            self.actions = [AlarmAction().from_dict(i) for i in m.get('actions')]
        if m.get('alertMetrics') is not None:
            self.alert_metrics = [AlertMetric().from_dict(i) for i in m.get('alertMetrics')]
        return self
