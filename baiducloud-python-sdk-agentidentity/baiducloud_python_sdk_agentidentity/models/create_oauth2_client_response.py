"""
Request entity for CreateOauth2ClientResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateOauth2ClientResponse(BceResponse):
    """
    CreateOauth2ClientResponse
    """

    def __init__(self, id=None, client_id=None, client_secret=None, name=None, client_type=None, created_at=None):
        """
        Initialize CreateOauth2ClientResponse response.

        :param id: 客户端记录 ID
        :type id: str (optional)

        :param client_id: 系统生成的 OAuth2 client_id
        :type client_id: str (optional)

        :param client_secret: client_secret 明文（仅此一次）
        :type client_secret: str (optional)

        :param name: 客户端名称
        :type name: str (optional)

        :param client_type: 客户端类型：WEB_APP / SPA / M2M
        :type client_type: str (optional)

        :param created_at: 创建时间
        :type created_at: datetime (optional)
        """
        super().__init__()
        self.id = id
        self.client_id = client_id
        self.client_secret = client_secret
        self.name = name
        self.client_type = client_type
        self.created_at = created_at

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
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.client_secret is not None:
            result['clientSecret'] = self.client_secret
        if self.name is not None:
            result['name'] = self.name
        if self.client_type is not None:
            result['clientType'] = self.client_type
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateOauth2ClientResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('clientSecret') is not None:
            self.client_secret = m.get('clientSecret')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('clientType') is not None:
            self.client_type = m.get('clientType')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        return self
