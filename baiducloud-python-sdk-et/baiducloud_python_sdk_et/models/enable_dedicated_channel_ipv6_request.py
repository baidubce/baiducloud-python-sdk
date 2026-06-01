"""
Request entity for EnableDedicatedChannelIpv6Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class EnableDedicatedChannelIpv6Request(AbstractModel):
    """
    Request entity for EnableDedicatedChannelIpv6Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, et_id, et_channel_id, baidu_ipv6_address, customer_ipv6_address, client_token=None, ipv6_networks=None
    ):
        """
        Initialize EnableDedicatedChannelIpv6Request request entity.

        :param et_id: et_id parameter
        :type et_id: str (required)

        :param et_channel_id: et_channel_id parameter
        :type et_channel_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param baidu_ipv6_address: 云端网络侧IPv6互联地址
        :type baidu_ipv6_address: str (required)

        :param customer_ipv6_address: IDC侧IPv6互联地址
        :type customer_ipv6_address: str (required)

        :param ipv6_networks: IPv6路由参数，通道路由类型为静态路由时必填
        :type ipv6_networks: List[str] (optional)
        """
        super().__init__()
        self.et_id = et_id
        self.et_channel_id = et_channel_id
        self.client_token = client_token
        self.baidu_ipv6_address = baidu_ipv6_address
        self.customer_ipv6_address = customer_ipv6_address
        self.ipv6_networks = ipv6_networks

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
        if self.baidu_ipv6_address is not None:
            result['baiduIpv6Address'] = self.baidu_ipv6_address
        if self.customer_ipv6_address is not None:
            result['customerIpv6Address'] = self.customer_ipv6_address
        if self.ipv6_networks is not None:
            result['ipv6Networks'] = self.ipv6_networks
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EnableDedicatedChannelIpv6Request

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
        if m.get('baiduIpv6Address') is not None:
            self.baidu_ipv6_address = m.get('baiduIpv6Address')
        if m.get('customerIpv6Address') is not None:
            self.customer_ipv6_address = m.get('customerIpv6Address')
        if m.get('ipv6Networks') is not None:
            self.ipv6_networks = m.get('ipv6Networks')
        return self
