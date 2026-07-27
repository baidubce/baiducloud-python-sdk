"""
Task information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_oos.models.execution import Execution

from baiducloud_python_sdk_oos.models.operator import Operator

from baiducloud_python_sdk_oos.models.execution import Execution


class Task(AbstractModel):
    """
    Task
    """

    def __init__(
        self,
        namespace=None,
        user_id=None,
        id=None,
        revision=None,
        loop_index=None,
        reason=None,
        error_code=None,
        execution=None,
        operator=None,
        created_timestamp=None,
        updated_timestamp=None,
        finished_timestamp=None,
        state=None,
        properties=None,
        tries=None,
        children=None,
        executions=None,
        output_context=None,
    ):
        """
        Initialize Task instance.

        :param namespace: 名称空间
        :type namespace: str (optional)

        :param user_id: 用户 ID
        :type user_id: str (optional)

        :param id: 任务 ID，全局唯一
        :type id: str (optional)

        :param revision: 版本号
        :type revision: int (optional)

        :param loop_index: 当前任务所对应的 loops 序号
        :type loop_index: int (optional)

        :param reason: 原因（失败/取消等）
        :type reason: str (optional)

        :param error_code: 错误码
        :type error_code: str (optional)

        :param execution: execution attribute
        :type execution: Execution (optional)

        :param operator: operator attribute
        :type operator: Operator (optional)

        :param created_timestamp: 任务开始时间，Unix 时间戳，单位：毫秒
        :type created_timestamp: int (optional)

        :param updated_timestamp: 任务更新时间，Unix 时间戳，单位：毫秒
        :type updated_timestamp: int (optional)

        :param finished_timestamp: 任务结束时间，Unix 时间戳，单位：毫秒，未结束填 0
        :type finished_timestamp: int (optional)

        :param state: state attribute
        :type state: str (optional)

        :param properties: 任务参数
        :type properties: Dict[str, object] (optional)

        :param tries: 任务尝试次数，从 0 开始
        :type tries: int (optional)

        :param children: 子任务列表
        :type children: List[Task] (optional)

        :param executions: 子执行实例列表（重试时会产生多个执行实例）
        :type executions: List[Execution] (optional)

        :param output_context: 任务输出结果
        :type output_context: object (optional)
        """
        super().__init__()
        self.namespace = namespace
        self.user_id = user_id
        self.id = id
        self.revision = revision
        self.loop_index = loop_index
        self.reason = reason
        self.error_code = error_code
        self.execution = execution
        self.operator = operator
        self.created_timestamp = created_timestamp
        self.updated_timestamp = updated_timestamp
        self.finished_timestamp = finished_timestamp
        self.state = state
        self.properties = properties
        self.tries = tries
        self.children = children
        self.executions = executions
        self.output_context = output_context

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
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.id is not None:
            result['id'] = self.id
        if self.revision is not None:
            result['revision'] = self.revision
        if self.loop_index is not None:
            result['loopIndex'] = self.loop_index
        if self.reason is not None:
            result['reason'] = self.reason
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.execution is not None:
            result['execution'] = self.execution.to_dict()
        if self.operator is not None:
            result['operator'] = self.operator.to_dict()
        if self.created_timestamp is not None:
            result['createdTimestamp'] = self.created_timestamp
        if self.updated_timestamp is not None:
            result['updatedTimestamp'] = self.updated_timestamp
        if self.finished_timestamp is not None:
            result['finishedTimestamp'] = self.finished_timestamp
        if self.state is not None:
            result['state'] = self.state
        if self.properties is not None:
            result['properties'] = self.properties
        if self.tries is not None:
            result['tries'] = self.tries
        if self.children is not None:
            result['children'] = [i.to_dict() for i in self.children]
        if self.executions is not None:
            result['executions'] = [i.to_dict() for i in self.executions]
        if self.output_context is not None:
            result['outputContext'] = self.output_context
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Task

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('revision') is not None:
            self.revision = m.get('revision')
        if m.get('loopIndex') is not None:
            self.loop_index = m.get('loopIndex')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('execution') is not None:
            self.execution = Execution().from_dict(m.get('execution'))
        if m.get('operator') is not None:
            self.operator = Operator().from_dict(m.get('operator'))
        if m.get('createdTimestamp') is not None:
            self.created_timestamp = m.get('createdTimestamp')
        if m.get('updatedTimestamp') is not None:
            self.updated_timestamp = m.get('updatedTimestamp')
        if m.get('finishedTimestamp') is not None:
            self.finished_timestamp = m.get('finishedTimestamp')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('tries') is not None:
            self.tries = m.get('tries')
        if m.get('children') is not None:
            self.children = [Task().from_dict(i) for i in m.get('children')]
        if m.get('executions') is not None:
            self.executions = [Execution().from_dict(i) for i in m.get('executions')]
        if m.get('outputContext') is not None:
            self.output_context = m.get('outputContext')
        return self
