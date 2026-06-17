"""
Request entity for CreateLogStoreTemplateRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bls.models.template import Template


class CreateLogStoreTemplateRequest(AbstractModel):
    """
    Request entity for CreateLogStoreTemplateRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, project_patterns, logstore_patterns, priority, template=None):
        """
        Initialize CreateLogStoreTemplateRequest request entity.

        :param name: 模板名称，同user下唯一
        :type name: str (required)

        :param project_patterns: 日志组匹配模式，支持*通配符
        :type project_patterns: List[str] (required)

        :param logstore_patterns: 日志集匹配模式，支持*通配符
        :type logstore_patterns: List[str] (required)

        :param priority: 日志集模板优先级，值越大，优先级越高，同user下唯一
        :type priority: int (required)

        :param template: template parameter
        :type template: Template (optional)
        """
        super().__init__()
        self.name = name
        self.project_patterns = project_patterns
        self.logstore_patterns = logstore_patterns
        self.priority = priority
        self.template = template

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
        if self.name is not None:
            result['name'] = self.name
        if self.project_patterns is not None:
            result['projectPatterns'] = self.project_patterns
        if self.logstore_patterns is not None:
            result['logstorePatterns'] = self.logstore_patterns
        if self.priority is not None:
            result['priority'] = self.priority
        if self.template is not None:
            result['template'] = self.template.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateLogStoreTemplateRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectPatterns') is not None:
            self.project_patterns = m.get('projectPatterns')
        if m.get('logstorePatterns') is not None:
            self.logstore_patterns = m.get('logstorePatterns')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('template') is not None:
            self.template = Template().from_dict(m.get('template'))
        return self
