"""
Request entity for UpdateDnsParserRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateDnsParserRequest(AbstractModel):
    """
    Request entity for UpdateDnsParserRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, resolver_id, client_token=None, name=None, description=None):
        """
        Initialize UpdateDnsParserRequest request entity.

        :param resolver_id: resolver_id parameter
        :type resolver_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 解析器的名称，允许大小写字母、数字、中文以及 `-_/.` 特殊字符，必须以字母或者中文开头，长度1-65
        :type name: str (optional)

        :param description: 解析器描述，不超过200字符，与name不能同时为空
        :type description: str (optional)
        """
        super().__init__()
        self.resolver_id = resolver_id
        self.client_token = client_token
        self.name = name
        self.description = description

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateDnsParserRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('resolverId') is not None:
            self.resolver_id = m.get('resolverId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
