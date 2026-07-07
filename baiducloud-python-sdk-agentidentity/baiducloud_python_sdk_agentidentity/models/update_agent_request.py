"""
Request entity for UpdateAgentRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateAgentRequest(AbstractModel):
    """
    Request entity for UpdateAgentRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, agent_id, description=None, allowed_resource_oauth2_return_urls=None):
        """
        Initialize UpdateAgentRequest request entity.

        :param agent_id: Agent ID
        :type agent_id: str (required)

        :param description: 新的描述，1-128 字符
        :type description: str (optional)

        :param allowed_resource_oauth2_return_urls: OAuth2 回调 URL 白名单列表，最多 10 个（全量替换）
        :type allowed_resource_oauth2_return_urls: List[str] (optional)
        """
        super().__init__()
        self.agent_id = agent_id
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
        if self.agent_id is not None:
            result['agentId'] = self.agent_id
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
        :rtype: UpdateAgentRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('allowedResourceOauth2ReturnUrls') is not None:
            self.allowed_resource_oauth2_return_urls = m.get('allowedResourceOauth2ReturnUrls')
        return self
