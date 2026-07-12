"""
Template information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_oos.models.key_value_pair import KeyValuePair

from baiducloud_python_sdk_oos.models.operator import Operator

from baiducloud_python_sdk_oos.models.link_model import LinkModel

from baiducloud_python_sdk_oos.models.model_property import ModelProperty


class Template(AbstractModel):
    """
    Template
    """

    def __init__(
        self,
        id=None,
        ref=None,
        name=None,
        type=None,
        description=None,
        tags=None,
        linear=None,
        parallelism=None,
        operators=None,
        links=None,
        properties=None,
        updated_time=None,
        supported_instance_types=None,
    ):
        """
        Initialize Template instance.

        :param id: 模板唯一标识，由服务端生成，更新模版需要传递此字段，查询详情和列表时响应此字段
        :type id: str (optional)

        :param ref: 创建执行时，使用本字段设置使用的模版id
        :type ref: str (optional)

        :param name: 模板名称，不允许重复
        :type name: str (optional)

        :param type: 模板类型，可选值：INDIVIDUAL（个人模板）,GLOBAL（系统模板）
        :type type: str (optional)

        :param description: 模板描述
        :type description: str (optional)

        :param tags: 模板标签
        :type tags: List[KeyValuePair] (optional)

        :param linear: 任务是否串行执行，默认false
        :type linear: bool (optional)

        :param parallelism: 并发度
        :type parallelism: int (optional)

        :param operators: 模板任务步骤列表
        :type operators: List[Operator] (optional)

        :param links: 描述 operator 之间的拓扑关系，linear=false 时必填
        :type links: List[LinkModel] (optional)

        :param properties: 全局参数列表
        :type properties: List[ModelProperty] (optional)

        :param updated_time: 最后更新时间，查询详情和列表接口返回
        :type updated_time: str (optional)

        :param supported_instance_types: 支持的实例类型列表，目前仅用于系统模版
        :type supported_instance_types: List[str] (optional)
        """
        super().__init__()
        self.id = id
        self.ref = ref
        self.name = name
        self.type = type
        self.description = description
        self.tags = tags
        self.linear = linear
        self.parallelism = parallelism
        self.operators = operators
        self.links = links
        self.properties = properties
        self.updated_time = updated_time
        self.supported_instance_types = supported_instance_types

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
        if self.ref is not None:
            result['ref'] = self.ref
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.description is not None:
            result['description'] = self.description
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.linear is not None:
            result['linear'] = self.linear
        if self.parallelism is not None:
            result['parallelism'] = self.parallelism
        if self.operators is not None:
            result['operators'] = [i.to_dict() for i in self.operators]
        if self.links is not None:
            result['links'] = [i.to_dict() for i in self.links]
        if self.properties is not None:
            result['properties'] = [i.to_dict() for i in self.properties]
        if self.updated_time is not None:
            result['updatedTime'] = self.updated_time
        if self.supported_instance_types is not None:
            result['supportedInstanceTypes'] = self.supported_instance_types
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Template

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('ref') is not None:
            self.ref = m.get('ref')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('tags') is not None:
            self.tags = [KeyValuePair().from_dict(i) for i in m.get('tags')]
        if m.get('linear') is not None:
            self.linear = m.get('linear')
        if m.get('parallelism') is not None:
            self.parallelism = m.get('parallelism')
        if m.get('operators') is not None:
            self.operators = [Operator().from_dict(i) for i in m.get('operators')]
        if m.get('links') is not None:
            self.links = [LinkModel().from_dict(i) for i in m.get('links')]
        if m.get('properties') is not None:
            self.properties = [ModelProperty().from_dict(i) for i in m.get('properties')]
        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')
        if m.get('supportedInstanceTypes') is not None:
            self.supported_instance_types = m.get('supportedInstanceTypes')
        return self
