"""
Request entity for CreateVpnResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateVpnResponse(BceResponse):
    """
    CreateVpnResponse
    """

    def __init__(self, vpn_id=None):
        """
        Initialize CreateVpnResponse response.

        :param vpn_id: VPN的ID
        :type vpn_id: str (optional)
        """
        super().__init__()
        self.vpn_id = vpn_id

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.vpn_id is not None:
            result['vpnId'] = self.vpn_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateVpnResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        return self
