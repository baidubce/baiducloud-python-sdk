"""
Request entity for UpdateSnicRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateSnicRequest(AbstractModel):
    """
    Request entity for UpdateSnicRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, endpoint_id, client_token=None, name=None, description=None):
        """
        Initialize UpdateSnicRequest request entity.

        :param endpoint_id: endpoint_id parameter
        :type endpoint_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 服务网卡名称,长度不超过65个字符，可由数字，字符，下划线、中文组成
        :type name: str (optional)

        :param description: 服务网卡描述，不超过200字符
        :type description: str (optional)
        """
        super().__init__()
        self.endpoint_id = endpoint_id
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
        :rtype: UpdateSnicRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('endpointId') is not None:
            self.endpoint_id = m.get('endpointId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
