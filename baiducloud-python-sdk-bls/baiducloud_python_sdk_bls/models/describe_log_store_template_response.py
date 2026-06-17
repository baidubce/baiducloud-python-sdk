"""
Request entity for DescribeLogStoreTemplateResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bls.models.template import Template


class DescribeLogStoreTemplateResponse(BceResponse):
    """
    DescribeLogStoreTemplateResponse
    """

    def __init__(
        self,
        success=None,
        code=None,
        message=None,
        name=None,
        project_patterns=None,
        logstore_patterns=None,
        priority=None,
        created_timestamp=None,
        updated_timestamp=None,
        template=None,
    ):
        """
        Initialize DescribeLogStoreTemplateResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 请求码，成功为OK，错误为具体的错误码
        :type code: str (optional)

        :param message: 请求成功为空，失败为具体的错误信息
        :type message: str (optional)

        :param name: 模板名称，同user下唯一
        :type name: str (optional)

        :param project_patterns: 日志组匹配模式，支持*通配符
        :type project_patterns: List[str] (optional)

        :param logstore_patterns: 日志集匹配模式，支持*通配符
        :type logstore_patterns: List[str] (optional)

        :param priority: 日志集模板优先级，值越大，优先级越高，同user下唯一
        :type priority: int (optional)

        :param created_timestamp: 创建时间，UTC时间，格式：2025-04-20T10:01:12Z
        :type created_timestamp: str (optional)

        :param updated_timestamp: 更新时间，UTC时间，格式：2025-04-20T10:01:12Z
        :type updated_timestamp: str (optional)

        :param template: template field
        :type template: Template (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.message = message
        self.name = name
        self.project_patterns = project_patterns
        self.logstore_patterns = logstore_patterns
        self.priority = priority
        self.created_timestamp = created_timestamp
        self.updated_timestamp = updated_timestamp
        self.template = template

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.success is not None:
            result['success'] = self.success
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.name is not None:
            result['name'] = self.name
        if self.project_patterns is not None:
            result['projectPatterns'] = self.project_patterns
        if self.logstore_patterns is not None:
            result['logstorePatterns'] = self.logstore_patterns
        if self.priority is not None:
            result['priority'] = self.priority
        if self.created_timestamp is not None:
            result['createdTimestamp'] = self.created_timestamp
        if self.updated_timestamp is not None:
            result['updatedTimestamp'] = self.updated_timestamp
        if self.template is not None:
            result['template'] = self.template.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeLogStoreTemplateResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectPatterns') is not None:
            self.project_patterns = m.get('projectPatterns')
        if m.get('logstorePatterns') is not None:
            self.logstore_patterns = m.get('logstorePatterns')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('createdTimestamp') is not None:
            self.created_timestamp = m.get('createdTimestamp')
        if m.get('updatedTimestamp') is not None:
            self.updated_timestamp = m.get('updatedTimestamp')
        if m.get('template') is not None:
            self.template = Template().from_dict(m.get('template'))
        return self
