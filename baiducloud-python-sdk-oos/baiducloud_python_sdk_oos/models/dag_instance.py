"""
DagInstance information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_oos.models.dag_spec import DagSpec

from baiducloud_python_sdk_oos.models.tag_selector import TagSelector

from baiducloud_python_sdk_oos.models.execution_task_summary import ExecutionTaskSummary

from baiducloud_python_sdk_oos.models.dag_action_model import DagActionModel

from baiducloud_python_sdk_oos.models.event_model import EventModel

from baiducloud_python_sdk_oos.models.execution_task_summary import ExecutionTaskSummary


class DagInstance(AbstractModel):
    """
    DagInstance
    """

    def __init__(
        self,
        id=None,
        description=None,
        revision=None,
        created_timestamp=None,
        updated_timestamp=None,
        finished_timestamp=None,
        namespace=None,
        state=None,
        dag_spec=None,
        init_context=None,
        parallelism=None,
        manually=None,
        worker_selectors=None,
        tasks=None,
        user=None,
        operator_actions=None,
        dag_actions=None,
        event=None,
        parent_task=None,
        trigger=None,
        init_operators=None,
        reason=None,
        error_code=None,
        cron_dag_name=None,
        event_dag_name=None,
    ):
        """
        Initialize DagInstance instance.

        :param id: DAG（执行）ID，全局唯一
        :type id: str (optional)

        :param description: 执行描述
        :type description: str (optional)

        :param revision: 版本号，更新 DAG 时需要携带
        :type revision: int (optional)

        :param created_timestamp: 执行创建时间，Unix 时间戳，单位：毫秒
        :type created_timestamp: int (optional)

        :param updated_timestamp: 执行最近更新时间，Unix 时间戳，单位：毫秒
        :type updated_timestamp: int (optional)

        :param finished_timestamp: 执行结束时间，Unix 时间戳，单位：毫秒；未结束时填 0
        :type finished_timestamp: int (optional)

        :param namespace: 名称空间，DAG 仅在所属 namespace 下执行
        :type namespace: str (optional)

        :param state: state attribute
        :type state: str (optional)

        :param dag_spec: dag_spec attribute
        :type dag_spec: DagSpec (optional)

        :param init_context: 全局参数取值集合（Map<String,Object>）
        :type init_context: object (optional)

        :param parallelism: 并发度
        :type parallelism: int (optional)

        :param manually: 是否手动触发，默认 false
        :type manually: bool (optional)

        :param worker_selectors: 工作机选择器列表（List<TagSelector>）
        :type worker_selectors: List[TagSelector] (optional)

        :param tasks: 执行中的任务列表（List<TaskModel>）
        :type tasks: List[ExecutionTaskSummary] (optional)

        :param user: 执行所属用户信息
        :type user: object (optional)

        :param operator_actions: operator_actions attribute
        :type operator_actions: object (optional)

        :param dag_actions: dag_actions attribute
        :type dag_actions: DagActionModel (optional)

        :param event: event attribute
        :type event: EventModel (optional)

        :param parent_task: parent_task attribute
        :type parent_task: ExecutionTaskSummary (optional)

        :param trigger: 触发方式（如 manual / cron / event 等）
        :type trigger: str (optional)

        :param init_operators: 初始 operator 列表（List<OperatorModel>），DAG 创建时记录的初始 operator 快照
        :type init_operators: List[TaskOperatorSummary] (optional)

        :param reason: 状态原因（失败/取消等场景下的原因说明）
        :type reason: str (optional)

        :param error_code: 错误码
        :type error_code: str (optional)

        :param cron_dag_name: 定时运维名称（cron 触发时填充）
        :type cron_dag_name: str (optional)

        :param event_dag_name: 报警事件运维名称（event 触发时填充）
        :type event_dag_name: str (optional)
        """
        super().__init__()
        self.id = id
        self.description = description
        self.revision = revision
        self.created_timestamp = created_timestamp
        self.updated_timestamp = updated_timestamp
        self.finished_timestamp = finished_timestamp
        self.namespace = namespace
        self.state = state
        self.dag_spec = dag_spec
        self.init_context = init_context
        self.parallelism = parallelism
        self.manually = manually
        self.worker_selectors = worker_selectors
        self.tasks = tasks
        self.user = user
        self.operator_actions = operator_actions
        self.dag_actions = dag_actions
        self.event = event
        self.parent_task = parent_task
        self.trigger = trigger
        self.init_operators = init_operators
        self.reason = reason
        self.error_code = error_code
        self.cron_dag_name = cron_dag_name
        self.event_dag_name = event_dag_name

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
        if self.description is not None:
            result['description'] = self.description
        if self.revision is not None:
            result['revision'] = self.revision
        if self.created_timestamp is not None:
            result['createdTimestamp'] = self.created_timestamp
        if self.updated_timestamp is not None:
            result['updatedTimestamp'] = self.updated_timestamp
        if self.finished_timestamp is not None:
            result['finishedTimestamp'] = self.finished_timestamp
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.state is not None:
            result['state'] = self.state
        if self.dag_spec is not None:
            result['dagSpec'] = self.dag_spec.to_dict()
        if self.init_context is not None:
            result['initContext'] = self.init_context
        if self.parallelism is not None:
            result['parallelism'] = self.parallelism
        if self.manually is not None:
            result['manually'] = self.manually
        if self.worker_selectors is not None:
            result['workerSelectors'] = [i.to_dict() for i in self.worker_selectors]
        if self.tasks is not None:
            result['tasks'] = [i.to_dict() for i in self.tasks]
        if self.user is not None:
            result['user'] = self.user
        if self.operator_actions is not None:
            result['operatorActions'] = self.operator_actions
        if self.dag_actions is not None:
            result['dagActions'] = self.dag_actions.to_dict()
        if self.event is not None:
            result['event'] = self.event.to_dict()
        if self.parent_task is not None:
            result['parentTask'] = self.parent_task.to_dict()
        if self.trigger is not None:
            result['trigger'] = self.trigger
        if self.init_operators is not None:
            result['initOperators'] = [i.to_dict() for i in self.init_operators]
        if self.reason is not None:
            result['reason'] = self.reason
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.cron_dag_name is not None:
            result['cronDagName'] = self.cron_dag_name
        if self.event_dag_name is not None:
            result['eventDagName'] = self.event_dag_name
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DagInstance

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('revision') is not None:
            self.revision = m.get('revision')
        if m.get('createdTimestamp') is not None:
            self.created_timestamp = m.get('createdTimestamp')
        if m.get('updatedTimestamp') is not None:
            self.updated_timestamp = m.get('updatedTimestamp')
        if m.get('finishedTimestamp') is not None:
            self.finished_timestamp = m.get('finishedTimestamp')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('dagSpec') is not None:
            self.dag_spec = DagSpec().from_dict(m.get('dagSpec'))
        if m.get('initContext') is not None:
            self.init_context = m.get('initContext')
        if m.get('parallelism') is not None:
            self.parallelism = m.get('parallelism')
        if m.get('manually') is not None:
            self.manually = m.get('manually')
        if m.get('workerSelectors') is not None:
            self.worker_selectors = [TagSelector().from_dict(i) for i in m.get('workerSelectors')]
        if m.get('tasks') is not None:
            self.tasks = [ExecutionTaskSummary().from_dict(i) for i in m.get('tasks')]
        if m.get('user') is not None:
            self.user = m.get('user')
        if m.get('operatorActions') is not None:
            self.operator_actions = m.get('operatorActions')
        if m.get('dagActions') is not None:
            self.dag_actions = DagActionModel().from_dict(m.get('dagActions'))
        if m.get('event') is not None:
            self.event = EventModel().from_dict(m.get('event'))
        if m.get('parentTask') is not None:
            self.parent_task = ExecutionTaskSummary().from_dict(m.get('parentTask'))
        if m.get('trigger') is not None:
            self.trigger = m.get('trigger')
        if m.get('initOperators') is not None:
            self.init_operators = [TaskOperatorSummary().from_dict(i) for i in m.get('initOperators')]
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('cronDagName') is not None:
            self.cron_dag_name = m.get('cronDagName')
        if m.get('eventDagName') is not None:
            self.event_dag_name = m.get('eventDagName')
        return self
