"""
Request entity for CreateAgentResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateAgentResponse(BceResponse):
    """
    CreateAgentResponse
    """

    def __init__(
        self,
        id=None,
        bce_domain_id=None,
        bce_user_id=None,
        name=None,
        description=None,
        extra=None,
        allowed_resource_oauth2_return_urls=None,
        created_at=None,
        updated_at=None,
    ):
        """
        Initialize CreateAgentResponse response.

        :param id: Agent ID
        :type id: str (optional)

        :param bce_domain_id: BCE 账户 ID
        :type bce_domain_id: str (optional)

        :param bce_user_id: BCE 用户 ID
        :type bce_user_id: str (optional)

        :param name: Agent 名称
        :type name: str (optional)

        :param description: Agent 描述
        :type description: str (optional)

        :param extra: 扩展信息
        :type extra: str (optional)

        :param allowed_resource_oauth2_return_urls: OAuth2 回调 URL 白名单列表
        :type allowed_resource_oauth2_return_urls: List[str] (optional)

        :param created_at: 创建时间
        :type created_at: datetime (optional)

        :param updated_at: 更新时间
        :type updated_at: datetime (optional)
        """
        super().__init__()
        self.id = id
        self.bce_domain_id = bce_domain_id
        self.bce_user_id = bce_user_id
        self.name = name
        self.description = description
        self.extra = extra
        self.allowed_resource_oauth2_return_urls = allowed_resource_oauth2_return_urls
        self.created_at = created_at
        self.updated_at = updated_at

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
        if self.id is not None:
            result['id'] = self.id
        if self.bce_domain_id is not None:
            result['bceDomainId'] = self.bce_domain_id
        if self.bce_user_id is not None:
            result['bceUserId'] = self.bce_user_id
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.extra is not None:
            result['extra'] = self.extra
        if self.allowed_resource_oauth2_return_urls is not None:
            result['allowedResourceOauth2ReturnUrls'] = self.allowed_resource_oauth2_return_urls
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAgentResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('bceDomainId') is not None:
            self.bce_domain_id = m.get('bceDomainId')
        if m.get('bceUserId') is not None:
            self.bce_user_id = m.get('bceUserId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('allowedResourceOauth2ReturnUrls') is not None:
            self.allowed_resource_oauth2_return_urls = m.get('allowedResourceOauth2ReturnUrls')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        return self
