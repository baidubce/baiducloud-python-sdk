"""
Vpn information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_vpc.models.vpn_conn import VpnConn

from baiducloud_python_sdk_vpc.models.ssl_vpn_server import SslVpnServer

from baiducloud_python_sdk_vpc.models.tag_model import TagModel


class Vpn(AbstractModel):
    """
    Vpn
    """

    def __init__(
        self,
        vpn_id=None,
        vpn_name=None,
        type=None,
        description=None,
        status=None,
        expired_time=None,
        payment_timing=None,
        eip=None,
        max_connection=None,
        bandwidth_in_mbps=None,
        vpc_id=None,
        vpn_conn_num=None,
        vpn_conns=None,
        ssl_vpn_server=None,
        delete_protect=None,
        tags=None,
        create_time=None,
    ):
        """
        Initialize Vpn instance.

        :param vpn_id: VPN的ID
        :type vpn_id: str (optional)

        :param vpn_name: 名称
        :type vpn_name: str (optional)

        :param type: 网关类型，取值[IPSec, SSL]
        :type type: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param status: vpn状态，active：可用，building：创建中，unconfigured：未配置
        :type status: str (optional)

        :param expired_time: 到期时间
        :type expired_time: str (optional)

        :param payment_timing: 计费类型
        :type payment_timing: str (optional)

        :param eip: 公网IP
        :type eip: str (optional)

        :param max_connection: SSL-VPN最大客户端连接数
        :type max_connection: int (optional)

        :param bandwidth_in_mbps: EIP带宽
        :type bandwidth_in_mbps: int (optional)

        :param vpc_id: VPC的ID
        :type vpc_id: str (optional)

        :param vpn_conn_num: 隧道数量
        :type vpn_conn_num: int (optional)

        :param vpn_conns: VPN隧道列表
        :type vpn_conns: List[VpnConn] (optional)

        :param ssl_vpn_server: ssl_vpn_server attribute
        :type ssl_vpn_server: SslVpnServer (optional)

        :param delete_protect: 是否开启释放保护
        :type delete_protect: bool (optional)

        :param tags: VPN绑定的标签集合
        :type tags: List[TagModel] (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.vpn_name = vpn_name
        self.type = type
        self.description = description
        self.status = status
        self.expired_time = expired_time
        self.payment_timing = payment_timing
        self.eip = eip
        self.max_connection = max_connection
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.vpc_id = vpc_id
        self.vpn_conn_num = vpn_conn_num
        self.vpn_conns = vpn_conns
        self.ssl_vpn_server = ssl_vpn_server
        self.delete_protect = delete_protect
        self.tags = tags
        self.create_time = create_time

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
        if self.vpn_id is not None:
            result['vpnId'] = self.vpn_id
        if self.vpn_name is not None:
            result['vpnName'] = self.vpn_name
        if self.type is not None:
            result['type'] = self.type
        if self.description is not None:
            result['description'] = self.description
        if self.status is not None:
            result['status'] = self.status
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.eip is not None:
            result['eip'] = self.eip
        if self.max_connection is not None:
            result['maxConnection'] = self.max_connection
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vpn_conn_num is not None:
            result['vpnConnNum'] = self.vpn_conn_num
        if self.vpn_conns is not None:
            result['vpnConns'] = [i.to_dict() for i in self.vpn_conns]
        if self.ssl_vpn_server is not None:
            result['sslVpnServer'] = self.ssl_vpn_server.to_dict()
        if self.delete_protect is not None:
            result['deleteProtect'] = self.delete_protect
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.create_time is not None:
            result['createTime'] = self.create_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Vpn

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('vpnName') is not None:
            self.vpn_name = m.get('vpnName')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('maxConnection') is not None:
            self.max_connection = m.get('maxConnection')
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vpnConnNum') is not None:
            self.vpn_conn_num = m.get('vpnConnNum')
        if m.get('vpnConns') is not None:
            self.vpn_conns = [VpnConn().from_dict(i) for i in m.get('vpnConns')]
        if m.get('sslVpnServer') is not None:
            self.ssl_vpn_server = SslVpnServer().from_dict(m.get('sslVpnServer'))
        if m.get('deleteProtect') is not None:
            self.delete_protect = m.get('deleteProtect')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        return self
