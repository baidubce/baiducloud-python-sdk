"""
Request entity for UnDirectEipRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UnDirectEipRequest(AbstractModel):
    """
    Request entity for UnDirectEipRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, eip, client_token=None):
        """
        Initialize UnDirectEipRequest request entity.

        :param eip: eip parameter
        :type eip: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)
        """
        super().__init__()
        self.eip = eip
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
        :rtype: UnDirectEipRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self
