"""
Request entity for ResubmitDedicatedChannelRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ResubmitDedicatedChannelRequest(AbstractModel):
    """
    Request entity for ResubmitDedicatedChannelRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        et_id,
        et_channel_id,
        baidu_address,
        name,
        networks,
        customer_address,
        route_type,
        vlan_id,
        client_token=None,
        authorized_users=None,
        description=None,
        enable_ipv6=None,
        baidu_ipv6_address=None,
        customer_ipv6_address=None,
        ipv6_networks=None,
    ):
        """
        Initialize ResubmitDedicatedChannelRequest request entity.

        :param et_id: et_id parameter
        :type et_id: str (required)

        :param et_channel_id: et_channel_id parameter
        :type et_channel_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param authorized_users: 分配对象
        :type authorized_users: List[str] (optional)

        :param description: 描述
        :type description: str (optional)

        :param baidu_address: 云端网络互联IP
        :type baidu_address: str (required)

        :param name: 通道名称
        :type name: str (required)

        :param networks: 路由参数
        :type networks: List[str] (required)

        :param customer_address: IDC互联IP
        :type customer_address: str (required)

        :param route_type: 路由协议，当前只支持static-route（静态）
        :type route_type: str (required)

        :param vlan_id: VLAN ID，取值范围：0, 2-4009
        :type vlan_id: int (required)

        :param enable_ipv6: IPv6功能是否开启，1是0否，IPv6为白名单功能
        :type enable_ipv6: int (optional)

        :param baidu_ipv6_address: 云端网络侧IPv6互联地址，enableIpv6=1时需要
        :type baidu_ipv6_address: str (optional)

        :param customer_ipv6_address: IDC侧IPv6互联地址，enableIpv6=1时需要
        :type customer_ipv6_address: str (optional)

        :param ipv6_networks: IPv6路由参数，当enableIpv6=1且“routeType”为“static-route”时需要
        :type ipv6_networks: List[str] (optional)
        """
        super().__init__()
        self.et_id = et_id
        self.et_channel_id = et_channel_id
        self.client_token = client_token
        self.authorized_users = authorized_users
        self.description = description
        self.baidu_address = baidu_address
        self.name = name
        self.networks = networks
        self.customer_address = customer_address
        self.route_type = route_type
        self.vlan_id = vlan_id
        self.enable_ipv6 = enable_ipv6
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
        if self.authorized_users is not None:
            result['authorizedUsers'] = self.authorized_users
        if self.description is not None:
            result['description'] = self.description
        if self.baidu_address is not None:
            result['baiduAddress'] = self.baidu_address
        if self.name is not None:
            result['name'] = self.name
        if self.networks is not None:
            result['networks'] = self.networks
        if self.customer_address is not None:
            result['customerAddress'] = self.customer_address
        if self.route_type is not None:
            result['routeType'] = self.route_type
        if self.vlan_id is not None:
            result['vlanId'] = self.vlan_id
        if self.enable_ipv6 is not None:
            result['enableIpv6'] = self.enable_ipv6
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
        :rtype: ResubmitDedicatedChannelRequest

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
        if m.get('authorizedUsers') is not None:
            self.authorized_users = m.get('authorizedUsers')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('baiduAddress') is not None:
            self.baidu_address = m.get('baiduAddress')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('networks') is not None:
            self.networks = m.get('networks')
        if m.get('customerAddress') is not None:
            self.customer_address = m.get('customerAddress')
        if m.get('routeType') is not None:
            self.route_type = m.get('routeType')
        if m.get('vlanId') is not None:
            self.vlan_id = m.get('vlanId')
        if m.get('enableIpv6') is not None:
            self.enable_ipv6 = m.get('enableIpv6')
        if m.get('baiduIpv6Address') is not None:
            self.baidu_ipv6_address = m.get('baiduIpv6Address')
        if m.get('customerIpv6Address') is not None:
            self.customer_ipv6_address = m.get('customerIpv6Address')
        if m.get('ipv6Networks') is not None:
            self.ipv6_networks = m.get('ipv6Networks')
        return self
