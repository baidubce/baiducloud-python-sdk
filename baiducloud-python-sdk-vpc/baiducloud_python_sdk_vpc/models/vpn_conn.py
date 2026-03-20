"""
VpnConn information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_vpc.models.ike_config import IkeConfig

from baiducloud_python_sdk_vpc.models.ipsec_config import IpsecConfig


class VpnConn(AbstractModel):
    """
    VpnConn
    """

    def __init__(
        self,
        vpn_id=None,
        vpn_conn_id=None,
        vpn_conn_name=None,
        local_ip=None,
        secret_key=None,
        local_subnets=None,
        remote_ip=None,
        remote_subnets=None,
        cgw_id=None,
        description=None,
        status=None,
        created_time=None,
        health_status=None,
        ike_config=None,
        ipsec_config=None,
    ):
        """
        Initialize VpnConn instance.

        :param vpn_id: VPN的ID
        :type vpn_id: str (optional)

        :param vpn_conn_id: 隧道的ID
        :type vpn_conn_id: str (optional)

        :param vpn_conn_name: 隧道的名称
        :type vpn_conn_name: str (optional)

        :param local_ip: 本地IP
        :type local_ip: str (optional)

        :param secret_key: 共享秘钥
        :type secret_key: str (optional)

        :param local_subnets: 本端网络CIDR列表
        :type local_subnets: List[str] (optional)

        :param remote_ip: 对端VPN网关公网IP
        :type remote_ip: str (optional)

        :param remote_subnets: 对端网络CIDR列表
        :type remote_subnets: List[str] (optional)

        :param cgw_id: 用户网关ID
        :type cgw_id: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param status: VPN隧道的状态
        :type status: str (optional)

        :param created_time: 创建时间
        :type created_time: str (optional)

        :param health_status: 联通状态
        :type health_status: str (optional)

        :param ike_config: ike_config attribute
        :type ike_config: IkeConfig (optional)

        :param ipsec_config: ipsec_config attribute
        :type ipsec_config: IpsecConfig (optional)
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.vpn_conn_id = vpn_conn_id
        self.vpn_conn_name = vpn_conn_name
        self.local_ip = local_ip
        self.secret_key = secret_key
        self.local_subnets = local_subnets
        self.remote_ip = remote_ip
        self.remote_subnets = remote_subnets
        self.cgw_id = cgw_id
        self.description = description
        self.status = status
        self.created_time = created_time
        self.health_status = health_status
        self.ike_config = ike_config
        self.ipsec_config = ipsec_config

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
        if self.vpn_conn_id is not None:
            result['vpnConnId'] = self.vpn_conn_id
        if self.vpn_conn_name is not None:
            result['vpnConnName'] = self.vpn_conn_name
        if self.local_ip is not None:
            result['localIp'] = self.local_ip
        if self.secret_key is not None:
            result['secretKey'] = self.secret_key
        if self.local_subnets is not None:
            result['localSubnets'] = self.local_subnets
        if self.remote_ip is not None:
            result['remoteIp'] = self.remote_ip
        if self.remote_subnets is not None:
            result['remoteSubnets'] = self.remote_subnets
        if self.cgw_id is not None:
            result['cgwId'] = self.cgw_id
        if self.description is not None:
            result['description'] = self.description
        if self.status is not None:
            result['status'] = self.status
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.health_status is not None:
            result['healthStatus'] = self.health_status
        if self.ike_config is not None:
            result['ikeConfig'] = self.ike_config.to_dict()
        if self.ipsec_config is not None:
            result['ipsecConfig'] = self.ipsec_config.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VpnConn

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('vpnConnId') is not None:
            self.vpn_conn_id = m.get('vpnConnId')
        if m.get('vpnConnName') is not None:
            self.vpn_conn_name = m.get('vpnConnName')
        if m.get('localIp') is not None:
            self.local_ip = m.get('localIp')
        if m.get('secretKey') is not None:
            self.secret_key = m.get('secretKey')
        if m.get('localSubnets') is not None:
            self.local_subnets = m.get('localSubnets')
        if m.get('remoteIp') is not None:
            self.remote_ip = m.get('remoteIp')
        if m.get('remoteSubnets') is not None:
            self.remote_subnets = m.get('remoteSubnets')
        if m.get('cgwId') is not None:
            self.cgw_id = m.get('cgwId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('healthStatus') is not None:
            self.health_status = m.get('healthStatus')
        if m.get('ikeConfig') is not None:
            self.ike_config = IkeConfig().from_dict(m.get('ikeConfig'))
        if m.get('ipsecConfig') is not None:
            self.ipsec_config = IpsecConfig().from_dict(m.get('ipsecConfig'))
        return self
