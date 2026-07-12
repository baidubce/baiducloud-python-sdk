"""
DagSpec information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_oos.models.task_operator_summary import TaskOperatorSummary

from baiducloud_python_sdk_oos.models.link_model import LinkModel

from baiducloud_python_sdk_oos.models.input_model import InputModel

from baiducloud_python_sdk_oos.models.output_model import OutputModel


class DagSpec(AbstractModel):
    """
    DagSpec
    """

    def __init__(
        self,
        ref=None,
        namespace=None,
        name=None,
        names=None,
        description=None,
        tags=None,
        operators=None,
        linear=None,
        links=None,
        inputs=None,
        outputs=None,
        parallelism=None,
        extra=None,
        created_timestamp=None,
        updated_timestamp=None,
    ):
        """
        Initialize DagSpec instance.

        :param ref: 引用的模板 ref 标识
        :type ref: str (optional)

        :param namespace: 名称空间
        :type namespace: str (optional)

        :param name: 模板名称
        :type name: str (optional)

        :param names: 模板名称列表（批量查询时使用）
        :type names: List[str] (optional)

        :param description: 模板描述
        :type description: str (optional)

        :param tags: 标签键值对
        :type tags: object (optional)

        :param operators: operator 列表
        :type operators: List[TaskOperatorSummary] (optional)

        :param linear: 是否线性执行（operator 顺序依次执行）
        :type linear: bool (optional)

        :param links: operator 间依赖关系列表
        :type links: List[LinkModel] (optional)

        :param inputs: 输入参数定义列表
        :type inputs: List[InputModel] (optional)

        :param outputs: 输出参数定义列表
        :type outputs: List[OutputModel] (optional)

        :param parallelism: 并发度
        :type parallelism: int (optional)

        :param extra: 扩展字段
        :type extra: object (optional)

        :param created_timestamp: 创建时间，Unix 时间戳，单位：毫秒
        :type created_timestamp: int (optional)

        :param updated_timestamp: 最近更新时间，Unix 时间戳，单位：毫秒
        :type updated_timestamp: int (optional)
        """
        super().__init__()
        self.ref = ref
        self.namespace = namespace
        self.name = name
        self.names = names
        self.description = description
        self.tags = tags
        self.operators = operators
        self.linear = linear
        self.links = links
        self.inputs = inputs
        self.outputs = outputs
        self.parallelism = parallelism
        self.extra = extra
        self.created_timestamp = created_timestamp
        self.updated_timestamp = updated_timestamp

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
        if self.ref is not None:
            result['ref'] = self.ref
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        if self.names is not None:
            result['names'] = self.names
        if self.description is not None:
            result['description'] = self.description
        if self.tags is not None:
            result['tags'] = self.tags
        if self.operators is not None:
            result['operators'] = [i.to_dict() for i in self.operators]
        if self.linear is not None:
            result['linear'] = self.linear
        if self.links is not None:
            result['links'] = [i.to_dict() for i in self.links]
        if self.inputs is not None:
            result['inputs'] = [i.to_dict() for i in self.inputs]
        if self.outputs is not None:
            result['outputs'] = [i.to_dict() for i in self.outputs]
        if self.parallelism is not None:
            result['parallelism'] = self.parallelism
        if self.extra is not None:
            result['extra'] = self.extra
        if self.created_timestamp is not None:
            result['createdTimestamp'] = self.created_timestamp
        if self.updated_timestamp is not None:
            result['updatedTimestamp'] = self.updated_timestamp
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DagSpec

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ref') is not None:
            self.ref = m.get('ref')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('names') is not None:
            self.names = m.get('names')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('operators') is not None:
            self.operators = [TaskOperatorSummary().from_dict(i) for i in m.get('operators')]
        if m.get('linear') is not None:
            self.linear = m.get('linear')
        if m.get('links') is not None:
            self.links = [LinkModel().from_dict(i) for i in m.get('links')]
        if m.get('inputs') is not None:
            self.inputs = [InputModel().from_dict(i) for i in m.get('inputs')]
        if m.get('outputs') is not None:
            self.outputs = [OutputModel().from_dict(i) for i in m.get('outputs')]
        if m.get('parallelism') is not None:
            self.parallelism = m.get('parallelism')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('createdTimestamp') is not None:
            self.created_timestamp = m.get('createdTimestamp')
        if m.get('updatedTimestamp') is not None:
            self.updated_timestamp = m.get('updatedTimestamp')
        return self
