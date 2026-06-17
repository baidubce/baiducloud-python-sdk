"""
Alarm information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bls.models.policy import Policy

from baiducloud_python_sdk_bls.models.log_store import LogStore

from baiducloud_python_sdk_bls.models.trigger_condition import TriggerCondition

from baiducloud_python_sdk_bls.models.execution import Execution


class Alarm(AbstractModel):
    """
    Alarm
    """

    def __init__(
        self,
        id=None,
        group_id=None,
        start_time=None,
        end_time=None,
        state=None,
        close_reason=None,
        policy=None,
        object=None,
        trigger_condition=None,
        groups=None,
        executions=None,
    ):
        """
        Initialize Alarm instance.

        :param id: 报警ID
        :type id: str (optional)

        :param group_id: 分组ID
        :type group_id: str (optional)

        :param start_time: 报警开始时间，UTC时间
        :type start_time: str (optional)

        :param end_time: 报警关闭时间，UTC时间，若报警未关闭，该值为空字符串
        :type end_time: str (optional)

        :param state: 报警状态，取值：OK: 已恢复, ALERT: 报警中, CLOSED: 已关闭
        :type state: str (optional)

        :param close_reason: 报警关闭原因， POLICY_MODIFIED: 报警策略更新
        :type close_reason: str (optional)

        :param policy: policy attribute
        :type policy: Policy (optional)

        :param object: object attribute
        :type object: LogStore (optional)

        :param trigger_condition: trigger_condition attribute
        :type trigger_condition: TriggerCondition (optional)

        :param groups: 分组结果
        :type groups: Dict[str, str] (optional)

        :param executions: 执行列表
        :type executions: List[Execution] (optional)
        """
        super().__init__()
        self.id = id
        self.group_id = group_id
        self.start_time = start_time
        self.end_time = end_time
        self.state = state
        self.close_reason = close_reason
        self.policy = policy
        self.object = object
        self.trigger_condition = trigger_condition
        self.groups = groups
        self.executions = executions

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
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.state is not None:
            result['state'] = self.state
        if self.close_reason is not None:
            result['closeReason'] = self.close_reason
        if self.policy is not None:
            result['policy'] = self.policy.to_dict()
        if self.object is not None:
            result['object'] = self.object.to_dict()
        if self.trigger_condition is not None:
            result['triggerCondition'] = self.trigger_condition.to_dict()
        if self.groups is not None:
            result['groups'] = self.groups
        if self.executions is not None:
            result['executions'] = [i.to_dict() for i in self.executions]
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
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('closeReason') is not None:
            self.close_reason = m.get('closeReason')
        if m.get('policy') is not None:
            self.policy = Policy().from_dict(m.get('policy'))
        if m.get('object') is not None:
            self.object = LogStore().from_dict(m.get('object'))
        if m.get('triggerCondition') is not None:
            self.trigger_condition = TriggerCondition().from_dict(m.get('triggerCondition'))
        if m.get('groups') is not None:
            self.groups = m.get('groups')
        if m.get('executions') is not None:
            self.executions = [Execution().from_dict(i) for i in m.get('executions')]
        return self
