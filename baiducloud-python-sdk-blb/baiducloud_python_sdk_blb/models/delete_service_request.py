"""
Request entity for DeleteServiceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteServiceRequest(AbstractModel):
    """
    Request entity for DeleteServiceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, service, client_token=None):
        """
        Initialize DeleteServiceRequest request entity.

        :param service: service parameter
        :type service: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)
        """
        super().__init__()
        self.service = service
        self.client_token = client_token

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
        :rtype: DeleteServiceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self
