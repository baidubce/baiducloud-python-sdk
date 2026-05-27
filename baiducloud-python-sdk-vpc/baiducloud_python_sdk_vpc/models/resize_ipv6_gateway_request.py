"""
Request entity for ResizeIpv6GatewayRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ResizeIpv6GatewayRequest(AbstractModel):
    """
    Request entity for ResizeIpv6GatewayRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, gateway_id, bandwidth_in_mbps, client_token=None):
        """
        Initialize ResizeIpv6GatewayRequest request entity.

        :param gateway_id: gateway_id parameter
        :type gateway_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param bandwidth_in_mbps: 更新后的IPv6网关的带宽
        :type bandwidth_in_mbps: int (required)
        """
        super().__init__()
        self.gateway_id = gateway_id
        self.client_token = client_token
        self.bandwidth_in_mbps = bandwidth_in_mbps

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
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ResizeIpv6GatewayRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        return self
