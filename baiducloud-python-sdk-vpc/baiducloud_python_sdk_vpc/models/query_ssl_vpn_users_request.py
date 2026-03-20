"""
Request entity for QuerySslVpnUsersRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QuerySslVpnUsersRequest(AbstractModel):
    """
    Request entity for QuerySslVpnUsersRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, vpn_id, marker=None, max_keys=None, user_name=None):
        """
        Initialize QuerySslVpnUsersRequest request entity.

        :param vpn_id: vpn_id parameter
        :type vpn_id: str (required)

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)

        :param user_name: user_name parameter
        :type user_name: str (optional)
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.marker = marker
        self.max_keys = max_keys
        self.user_name = user_name

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
        :rtype: QuerySslVpnUsersRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self
