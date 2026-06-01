"""
Request entity for CreateDedicatedChannelRouteParametersRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateDedicatedChannelRouteParametersRequest(AbstractModel):
    """
    Request entity for CreateDedicatedChannelRouteParametersRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, et_id, et_channel_id, route_type, client_token=None, networks=None, ipv6_networks=None):
        """
        Initialize CreateDedicatedChannelRouteParametersRequest request entity.

        :param et_id: et_id parameter
        :type et_id: str (required)

        :param et_channel_id: et_channel_id parameter
        :type et_channel_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param networks: IPv4路由cidr
        :type networks: List[str] (optional)

        :param ipv6_networks: IPv6路由cidr
        :type ipv6_networks: List[str] (optional)

        :param route_type: 路由类型，当前支持static-route
        :type route_type: str (required)
        """
        super().__init__()
        self.et_id = et_id
        self.et_channel_id = et_channel_id
        self.client_token = client_token
        self.networks = networks
        self.ipv6_networks = ipv6_networks
        self.route_type = route_type

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
        if self.networks is not None:
            result['networks'] = self.networks
        if self.ipv6_networks is not None:
            result['ipv6Networks'] = self.ipv6_networks
        if self.route_type is not None:
            result['routeType'] = self.route_type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateDedicatedChannelRouteParametersRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('etId') is not None:
            self.et_id = m.get('etId')
        if m.get('etChannelId') is not None:
            self.et_channel_id = m.get('etChannelId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('networks') is not None:
            self.networks = m.get('networks')
        if m.get('ipv6Networks') is not None:
            self.ipv6_networks = m.get('ipv6Networks')
        if m.get('routeType') is not None:
            self.route_type = m.get('routeType')
        return self
