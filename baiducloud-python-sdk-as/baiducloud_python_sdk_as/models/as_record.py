"""
AsRecord information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_as.models.scale_condition import ScaleCondition

from baiducloud_python_sdk_as.models.expect_action import ExpectAction

from baiducloud_python_sdk_as.models.resource import Resource


class AsRecord(AbstractModel):
    """
    AsRecord
    """

    def __init__(
        self,
        group_id=None,
        record_id=None,
        start_time=None,
        result=None,
        actual_scale_node=None,
        actual_scale_bandwidth=None,
        current_bandwidth=None,
        remained_node=None,
        action=None,
        scale_condition=None,
        rule_id=None,
        message=None,
        expect_action=None,
        execute_type=None,
        dag_id=None,
        resource=None,
    ):
        """
        Initialize AsRecord instance.

        :param group_id: 伸缩组ID
        :type group_id: str (optional)

        :param record_id: 记录ID
        :type record_id: str (optional)

        :param start_time: 开始时间
        :type start_time: str (optional)

        :param result: 执行结果
        :type result: str (optional)

        :param actual_scale_node: 实际操作的节点列表
        :type actual_scale_node: List[str] (optional)

        :param actual_scale_bandwidth: 实际扩容后的带宽值
        :type actual_scale_bandwidth: int (optional)

        :param current_bandwidth: 当前带宽值
        :type current_bandwidth: int (optional)

        :param remained_node: 剩余的节点列表
        :type remained_node: List[str] (optional)

        :param action: 动作
        :type action: str (optional)

        :param scale_condition: scale_condition attribute
        :type scale_condition: ScaleCondition (optional)

        :param rule_id: 规则 ID
        :type rule_id: str (optional)

        :param message: 消息
        :type message: str (optional)

        :param expect_action: expect_action attribute
        :type expect_action: ExpectAction (optional)

        :param execute_type: 执行类型
        :type execute_type: str (optional)

        :param dag_id: DAG编号
        :type dag_id: str (optional)

        :param resource: resource attribute
        :type resource: Resource (optional)
        """
        super().__init__()
        self.group_id = group_id
        self.record_id = record_id
        self.start_time = start_time
        self.result = result
        self.actual_scale_node = actual_scale_node
        self.actual_scale_bandwidth = actual_scale_bandwidth
        self.current_bandwidth = current_bandwidth
        self.remained_node = remained_node
        self.action = action
        self.scale_condition = scale_condition
        self.rule_id = rule_id
        self.message = message
        self.expect_action = expect_action
        self.execute_type = execute_type
        self.dag_id = dag_id
        self.resource = resource

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
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.record_id is not None:
            result['recordId'] = self.record_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.result is not None:
            result['result'] = self.result
        if self.actual_scale_node is not None:
            result['actualScaleNode'] = self.actual_scale_node
        if self.actual_scale_bandwidth is not None:
            result['actualScaleBandwidth'] = self.actual_scale_bandwidth
        if self.current_bandwidth is not None:
            result['currentBandwidth'] = self.current_bandwidth
        if self.remained_node is not None:
            result['remainedNode'] = self.remained_node
        if self.action is not None:
            result['action'] = self.action
        if self.scale_condition is not None:
            result['scaleCondition'] = self.scale_condition.to_dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.message is not None:
            result['message'] = self.message
        if self.expect_action is not None:
            result['expectAction'] = self.expect_action.to_dict()
        if self.execute_type is not None:
            result['executeType'] = self.execute_type
        if self.dag_id is not None:
            result['dagId'] = self.dag_id
        if self.resource is not None:
            result['resource'] = self.resource.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AsRecord

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('actualScaleNode') is not None:
            self.actual_scale_node = m.get('actualScaleNode')
        if m.get('actualScaleBandwidth') is not None:
            self.actual_scale_bandwidth = m.get('actualScaleBandwidth')
        if m.get('currentBandwidth') is not None:
            self.current_bandwidth = m.get('currentBandwidth')
        if m.get('remainedNode') is not None:
            self.remained_node = m.get('remainedNode')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('scaleCondition') is not None:
            self.scale_condition = ScaleCondition().from_dict(m.get('scaleCondition'))
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('expectAction') is not None:
            self.expect_action = ExpectAction().from_dict(m.get('expectAction'))
        if m.get('executeType') is not None:
            self.execute_type = m.get('executeType')
        if m.get('dagId') is not None:
            self.dag_id = m.get('dagId')
        if m.get('resource') is not None:
            self.resource = Resource().from_dict(m.get('resource'))
        return self
