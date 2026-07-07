"""
Request entity for CreateCredentialProviderRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateCredentialProviderRequest(AbstractModel):
    """
    Request entity for CreateCredentialProviderRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, type, credential, desc=None):
        """
        Initialize CreateCredentialProviderRequest request entity.

        :param name: 凭证提供方名称，1-64 字符，仅允许字母、数字、下划线和连字符（^[a-zA-Z0-9_-]+$）
        :type name: str (required)

        :param type: 凭证类型：API_KEY / OAUTH2 / STS
        :type type: str (required)

        :param desc: 描述，最多 128 字符
        :type desc: str (optional)

        :param credential: credential parameter
        :type credential: object (required)
        """
        super().__init__()
        self.name = name
        self.type = type
        self.desc = desc
        self.credential = credential

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
        if self.type is not None:
            result['type'] = self.type
        if self.desc is not None:
            result['desc'] = self.desc
        if self.credential is not None:
            result['credential'] = self.credential
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateCredentialProviderRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('credential') is not None:
            self.credential = m.get('credential')
        return self
