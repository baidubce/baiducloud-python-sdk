"""
Request entity for Oauth2idpCallbackRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Oauth2idpCallbackRequest(AbstractModel):
    """
    Request entity for Oauth2idpCallbackRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, provider_id, code, state):
        """
        Initialize Oauth2idpCallbackRequest request entity.

        :param provider_id: provider_id parameter
        :type provider_id: str (required)

        :param code: code parameter
        :type code: str (required)

        :param state: state parameter
        :type state: str (required)
        """
        super().__init__()
        self.provider_id = provider_id
        self.code = code
        self.state = state

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
        :rtype: Oauth2idpCallbackRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('providerId') is not None:
            self.provider_id = m.get('providerId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self
