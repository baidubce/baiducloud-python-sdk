"""
Request entity for UserGatewayDetailsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UserGatewayDetailsRequest(AbstractModel):
    """
    Request entity for UserGatewayDetailsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, cgw_id):
        """
        Initialize UserGatewayDetailsRequest request entity.

        :param cgw_id: cgw_id parameter
        :type cgw_id: str (required)
        """
        super().__init__()
        self.cgw_id = cgw_id

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
        :rtype: UserGatewayDetailsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cgwId') is not None:
            self.cgw_id = m.get('cgwId')
        return self
