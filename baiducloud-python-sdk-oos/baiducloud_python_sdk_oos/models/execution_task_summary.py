"""
ExecutionTaskSummary information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_oos.models.dag_instance import DagInstance

from baiducloud_python_sdk_oos.models.task_operator_summary import TaskOperatorSummary

from baiducloud_python_sdk_oos.models.log import Log


class ExecutionTaskSummary(AbstractModel):
    """
    ExecutionTaskSummary
    """

    def __init__(
        self,
        id=None,
        loop_index=None,
        namespace=None,
        dag=None,
        revision=None,
        created_timestamp=None,
        updated_timestamp=None,
        finished_timestamp=None,
        state=None,
        operator=None,
        reason=None,
        error_code=None,
        init_context=None,
        context=None,
        output_context=None,
        tries=None,
        children=None,
        log=None,
    ):
        """
        Initialize ExecutionTaskSummary instance.

        :param id: 任务 ID
        :type id: str (optional)

        :param loop_index: loops 序号
        :type loop_index: int (optional)

        :param namespace: 名称空间
        :type namespace: str (optional)

        :param dag: dag attribute
        :type dag: DagInstance (optional)

        :param revision: 版本号
        :type revision: int (optional)

        :param created_timestamp: 任务开始时间，Unix 时间戳，单位：毫秒
        :type created_timestamp: int (optional)

        :param updated_timestamp: 任务更新时间，Unix 时间戳，单位：毫秒
        :type updated_timestamp: int (optional)

        :param finished_timestamp: 任务结束时间，Unix 时间戳，单位：毫秒，未结束填 0
        :type finished_timestamp: int (optional)

        :param state: 任务状态
        :type state: str (optional)

        :param operator: operator attribute
        :type operator: TaskOperatorSummary (optional)

        :param reason: 原因
        :type reason: str (optional)

        :param error_code: 错误码
        :type error_code: str (optional)

        :param init_context: 任务初始参数
        :type init_context: object (optional)

        :param context: 任务上下文，包含全局参数和输出结果
        :type context: object (optional)

        :param output_context: 任务输出结果
        :type output_context: object (optional)

        :param tries: 任务尝试次数，从 0 开始
        :type tries: int (optional)

        :param children: 子任务列表
        :type children: List[ExecutionTaskSummary] (optional)

        :param log: 任务日志列表
        :type log: List[Log] (optional)
        """
        super().__init__()
        self.id = id
        self.loop_index = loop_index
        self.namespace = namespace
        self.dag = dag
        self.revision = revision
        self.created_timestamp = created_timestamp
        self.updated_timestamp = updated_timestamp
        self.finished_timestamp = finished_timestamp
        self.state = state
        self.operator = operator
        self.reason = reason
        self.error_code = error_code
        self.init_context = init_context
        self.context = context
        self.output_context = output_context
        self.tries = tries
        self.children = children
        self.log = log

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
        if self.loop_index is not None:
            result['loopIndex'] = self.loop_index
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.dag is not None:
            result['dag'] = self.dag.to_dict()
        if self.revision is not None:
            result['revision'] = self.revision
        if self.created_timestamp is not None:
            result['createdTimestamp'] = self.created_timestamp
        if self.updated_timestamp is not None:
            result['updatedTimestamp'] = self.updated_timestamp
        if self.finished_timestamp is not None:
            result['finishedTimestamp'] = self.finished_timestamp
        if self.state is not None:
            result['state'] = self.state
        if self.operator is not None:
            result['operator'] = self.operator.to_dict()
        if self.reason is not None:
            result['reason'] = self.reason
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.init_context is not None:
            result['initContext'] = self.init_context
        if self.context is not None:
            result['context'] = self.context
        if self.output_context is not None:
            result['outputContext'] = self.output_context
        if self.tries is not None:
            result['tries'] = self.tries
        if self.children is not None:
            result['children'] = [i.to_dict() for i in self.children]
        if self.log is not None:
            result['log'] = [i.to_dict() for i in self.log]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ExecutionTaskSummary

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('loopIndex') is not None:
            self.loop_index = m.get('loopIndex')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('dag') is not None:
            self.dag = DagInstance().from_dict(m.get('dag'))
        if m.get('revision') is not None:
            self.revision = m.get('revision')
        if m.get('createdTimestamp') is not None:
            self.created_timestamp = m.get('createdTimestamp')
        if m.get('updatedTimestamp') is not None:
            self.updated_timestamp = m.get('updatedTimestamp')
        if m.get('finishedTimestamp') is not None:
            self.finished_timestamp = m.get('finishedTimestamp')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('operator') is not None:
            self.operator = TaskOperatorSummary().from_dict(m.get('operator'))
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('initContext') is not None:
            self.init_context = m.get('initContext')
        if m.get('context') is not None:
            self.context = m.get('context')
        if m.get('outputContext') is not None:
            self.output_context = m.get('outputContext')
        if m.get('tries') is not None:
            self.tries = m.get('tries')
        if m.get('children') is not None:
            self.children = [ExecutionTaskSummary().from_dict(i) for i in m.get('children')]
        if m.get('log') is not None:
            self.log = [Log().from_dict(i) for i in m.get('log')]
        return self
