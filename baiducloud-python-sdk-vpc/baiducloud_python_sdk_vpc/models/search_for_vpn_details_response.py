"""
Request entity for SearchForVpnDetailsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.vpn_conn import VpnConn
from baiducloud_python_sdk_vpc.models.ssl_vpn_server import SslVpnServer
from baiducloud_python_sdk_vpc.models.tag_model import TagModel


class SearchForVpnDetailsResponse(BceResponse):
    """
    SearchForVpnDetailsResponse
    """

    def __init__(
        self,
        vpn_id=None,
        vpn_name=None,
        create_time=None,
        description=None,
        type=None,
        status=None,
        expired_time=None,
        payment_timing=None,
        eip=None,
        bandwidth_in_mbps=None,
        vpc_id=None,
        vpn_conn_num=None,
        max_connection=None,
        vpn_conns=None,
        ssl_vpn_server=None,
        tags=None,
        delete_protect=None,
    ):
        """
        Initialize SearchForVpnDetailsResponse response.

        :param vpn_id: VPN的ID
        :type vpn_id: str (optional)

        :param vpn_name: 名称
        :type vpn_name: str (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param type: VPN网关类型，值“IPSec”表示IPSec-VPN网关，值“SSL”表示SSL-VPN网关
        :type type: str (optional)

        :param status: vpn状态，active：可用，building：创建中，unconfigured：未配置
        :type status: str (optional)

        :param expired_time: 到期时间
        :type expired_time: str (optional)

        :param payment_timing: 计费类型
        :type payment_timing: str (optional)

        :param eip: 公网IP
        :type eip: str (optional)

        :param bandwidth_in_mbps: eip带宽
        :type bandwidth_in_mbps: int (optional)

        :param vpc_id: VPC的ID
        :type vpc_id: str (optional)

        :param vpn_conn_num: 隧道数量
        :type vpn_conn_num: int (optional)

        :param max_connection: SSL-VPN最大客户端连接数
        :type max_connection: int (optional)

        :param vpn_conns: VPN隧道列表
        :type vpn_conns: List[VpnConn] (optional)

        :param ssl_vpn_server: ssl_vpn_server field
        :type ssl_vpn_server: SslVpnServer (optional)

        :param tags: VPN实例绑定的标签
        :type tags: List[TagModel] (optional)

        :param delete_protect: 是否开启释放保护
        :type delete_protect: bool (optional)
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.vpn_name = vpn_name
        self.create_time = create_time
        self.description = description
        self.type = type
        self.status = status
        self.expired_time = expired_time
        self.payment_timing = payment_timing
        self.eip = eip
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.vpc_id = vpc_id
        self.vpn_conn_num = vpn_conn_num
        self.max_connection = max_connection
        self.vpn_conns = vpn_conns
        self.ssl_vpn_server = ssl_vpn_server
        self.tags = tags
        self.delete_protect = delete_protect

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
        if self.vpn_name is not None:
            result['vpnName'] = self.vpn_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.type is not None:
            result['type'] = self.type
        if self.status is not None:
            result['status'] = self.status
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.eip is not None:
            result['eip'] = self.eip
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vpn_conn_num is not None:
            result['vpnConnNum'] = self.vpn_conn_num
        if self.max_connection is not None:
            result['maxConnection'] = self.max_connection
        if self.vpn_conns is not None:
            result['vpnConns'] = [i.to_dict() for i in self.vpn_conns]
        if self.ssl_vpn_server is not None:
            result['sslVpnServer'] = self.ssl_vpn_server.to_dict()
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.delete_protect is not None:
            result['deleteProtect'] = self.delete_protect
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SearchForVpnDetailsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('vpnName') is not None:
            self.vpn_name = m.get('vpnName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vpnConnNum') is not None:
            self.vpn_conn_num = m.get('vpnConnNum')
        if m.get('maxConnection') is not None:
            self.max_connection = m.get('maxConnection')
        if m.get('vpnConns') is not None:
            self.vpn_conns = [VpnConn().from_dict(i) for i in m.get('vpnConns')]
        if m.get('sslVpnServer') is not None:
            self.ssl_vpn_server = SslVpnServer().from_dict(m.get('sslVpnServer'))
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('deleteProtect') is not None:
            self.delete_protect = m.get('deleteProtect')
        return self
