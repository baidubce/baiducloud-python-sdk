from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateVpnTunnelResponse(BceResponse):
    """
    CreateVpnTunnelResponse 用于表示创建VPN隧道的响应

    Attributes:
        vpn_conn_id (str): VPN连接ID
    """
    
    def __init__(self, vpn_conn_id=None):
        """
        初始化CreateVpnTunnelResponse实例

        Args:
            vpn_conn_id (str, optional): VPN连接ID. 默认为None.
        """
        super().__init__()
        self.vpn_conn_id = vpn_conn_id

    def to_dict(self):
        """
        将响应对象转换为字典

        Returns:
            dict: 包含响应数据的字典
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.vpn_conn_id is not None:
            result['vpnConnId'] = self.vpn_conn_id
        return result


    def from_dict(self, m):
        """
        从字典数据初始化响应对象

        Args:
            m (dict): 包含响应数据的字典

        Returns:
            CreateVpnTunnelResponse: 初始化后的响应对象
        """
        m = m or dict()
        if m.get('vpnConnId') is not None:
            self.vpn_conn_id = m.get('vpnConnId')
        return self