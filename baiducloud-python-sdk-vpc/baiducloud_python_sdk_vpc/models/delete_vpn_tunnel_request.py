from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteVpnTunnelRequest(AbstractModel):
    """
    删除VPN隧道请求类
    用于封装删除VPN隧道所需的参数
    """
    
    def __init__(self, vpn_conn_id, client_token=None):
        """
        初始化删除VPN隧道请求
        
        :param vpn_conn_id: VPN连接ID
        :param client_token: 客户端令牌，用于保证请求的幂等性
        """
        super().__init__()
        self.vpn_conn_id = vpn_conn_id
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
        从字典格式初始化对象
        
        :param m: 包含对象属性的字典
        :return: 初始化后的对象本身
        """
        m = m or dict()
        if m.get('vpnConnId') is not None:
            self.vpn_conn_id = m.get('vpnConnId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self