"""
TaskOperatorSummary information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_oos.models.tag_selector import TagSelector

from baiducloud_python_sdk_oos.models.event_model import EventModel


class TaskOperatorSummary(AbstractModel):
    """
    TaskOperatorSummary
    """

    def __init__(
        self,
        name=None,
        description=None,
        tags=None,
        operator=None,
        dag_spec=None,
        inline=None,
        retries=None,
        retry_interval=None,
        timeout=None,
        init_context=None,
        loops=None,
        parallelism_ratio=None,
        parallelism_count=None,
        allowed_failure_ratio=None,
        allowed_failure_count=None,
        manually=None,
        pause_on_failure=None,
        schedule_delay_milli=None,
        wait_on_agent_milli=None,
        condition=None,
        breakpoints=None,
        trigger_rule=None,
        loop_window_type=None,
        worker_selectors=None,
        collect_children_context=None,
        rollback_operator=None,
        events=None,
        init_operators=None,
        by_bsm_agent=None,
    ):
        """
        Initialize TaskOperatorSummary instance.

        :param name: operator 名称
        :type name: str (optional)

        :param description: operator 描述
        :type description: str (optional)

        :param tags: 标签键值对
        :type tags: object (optional)

        :param operator: operator 类型标识
        :type operator: str (optional)

        :param dag_spec: dag_spec attribute
        :type dag_spec: DagSpec (optional)

        :param inline: 是否内联子模板
        :type inline: bool (optional)

        :param retries: 重试次数
        :type retries: int (optional)

        :param retry_interval: 重试间隔，单位毫秒
        :type retry_interval: int (optional)

        :param timeout: 超时时长，单位毫秒
        :type timeout: int (optional)

        :param init_context: 初始上下文
        :type init_context: object (optional)

        :param loops: 循环配置列表
        :type loops: List[object] (optional)

        :param parallelism_ratio: 允许的并行比例，取值 [0,1]
        :type parallelism_ratio: float (optional)

        :param parallelism_count: 允许的并行个数
        :type parallelism_count: int (optional)

        :param allowed_failure_ratio: 允许失败的 loops 比例，取值 [0,1]
        :type allowed_failure_ratio: float (optional)

        :param allowed_failure_count: 允许失败的 loops 个数
        :type allowed_failure_count: int (optional)

        :param manually: 是否需要手动触发
        :type manually: bool (optional)

        :param pause_on_failure: 失败后是否暂停
        :type pause_on_failure: bool (optional)

        :param schedule_delay_milli: 延时启动，单位毫秒
        :type schedule_delay_milli: int (optional)

        :param wait_on_agent_milli: 等待 agent 就绪的超时时长，单位毫秒
        :type wait_on_agent_milli: int (optional)

        :param condition: 执行条件表达式
        :type condition: object (optional)

        :param breakpoints: 断点列表
        :type breakpoints: List[int] (optional)

        :param trigger_rule: 触发规则，默认 ALL_SUCCESS
        :type trigger_rule: str (optional)

        :param loop_window_type: loop 窗口类型，默认 SLICING
        :type loop_window_type: str (optional)

        :param worker_selectors: 工作机选择器列表
        :type worker_selectors: List[TagSelector] (optional)

        :param collect_children_context: 子执行上下文收集策略
        :type collect_children_context: str (optional)

        :param rollback_operator: rollback_operator attribute
        :type rollback_operator: TaskOperatorSummary (optional)

        :param events: 关联审计事件列表
        :type events: List[EventModel] (optional)

        :param init_operators: 初始 operator 列表
        :type init_operators: List[TaskOperatorSummary] (optional)

        :param by_bsm_agent: 是否通过 BSM Agent 执行
        :type by_bsm_agent: bool (optional)
        """
        super().__init__()
        self.name = name
        self.description = description
        self.tags = tags
        self.operator = operator
        self.dag_spec = dag_spec
        self.inline = inline
        self.retries = retries
        self.retry_interval = retry_interval
        self.timeout = timeout
        self.init_context = init_context
        self.loops = loops
        self.parallelism_ratio = parallelism_ratio
        self.parallelism_count = parallelism_count
        self.allowed_failure_ratio = allowed_failure_ratio
        self.allowed_failure_count = allowed_failure_count
        self.manually = manually
        self.pause_on_failure = pause_on_failure
        self.schedule_delay_milli = schedule_delay_milli
        self.wait_on_agent_milli = wait_on_agent_milli
        self.condition = condition
        self.breakpoints = breakpoints
        self.trigger_rule = trigger_rule
        self.loop_window_type = loop_window_type
        self.worker_selectors = worker_selectors
        self.collect_children_context = collect_children_context
        self.rollback_operator = rollback_operator
        self.events = events
        self.init_operators = init_operators
        self.by_bsm_agent = by_bsm_agent

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
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.tags is not None:
            result['tags'] = self.tags
        if self.operator is not None:
            result['operator'] = self.operator
        if self.dag_spec is not None:
            result['dagSpec'] = self.dag_spec.to_dict()
        if self.inline is not None:
            result['inline'] = self.inline
        if self.retries is not None:
            result['retries'] = self.retries
        if self.retry_interval is not None:
            result['retryInterval'] = self.retry_interval
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.init_context is not None:
            result['initContext'] = self.init_context
        if self.loops is not None:
            result['loops'] = self.loops
        if self.parallelism_ratio is not None:
            result['parallelismRatio'] = self.parallelism_ratio
        if self.parallelism_count is not None:
            result['parallelismCount'] = self.parallelism_count
        if self.allowed_failure_ratio is not None:
            result['allowedFailureRatio'] = self.allowed_failure_ratio
        if self.allowed_failure_count is not None:
            result['allowedFailureCount'] = self.allowed_failure_count
        if self.manually is not None:
            result['manually'] = self.manually
        if self.pause_on_failure is not None:
            result['pauseOnFailure'] = self.pause_on_failure
        if self.schedule_delay_milli is not None:
            result['scheduleDelayMilli'] = self.schedule_delay_milli
        if self.wait_on_agent_milli is not None:
            result['waitOnAgentMilli'] = self.wait_on_agent_milli
        if self.condition is not None:
            result['condition'] = self.condition
        if self.breakpoints is not None:
            result['breakpoints'] = self.breakpoints
        if self.trigger_rule is not None:
            result['triggerRule'] = self.trigger_rule
        if self.loop_window_type is not None:
            result['loopWindowType'] = self.loop_window_type
        if self.worker_selectors is not None:
            result['workerSelectors'] = [i.to_dict() for i in self.worker_selectors]
        if self.collect_children_context is not None:
            result['collectChildrenContext'] = self.collect_children_context
        if self.rollback_operator is not None:
            result['rollbackOperator'] = self.rollback_operator.to_dict()
        if self.events is not None:
            result['events'] = [i.to_dict() for i in self.events]
        if self.init_operators is not None:
            result['initOperators'] = [i.to_dict() for i in self.init_operators]
        if self.by_bsm_agent is not None:
            result['byBsmAgent'] = self.by_bsm_agent
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TaskOperatorSummary

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('dagSpec') is not None:
            # 延迟导入，避免与 dag_spec 模块形成顶层循环导入
            from baiducloud_python_sdk_oos.models.dag_spec import DagSpec
            self.dag_spec = DagSpec().from_dict(m.get('dagSpec'))
        if m.get('inline') is not None:
            self.inline = m.get('inline')
        if m.get('retries') is not None:
            self.retries = m.get('retries')
        if m.get('retryInterval') is not None:
            self.retry_interval = m.get('retryInterval')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('initContext') is not None:
            self.init_context = m.get('initContext')
        if m.get('loops') is not None:
            self.loops = m.get('loops')
        if m.get('parallelismRatio') is not None:
            self.parallelism_ratio = m.get('parallelismRatio')
        if m.get('parallelismCount') is not None:
            self.parallelism_count = m.get('parallelismCount')
        if m.get('allowedFailureRatio') is not None:
            self.allowed_failure_ratio = m.get('allowedFailureRatio')
        if m.get('allowedFailureCount') is not None:
            self.allowed_failure_count = m.get('allowedFailureCount')
        if m.get('manually') is not None:
            self.manually = m.get('manually')
        if m.get('pauseOnFailure') is not None:
            self.pause_on_failure = m.get('pauseOnFailure')
        if m.get('scheduleDelayMilli') is not None:
            self.schedule_delay_milli = m.get('scheduleDelayMilli')
        if m.get('waitOnAgentMilli') is not None:
            self.wait_on_agent_milli = m.get('waitOnAgentMilli')
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('breakpoints') is not None:
            self.breakpoints = m.get('breakpoints')
        if m.get('triggerRule') is not None:
            self.trigger_rule = m.get('triggerRule')
        if m.get('loopWindowType') is not None:
            self.loop_window_type = m.get('loopWindowType')
        if m.get('workerSelectors') is not None:
            self.worker_selectors = [TagSelector().from_dict(i) for i in m.get('workerSelectors')]
        if m.get('collectChildrenContext') is not None:
            self.collect_children_context = m.get('collectChildrenContext')
        if m.get('rollbackOperator') is not None:
            self.rollback_operator = TaskOperatorSummary().from_dict(m.get('rollbackOperator'))
        if m.get('events') is not None:
            self.events = [EventModel().from_dict(i) for i in m.get('events')]
        if m.get('initOperators') is not None:
            self.init_operators = [TaskOperatorSummary().from_dict(i) for i in m.get('initOperators')]
        if m.get('byBsmAgent') is not None:
            self.by_bsm_agent = m.get('byBsmAgent')
        return self
