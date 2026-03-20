"""
Request entity for BindEipRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BindEipRequest(AbstractModel):
    """
    Request entity for BindEipRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, vpn_id, eip, client_token=None):
        """
        Initialize BindEipRequest request entity.

        :param vpn_id: vpn_id parameter
        :type vpn_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param eip: 需要绑定的EIP
        :type eip: str (required)
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.client_token = client_token
        self.eip = eip

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
        if self.eip is not None:
            result['eip'] = self.eip
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BindEipRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        return self
