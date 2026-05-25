"""
Request entity for CreateAnIpv6GatewayResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateAnIpv6GatewayResponse(BceResponse):
    """
    CreateAnIpv6GatewayResponse
    """

    def __init__(self, gateway_id=None):
        """
        Initialize CreateAnIpv6GatewayResponse response.

        :param gateway_id: IPv6网关的ID
        :type gateway_id: str (optional)
        """
        super().__init__()
        self.gateway_id = gateway_id

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
            result['metadata'] = dict(self.metadata)
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAnIpv6GatewayResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        return self
