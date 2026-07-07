"""
ResourceCredentialDTO information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ResourceCredentialDTO(AbstractModel):
    """
    ResourceCredentialDTO
    """

    def __init__(self, type=None, name=None, credential=None, credential_api_key=None, expire_at=None):
        """
        Initialize ResourceCredentialDTO instance.

        :param type: 凭证类型（API_KEY）
        :type type: str (optional)

        :param name: 凭证提供方名称
        :type name: str (optional)

        :param credential: 凭证内容
        :type credential: object (optional)

        :param credential_api_key: API Key 明文值
        :type credential_api_key: str (optional)

        :param expire_at: 凭证缓存过期时间（ISO 8601）
        :type expire_at: datetime (optional)
        """
        super().__init__()
        self.type = type
        self.name = name
        self.credential = credential
        self.credential_api_key = credential_api_key
        self.expire_at = expire_at

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
        if self.type is not None:
            result['type'] = self.type
        if self.name is not None:
            result['name'] = self.name
        if self.credential is not None:
            result['credential'] = self.credential
        if self.credential_api_key is not None:
            result['credential.apiKey'] = self.credential_api_key
        if self.expire_at is not None:
            result['expireAt'] = self.expire_at
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ResourceCredentialDTO

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('credential') is not None:
            self.credential = m.get('credential')
        if m.get('credential.apiKey') is not None:
            self.credential_api_key = m.get('credential.apiKey')
        if m.get('expireAt') is not None:
            self.expire_at = m.get('expireAt')
        return self
