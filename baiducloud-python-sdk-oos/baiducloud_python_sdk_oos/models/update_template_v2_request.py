"""
Request entity for UpdateTemplateV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_oos.models.key_value_pair import KeyValuePair
from baiducloud_python_sdk_oos.models.operator import Operator
from baiducloud_python_sdk_oos.models.link_model import LinkModel
from baiducloud_python_sdk_oos.models.model_property import ModelProperty


class UpdateTemplateV2Request(AbstractModel):
    """
    Request entity for UpdateTemplateV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        id,
        name,
        operators,
        namespace=None,
        description=None,
        tags=None,
        linear=None,
        parallelism=None,
        links=None,
        properties=None,
    ):
        """
        Initialize UpdateTemplateV2Request request entity.

        :param namespace: 名称空间，默认 default
        :type namespace: str (optional)

        :param id: 模板唯一标识，由服务端生成，更新模版需要传递此字段，查询详情和列表时响应此字段
        :type id: str (required)

        :param name: 模板名称，和原名称保持一致
        :type name: str (required)

        :param description: 模板描述
        :type description: str (optional)

        :param tags: 模板标签
        :type tags: List[KeyValuePair] (optional)

        :param linear: 任务是否串行执行，默认false
        :type linear: bool (optional)

        :param parallelism: 并发度，当linear=false的时候，可以控制Operator并发执行的数量
        :type parallelism: int (optional)

        :param operators: 模板任务步骤列表
        :type operators: List[Operator] (required)

        :param links: 描述 operator 之间的拓扑关系，linear=false 时必填
        :type links: List[LinkModel] (optional)

        :param properties: 全局参数列表
        :type properties: List[ModelProperty] (optional)
        """
        super().__init__()
        self.namespace = namespace
        self.id = id
        self.name = name
        self.description = description
        self.tags = tags
        self.linear = linear
        self.parallelism = parallelism
        self.operators = operators
        self.links = links
        self.properties = properties

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateTemplateV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
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
        return self
