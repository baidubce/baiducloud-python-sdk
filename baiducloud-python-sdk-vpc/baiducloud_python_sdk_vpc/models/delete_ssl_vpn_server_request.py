from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteSslVpnServerRequest(AbstractModel):
    """
    DeleteSslVpnServerRequest 类用于封装删除SSL VPN服务器的请求参数
    """
    
    def __init__(self, vpn_id, ssl_vpn_server_id, client_token=None):
        """
        初始化DeleteSslVpnServerRequest实例
        
        :param vpn_id: VPN实例ID
        :param ssl_vpn_server_id: SSL VPN服务器ID
        :param client_token: 客户端token，用于保证请求的幂等性
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.ssl_vpn_server_id = ssl_vpn_server_id
        self.client_token = client_token

    def to_dict(self):
        """
        将对象转换为字典格式
        
        :return: 包含对象属性的字典
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        return result


    def from_dict(self, m):
        """
        从字典格式初始化对象属性
        
        :param m: 包含对象属性的字典
        :return: 初始化后的对象本身
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('sslVpnServerId') is not None:
            self.ssl_vpn_server_id = m.get('sslVpnServerId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self