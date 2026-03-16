from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateVpnResponse(BceResponse):
    """CreateVpnResponse类用于封装创建VPN连接的响应信息
    
    Attributes:
        vpn_id (str): VPN连接的ID
    """
    
    def __init__(self, vpn_id=None):
        """初始化CreateVpnResponse实例
        
        Args:
            vpn_id (str, optional): VPN连接的ID. 默认为None.
        """
        super().__init__()
        self.vpn_id = vpn_id

    def to_dict(self):
        """将响应对象转换为字典格式
        
        Returns:
            dict: 包含响应信息的字典
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.vpn_id is not None:
            result['vpnId'] = self.vpn_id
        return result


    def from_dict(self, m):
        """从字典格式初始化响应对象
        
        Args:
            m (dict): 包含响应信息的字典
            
        Returns:
            CreateVpnResponse: 初始化后的响应对象
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        return self