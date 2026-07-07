"""
Request entity for CreateAgentRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateAgentRequest(AbstractModel):
    """
    Request entity for CreateAgentRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, description=None, allowed_resource_oauth2_return_urls=None):
        """
        Initialize CreateAgentRequest request entity.

        :param name: Agent 名称，1-64 字符，仅允许字母、数字、下划线和连字符（^[a-zA-Z0-9_-]+$）
        :type name: str (required)

        :param description: Agent 描述，1-128 字符
        :type description: str (optional)

        :param allowed_resource_oauth2_return_urls: OAuth2 回调 URL 白名单列表，最多 10 个，每个最长 512 字符
        :type allowed_resource_oauth2_return_urls: List[str] (optional)
        """
        super().__init__()
        self.name = name
        self.description = description
        self.allowed_resource_oauth2_return_urls = allowed_resource_oauth2_return_urls

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
        if self.description is not None:
            result['description'] = self.description
        if self.allowed_resource_oauth2_return_urls is not None:
            result['allowedResourceOauth2ReturnUrls'] = self.allowed_resource_oauth2_return_urls
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAgentRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('allowedResourceOauth2ReturnUrls') is not None:
            self.allowed_resource_oauth2_return_urls = m.get('allowedResourceOauth2ReturnUrls')
        return self
