from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_vpc.models.ike_config import IkeConfig

from baiducloud_python_sdk_vpc.models.ipsec_config import IpsecConfig


class VpnConn(AbstractModel):
    """
    VpnConn model class
    """
    
    def __init__(self, vpn_id=None, vpn_conn_id=None, vpn_conn_name=None, local_ip=None, secret_key=None, 
                 local_subnets=None, remote_ip=None, remote_subnets=None, cgw_id=None, description=None, 
                 status=None, created_time=None, health_status=None, ike_config=None, ipsec_config=None):
        """
        Initialize VpnConn instance
        
        Args:
            vpn_id (str): VPN ID
            vpn_conn_id (str): VPN connection ID
            vpn_conn_name (str): VPN connection name
            local_ip (str): Local IP address
            secret_key (str): Secret key
            local_subnets (list): Local subnets
            remote_ip (str): Remote IP address
            remote_subnets (list): Remote subnets
            cgw_id (str): Customer gateway ID
            description (str): Description
            status (str): Status
            created_time (str): Created time
            health_status (str): Health status
            ike_config (IkeConfig): IKE configuration
            ipsec_config (IpsecConfig): IPsec configuration
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
        Convert VpnConn instance to dictionary
        
        Returns:
            dict: Dictionary containing VpnConn attributes
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
        Initialize VpnConn instance from dictionary
        
        Args:
            m (dict): Dictionary containing VpnConn attributes
            
        Returns:
            VpnConn: Initialized VpnConn instance
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