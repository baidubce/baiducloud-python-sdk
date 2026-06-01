"""
Request entity for UpdateServiceAuthRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_blb.models.auth import Auth


class UpdateServiceAuthRequest(AbstractModel):
    """
    Request entity for UpdateServiceAuthRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, service, auth_list, client_token=None):
        """
        Initialize UpdateServiceAuthRequest request entity.

        :param service: service parameter
        :type service: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param auth_list: 用户授权列表
        :type auth_list: List[Auth] (required)
        """
        super().__init__()
        self.service = service
        self.client_token = client_token
        self.auth_list = auth_list

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
        if self.auth_list is not None:
            result['authList'] = [i.to_dict() for i in self.auth_list]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateServiceAuthRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('authList') is not None:
            self.auth_list = [Auth().from_dict(i) for i in m.get('authList')]
        return self
