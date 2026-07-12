"""
OperatorSpec information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_oos.models.key_value_pair import KeyValuePair

from baiducloud_python_sdk_oos.models.template import Template

from baiducloud_python_sdk_oos.models.model_property import ModelProperty

from baiducloud_python_sdk_oos.models.model_property import ModelProperty

from baiducloud_python_sdk_oos.models.loop_model import LoopModel


class OperatorSpec(AbstractModel):
    """
    OperatorSpec
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
        allowed_failure_ratio=None,
        allowed_failure_count=None,
        manually=None,
        schedule_delay_milli=None,
        wait_on_agent_milli=None,
        auto_rollback=None,
        pause_on_failure=None,
        properties=None,
        output=None,
        init_context=None,
        loops=None,
        parallel=None,
    ):
        """
        Initialize OperatorSpec instance.

        :param name: operator 名称
        :type name: str (optional)

        :param description: operator 描述
        :type description: str (optional)

        :param tags: 标签列表
        :type tags: List[KeyValuePair] (optional)

        :param operator: operator 类型
        :type operator: str (optional)

        :param label: 显示名称
        :type label: str (optional)

        :param template: template attribute
        :type template: Template (optional)

        :param retries: 重试次数
        :type retries: int (optional)

        :param retry_interval: 重试间隔，单位毫秒，默认 300000
        :type retry_interval: int (optional)

        :param timeout: 超时时长，单位毫秒
        :type timeout: int (optional)

        :param parallelism_ratio: 并行比例
        :type parallelism_ratio: float (optional)

        :param parallelism_count: 并行个数
        :type parallelism_count: int (optional)

        :param allowed_failure_ratio: 允许失败比例
        :type allowed_failure_ratio: float (optional)

        :param allowed_failure_count: 允许失败个数
        :type allowed_failure_count: int (optional)

        :param manually: 是否手动执行
        :type manually: bool (optional)

        :param schedule_delay_milli: 延时启动毫秒数
        :type schedule_delay_milli: int (optional)

        :param wait_on_agent_milli: 等待Agent可用毫秒数
        :type wait_on_agent_milli: int (optional)

        :param auto_rollback: 是否自动回滚
        :type auto_rollback: bool (optional)

        :param pause_on_failure: 失败后是否暂停
        :type pause_on_failure: bool (optional)

        :param properties: 参数定义列表
        :type properties: List[ModelProperty] (optional)

        :param output: 输出参数定义列表
        :type output: List[ModelProperty] (optional)

        :param init_context: 初始上下文
        :type init_context: object (optional)

        :param loops: 循环配置列表
        :type loops: List[LoopModel] (optional)

        :param parallel: 是否并行
        :type parallel: bool (optional)
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
        self.allowed_failure_ratio = allowed_failure_ratio
        self.allowed_failure_count = allowed_failure_count
        self.manually = manually
        self.schedule_delay_milli = schedule_delay_milli
        self.wait_on_agent_milli = wait_on_agent_milli
        self.auto_rollback = auto_rollback
        self.pause_on_failure = pause_on_failure
        self.properties = properties
        self.output = output
        self.init_context = init_context
        self.loops = loops
        self.parallel = parallel

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
        if self.allowed_failure_ratio is not None:
            result['allowedFailureRatio'] = self.allowed_failure_ratio
        if self.allowed_failure_count is not None:
            result['allowedFailureCount'] = self.allowed_failure_count
        if self.manually is not None:
            result['manually'] = self.manually
        if self.schedule_delay_milli is not None:
            result['scheduleDelayMilli'] = self.schedule_delay_milli
        if self.wait_on_agent_milli is not None:
            result['waitOnAgentMilli'] = self.wait_on_agent_milli
        if self.auto_rollback is not None:
            result['autoRollback'] = self.auto_rollback
        if self.pause_on_failure is not None:
            result['pauseOnFailure'] = self.pause_on_failure
        if self.properties is not None:
            result['properties'] = [i.to_dict() for i in self.properties]
        if self.output is not None:
            result['output'] = [i.to_dict() for i in self.output]
        if self.init_context is not None:
            result['initContext'] = self.init_context
        if self.loops is not None:
            result['loops'] = [i.to_dict() for i in self.loops]
        if self.parallel is not None:
            result['parallel'] = self.parallel
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: OperatorSpec

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
        if m.get('allowedFailureRatio') is not None:
            self.allowed_failure_ratio = m.get('allowedFailureRatio')
        if m.get('allowedFailureCount') is not None:
            self.allowed_failure_count = m.get('allowedFailureCount')
        if m.get('manually') is not None:
            self.manually = m.get('manually')
        if m.get('scheduleDelayMilli') is not None:
            self.schedule_delay_milli = m.get('scheduleDelayMilli')
        if m.get('waitOnAgentMilli') is not None:
            self.wait_on_agent_milli = m.get('waitOnAgentMilli')
        if m.get('autoRollback') is not None:
            self.auto_rollback = m.get('autoRollback')
        if m.get('pauseOnFailure') is not None:
            self.pause_on_failure = m.get('pauseOnFailure')
        if m.get('properties') is not None:
            self.properties = [ModelProperty().from_dict(i) for i in m.get('properties')]
        if m.get('output') is not None:
            self.output = [ModelProperty().from_dict(i) for i in m.get('output')]
        if m.get('initContext') is not None:
            self.init_context = m.get('initContext')
        if m.get('loops') is not None:
            self.loops = [LoopModel().from_dict(i) for i in m.get('loops')]
        if m.get('parallel') is not None:
            self.parallel = m.get('parallel')
        return self
