"""
Request entity for UpdateServiceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateServiceRequest(AbstractModel):
    """
    Request entity for UpdateServiceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, service, client_token=None, name=None, description=None):
        """
        Initialize UpdateServiceRequest request entity.

        :param service: service parameter
        :type service: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 服务发布点名称,大小写字母、数字以及-_/.特殊字符，必须以字母开头，长度1-65
        :type name: str (optional)

        :param description: 服务发布点描述，不超过200字符
        :type description: str (optional)
        """
        super().__init__()
        self.service = service
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
        :rtype: UpdateServiceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
