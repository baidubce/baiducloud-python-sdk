"""
Operator information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_oos.models.key_value_pair import KeyValuePair

from baiducloud_python_sdk_oos.models.parallelism_control import ParallelismControl

from baiducloud_python_sdk_oos.models.allowed_failure_control import AllowedFailureControl


class Operator(AbstractModel):
    """
    Operator
    """

    def __init__(
        self,
        name=None,
        description=None,
        tags=None,
        operator=None,
        label=None,
        template=None,
        retries=None,
        retry_interval=None,
        timeout=None,
        parallelism_ratio=None,
        parallelism_count=None,
        parallelism_control=None,
        allowed_failure_ratio=None,
        allowed_failure_count=None,
        allowed_failure_control=None,
        manually=None,
        schedule_delay_milli=None,
        wait_on_agent_milli=None,
        pause_on_failure=None,
        condition=None,
        breakpoints=None,
        trigger_rule=None,
        loop_window_type=None,
        properties=None,
        loops=None,
    ):
        """
        Initialize Operator instance.

        :param name: 任务自定义名称，同一个模板下不允许重复（必填）
        :type name: str (optional)

        :param description: 任务描述，选填
        :type description: str (optional)

        :param tags: 任务标签列表
        :type tags: List[KeyValuePair] (optional)

        :param operator: 任务 ID/类型标识（如 BCE::BCC::StopInstance）；与 template.ref 不可同时为空
        :type operator: str (optional)

        :param label: 任务显示名称
        :type label: str (optional)

        :param template: template attribute
        :type template: Template (optional)

        :param retries: 重试次数，默认 0，表示不重试
        :type retries: int (optional)

        :param retry_interval: 重试间隔，单位毫秒，默认 300000（5 分钟）
        :type retry_interval: int (optional)

        :param timeout: 超时时长，单位毫秒，默认 21600000（6 小时）；超时将触发重试
        :type timeout: int (optional)

        :param parallelism_ratio: 允许的并行比例，取值 [0,1]，默认 0；仅当 loops 字段存在时生效
        :type parallelism_ratio: float (optional)

        :param parallelism_count: 允许的并行个数，默认 0；与 parallelismRatio 二选一
        :type parallelism_count: int (optional)

        :param parallelism_control: parallelism_control attribute
        :type parallelism_control: ParallelismControl (optional)

        :param allowed_failure_ratio: 允许失败的 loops 比例，取值 [0,1]，默认 0
        :type allowed_failure_ratio: float (optional)

        :param allowed_failure_count: 允许失败的 loops 个数，默认 0
        :type allowed_failure_count: int (optional)

        :param allowed_failure_control: allowed_failure_control attribute
        :type allowed_failure_control: AllowedFailureControl (optional)

        :param manually: 是否需要手动执行，默认 false
        :type manually: bool (optional)

        :param schedule_delay_milli: 延时启动，单位毫秒，默认 0
        :type schedule_delay_milli: int (optional)

        :param wait_on_agent_milli: 等待 Agent 上线毫秒数
        :type wait_on_agent_milli: int (optional)

        :param pause_on_failure: 失败后是否暂停，默认 false
        :type pause_on_failure: bool (optional)

        :param condition: 条件表达式，节点是否执行的判断依据（结构由具体表达式决定）
        :type condition: object (optional)

        :param breakpoints: 断点列表
        :type breakpoints: List[int] (optional)

        :param trigger_rule: 触发规则，默认 ALL_SUCCESS
        :type trigger_rule: str (optional)

        :param loop_window_type: 循环窗口类型，默认 SLICING
        :type loop_window_type: str (optional)

        :param properties: 任务执行所需参数取值
        :type properties: object (optional)

        :param loops: 循环执行参数列表，与 targetInstances 不能同时设置
        :type loops: List[object] (optional)
        """
        super().__init__()
        self.name = name
        self.description = description
        self.tags = tags
        self.operator = operator
        self.label = label
        self.template = template
        self.retries = retries
        self.retry_interval = retry_interval
        self.timeout = timeout
        self.parallelism_ratio = parallelism_ratio
        self.parallelism_count = parallelism_count
        self.parallelism_control = parallelism_control
        self.allowed_failure_ratio = allowed_failure_ratio
        self.allowed_failure_count = allowed_failure_count
        self.allowed_failure_control = allowed_failure_control
        self.manually = manually
        self.schedule_delay_milli = schedule_delay_milli
        self.wait_on_agent_milli = wait_on_agent_milli
        self.pause_on_failure = pause_on_failure
        self.condition = condition
        self.breakpoints = breakpoints
        self.trigger_rule = trigger_rule
        self.loop_window_type = loop_window_type
        self.properties = properties
        self.loops = loops

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
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.operator is not None:
            result['operator'] = self.operator
        if self.label is not None:
            result['label'] = self.label
        if self.template is not None:
            result['template'] = self.template.to_dict()
        if self.retries is not None:
            result['retries'] = self.retries
        if self.retry_interval is not None:
            result['retryInterval'] = self.retry_interval
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.parallelism_ratio is not None:
            result['parallelismRatio'] = self.parallelism_ratio
        if self.parallelism_count is not None:
            result['parallelismCount'] = self.parallelism_count
        if self.parallelism_control is not None:
            result['parallelismControl'] = self.parallelism_control.to_dict()
        if self.allowed_failure_ratio is not None:
            result['allowedFailureRatio'] = self.allowed_failure_ratio
        if self.allowed_failure_count is not None:
            result['allowedFailureCount'] = self.allowed_failure_count
        if self.allowed_failure_control is not None:
            result['allowedFailureControl'] = self.allowed_failure_control.to_dict()
        if self.manually is not None:
            result['manually'] = self.manually
        if self.schedule_delay_milli is not None:
            result['scheduleDelayMilli'] = self.schedule_delay_milli
        if self.wait_on_agent_milli is not None:
            result['waitOnAgentMilli'] = self.wait_on_agent_milli
        if self.pause_on_failure is not None:
            result['pauseOnFailure'] = self.pause_on_failure
        if self.condition is not None:
            result['condition'] = self.condition
        if self.breakpoints is not None:
            result['breakpoints'] = self.breakpoints
        if self.trigger_rule is not None:
            result['triggerRule'] = self.trigger_rule
        if self.loop_window_type is not None:
            result['loopWindowType'] = self.loop_window_type
        if self.properties is not None:
            result['properties'] = self.properties
        if self.loops is not None:
            result['loops'] = self.loops
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Operator

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('tags') is not None:
            self.tags = [KeyValuePair().from_dict(i) for i in m.get('tags')]
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('template') is not None:
            # 延迟导入，避免与 template 模块形成顶层循环导入
            from baiducloud_python_sdk_oos.models.template import Template
            self.template = Template().from_dict(m.get('template'))
        if m.get('retries') is not None:
            self.retries = m.get('retries')
        if m.get('retryInterval') is not None:
            self.retry_interval = m.get('retryInterval')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('parallelismRatio') is not None:
            self.parallelism_ratio = m.get('parallelismRatio')
        if m.get('parallelismCount') is not None:
            self.parallelism_count = m.get('parallelismCount')
        if m.get('parallelismControl') is not None:
            self.parallelism_control = ParallelismControl().from_dict(m.get('parallelismControl'))
        if m.get('allowedFailureRatio') is not None:
            self.allowed_failure_ratio = m.get('allowedFailureRatio')
        if m.get('allowedFailureCount') is not None:
            self.allowed_failure_count = m.get('allowedFailureCount')
        if m.get('allowedFailureControl') is not None:
            self.allowed_failure_control = AllowedFailureControl().from_dict(m.get('allowedFailureControl'))
        if m.get('manually') is not None:
            self.manually = m.get('manually')
        if m.get('scheduleDelayMilli') is not None:
            self.schedule_delay_milli = m.get('scheduleDelayMilli')
        if m.get('waitOnAgentMilli') is not None:
            self.wait_on_agent_milli = m.get('waitOnAgentMilli')
        if m.get('pauseOnFailure') is not None:
            self.pause_on_failure = m.get('pauseOnFailure')
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('breakpoints') is not None:
            self.breakpoints = m.get('breakpoints')
        if m.get('triggerRule') is not None:
            self.trigger_rule = m.get('triggerRule')
        if m.get('loopWindowType') is not None:
            self.loop_window_type = m.get('loopWindowType')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('loops') is not None:
            self.loops = m.get('loops')
        return self
