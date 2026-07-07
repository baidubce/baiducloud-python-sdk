"""
Request entity for UserinfoEndpointRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_core.annotation import host


class UserinfoEndpointRequest(AbstractModel):
    """
    Request entity for UserinfoEndpointRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, user_pool_id, authorization):
        """
        Initialize UserinfoEndpointRequest request entity.

        :param user_pool_id: user_pool_id parameter
        :type user_pool_id: str (required)

        :param authorization: authorization parameter
        :type authorization: str (required)
        """
        super().__init__()
        self.user_pool_id = user_pool_id
        self._authorization = authorization

    @property
    @host
    def authorization(self):
        """authorization property"""
        return self._authorization

    @authorization.setter
    def authorization(self, value):
        """Set authorization value"""
        self._authorization = value

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UserinfoEndpointRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userPoolId') is not None:
            self.user_pool_id = m.get('userPoolId')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self
