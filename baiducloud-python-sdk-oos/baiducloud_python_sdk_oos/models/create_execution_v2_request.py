"""
Request entity for CreateExecutionV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_oos.models.template import Template
from baiducloud_python_sdk_oos.models.tag import Tag


class CreateExecutionV2Request(AbstractModel):
    """
    Request entity for CreateExecutionV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, template, locale=None, description=None, parallelism=None, manually=None, properties=None, tags=None
    ):
        """
        Initialize CreateExecutionV2Request request entity.

        :param locale: locale parameter
        :type locale: str (optional)

        :param description: 执行描述
        :type description: str (optional)

        :param template: template parameter
        :type template: Template (required)

        :param parallelism: 并发度
        :type parallelism: int (optional)

        :param manually: 是否手动触发
        :type manually: bool (optional)

        :param properties: 全局参数取值集合
        :type properties: Dict[str, object] (optional)

        :param tags: 执行绑定标签列表
        :type tags: List[Tag] (optional)
        """
        super().__init__()
        self.locale = locale
        self.description = description
        self.template = template
        self.parallelism = parallelism
        self.manually = manually
        self.properties = properties
        self.tags = tags

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
        if self.description is not None:
            result['description'] = self.description
        if self.template is not None:
            result['template'] = self.template.to_dict()
        if self.parallelism is not None:
            result['parallelism'] = self.parallelism
        if self.manually is not None:
            result['manually'] = self.manually
        if self.properties is not None:
            result['properties'] = self.properties
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateExecutionV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('locale') is not None:
            self.locale = m.get('locale')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('template') is not None:
            self.template = Template().from_dict(m.get('template'))
        if m.get('parallelism') is not None:
            self.parallelism = m.get('parallelism')
        if m.get('manually') is not None:
            self.manually = m.get('manually')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        return self
