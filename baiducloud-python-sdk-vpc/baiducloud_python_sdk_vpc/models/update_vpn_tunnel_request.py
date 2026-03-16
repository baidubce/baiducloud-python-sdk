from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.ike_config import IkeConfig
from baiducloud_python_sdk_vpc.models.ipsec_config import IpsecConfig


class UpdateVpnTunnelRequest(AbstractModel):
    """
    UpdateVpnTunnelRequest类用于封装更新VPN隧道的请求参数
    """
    
    def __init__(self, vpn_conn_id, vpn_id, secret_key, local_subnets, cgw_id, remote_subnets, vpn_conn_name, ike_config, ipsec_config, client_token=None, description=None):
        """
        初始化UpdateVpnTunnelRequest实例
        
        Args:
            vpn_conn_id: VPN连接ID
            vpn_id: VPN实例ID
            secret_key: 预共享密钥
            local_subnets: 本地子网列表
            cgw_id: 客户网关ID
            remote_subnets: 远程子网列表
            vpn_conn_name: VPN连接名称
            ike_config: IKE配置
            ipsec_config: IPSEC配置
            client_token: 客户端令牌
            description: 描述信息
        """
        super().__init__()
        self.vpn_conn_id = vpn_conn_id
        self.client_token = client_token
        self.vpn_id = vpn_id
        self.secret_key = secret_key
        self.local_subnets = local_subnets
        self.cgw_id = cgw_id
        self.remote_subnets = remote_subnets
        self.description = description
        self.vpn_conn_name = vpn_conn_name
        self.ike_config = ike_config
        self.ipsec_config = ipsec_config

    def to_dict(self):
        """
        将对象转换为字典格式
        
        Returns:
            dict: 包含对象属性的字典
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.vpn_id is not None:
            result['vpnId'] = self.vpn_id
        if self.secret_key is not None:
            result['secretKey'] = self.secret_key
        if self.local_subnets is not None:
            result['localSubnets'] = self.local_subnets
        if self.cgw_id is not None:
            result['cgwId'] = self.cgw_id
        if self.remote_subnets is not None:
            result['remoteSubnets'] = self.remote_subnets
        if self.description is not None:
            result['description'] = self.description
        if self.vpn_conn_name is not None:
            result['vpnConnName'] = self.vpn_conn_name
        if self.ike_config is not None:
            result['ikeConfig'] = self.ike_config.to_dict()
        if self.ipsec_config is not None:
            result['ipsecConfig'] = self.ipsec_config.to_dict()
        return result


    def from_dict(self, m):
        """
        从字典初始化对象
        
        Args:
            m (dict): 包含对象属性的字典
            
        Returns:
            UpdateVpnTunnelRequest: 初始化后的对象
        """
        m = m or dict()
        if m.get('vpnConnId') is not None:
            self.vpn_conn_id = m.get('vpnConnId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('secretKey') is not None:
            self.secret_key = m.get('secretKey')
        if m.get('localSubnets') is not None:
            self.local_subnets = m.get('localSubnets')
        if m.get('cgwId') is not None:
            self.cgw_id = m.get('cgwId')
        if m.get('remoteSubnets') is not None:
            self.remote_subnets = m.get('remoteSubnets')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('vpnConnName') is not None:
            self.vpn_conn_name = m.get('vpnConnName')
        if m.get('ikeConfig') is not None:
            self.ike_config = IkeConfig().from_dict(m.get('ikeConfig'))
        if m.get('ipsecConfig') is not None:
            self.ipsec_config = IpsecConfig().from_dict(m.get('ipsecConfig'))
        return self