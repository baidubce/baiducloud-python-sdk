"""
EtChannel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_et.models.tag_model import TagModel


class EtChannel(AbstractModel):
    """
    EtChannel
    """

    def __init__(
        self,
        id=None,
        name=None,
        status=None,
        bgp_status=None,
        bgp_route_limit=None,
        ipv6_bgp_status=None,
        baidu_address=None,
        authorized_users=None,
        description=None,
        networks=None,
        customer_address=None,
        route_type=None,
        vlan_id=None,
        enable_ipv6=None,
        baidu_ipv6_address=None,
        customer_ipv6_address=None,
        ipv6_networks=None,
        send_interval=None,
        receiv_interval=None,
        detect_multiplier=None,
        tags=None,
    ):
        """
        Initialize EtChannel instance.

        :param id: 专线通道ID
        :type id: str (optional)

        :param name: 通道名称
        :type name: str (optional)

        :param status: status attribute
        :type status: str (optional)

        :param bgp_status: IPv4 BGP状态，取值范围：up/down
        :type bgp_status: str (optional)

        :param bgp_route_limit: BGP路由条目上限
        :type bgp_route_limit: int (optional)

        :param ipv6_bgp_status: IPv6 BGP状态，取值范围：up/down
        :type ipv6_bgp_status: str (optional)

        :param baidu_address: 云端网络互联IP
        :type baidu_address: str (optional)

        :param authorized_users: 分配对象
        :type authorized_users: List[str] (optional)

        :param description: 描述
        :type description: str (optional)

        :param networks: 路由参数
        :type networks: List[str] (optional)

        :param customer_address: IDC互联IP
        :type customer_address: str (optional)

        :param route_type: 路由协议
        :type route_type: str (optional)

        :param vlan_id: VLAN ID，取值范围：0, 2-4009
        :type vlan_id: int (optional)

        :param enable_ipv6: IPv6功能是否开启，1是0否
        :type enable_ipv6: int (optional)

        :param baidu_ipv6_address: 云端网络侧IPv6互联地址
        :type baidu_ipv6_address: str (optional)

        :param customer_ipv6_address: IDC侧IPv6互联地址
        :type customer_ipv6_address: str (optional)

        :param ipv6_networks: IPv6路由参数
        :type ipv6_networks: List[str] (optional)

        :param send_interval: 报文发送间隔
        :type send_interval: int (optional)

        :param receiv_interval: 报文接收间隔
        :type receiv_interval: int (optional)

        :param detect_multiplier: 检测时间倍数
        :type detect_multiplier: int (optional)

        :param tags: 专线通道绑定的标签列表
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.status = status
        self.bgp_status = bgp_status
        self.bgp_route_limit = bgp_route_limit
        self.ipv6_bgp_status = ipv6_bgp_status
        self.baidu_address = baidu_address
        self.authorized_users = authorized_users
        self.description = description
        self.networks = networks
        self.customer_address = customer_address
        self.route_type = route_type
        self.vlan_id = vlan_id
        self.enable_ipv6 = enable_ipv6
        self.baidu_ipv6_address = baidu_ipv6_address
        self.customer_ipv6_address = customer_ipv6_address
        self.ipv6_networks = ipv6_networks
        self.send_interval = send_interval
        self.receiv_interval = receiv_interval
        self.detect_multiplier = detect_multiplier
        self.tags = tags

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.bgp_status is not None:
            result['bgpStatus'] = self.bgp_status
        if self.bgp_route_limit is not None:
            result['bgpRouteLimit'] = self.bgp_route_limit
        if self.ipv6_bgp_status is not None:
            result['ipv6BgpStatus'] = self.ipv6_bgp_status
        if self.baidu_address is not None:
            result['baiduAddress'] = self.baidu_address
        if self.authorized_users is not None:
            result['authorizedUsers'] = self.authorized_users
        if self.description is not None:
            result['description'] = self.description
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
        if self.send_interval is not None:
            result['sendInterval'] = self.send_interval
        if self.receiv_interval is not None:
            result['receivInterval'] = self.receiv_interval
        if self.detect_multiplier is not None:
            result['detectMultiplier'] = self.detect_multiplier
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EtChannel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('bgpStatus') is not None:
            self.bgp_status = m.get('bgpStatus')
        if m.get('bgpRouteLimit') is not None:
            self.bgp_route_limit = m.get('bgpRouteLimit')
        if m.get('ipv6BgpStatus') is not None:
            self.ipv6_bgp_status = m.get('ipv6BgpStatus')
        if m.get('baiduAddress') is not None:
            self.baidu_address = m.get('baiduAddress')
        if m.get('authorizedUsers') is not None:
            self.authorized_users = m.get('authorizedUsers')
        if m.get('description') is not None:
            self.description = m.get('description')
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
        if m.get('sendInterval') is not None:
            self.send_interval = m.get('sendInterval')
        if m.get('receivInterval') is not None:
            self.receiv_interval = m.get('receivInterval')
        if m.get('detectMultiplier') is not None:
            self.detect_multiplier = m.get('detectMultiplier')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
