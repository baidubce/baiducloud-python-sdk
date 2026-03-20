"""
Request entity for CreateUserGatewayRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateUserGatewayRequest(AbstractModel):
    """
    Request entity for CreateUserGatewayRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, ip, client_token=None, description=None):
        """
        Initialize CreateUserGatewayRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 用户网关名称，以字母开头，支持大小写字母、数字以及 -_/. 特殊字符，不能超过65个字符
        :type name: str (required)

        :param ip: 用户网关IP
        :type ip: str (required)

        :param description: 用户网关描述，不能超过200个字符
        :type description: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.ip = ip
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
        if self.ip is not None:
            result['ip'] = self.ip
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
        :rtype: CreateUserGatewayRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
