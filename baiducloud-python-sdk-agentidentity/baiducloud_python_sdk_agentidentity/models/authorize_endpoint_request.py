"""
Request entity for AuthorizeEndpointRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AuthorizeEndpointRequest(AbstractModel):
    """
    Request entity for AuthorizeEndpointRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, user_pool_id, client_id, redirect_uri, response_type, scope=None, state=None, nonce=None):
        """
        Initialize AuthorizeEndpointRequest request entity.

        :param user_pool_id: user_pool_id parameter
        :type user_pool_id: str (required)

        :param client_id: client_id parameter
        :type client_id: str (required)

        :param redirect_uri: redirect_uri parameter
        :type redirect_uri: str (required)

        :param response_type: response_type parameter
        :type response_type: str (required)

        :param scope: scope parameter
        :type scope: str (optional)

        :param state: state parameter
        :type state: str (optional)

        :param nonce: nonce parameter
        :type nonce: str (optional)
        """
        super().__init__()
        self.user_pool_id = user_pool_id
        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.response_type = response_type
        self.scope = scope
        self.state = state
        self.nonce = nonce

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
        :rtype: AuthorizeEndpointRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userPoolId') is not None:
            self.user_pool_id = m.get('userPoolId')
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('redirectUri') is not None:
            self.redirect_uri = m.get('redirectUri')
        if m.get('responseType') is not None:
            self.response_type = m.get('responseType')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('nonce') is not None:
            self.nonce = m.get('nonce')
        return self
