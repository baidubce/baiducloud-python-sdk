from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BindEipRequest(AbstractModel):
    """
    绑定EIP请求类
    """
    
    def __init__(self, vpn_id, eip, client_token=None):
        """
        初始化BindEipRequest实例
        
        :param vpn_id: VPN ID
        :param eip: 弹性IP地址
        :param client_token: 客户端令牌，可选
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.client_token = client_token
        self.eip = eip

    def to_dict(self):
        """
        将对象转换为字典
        
        :return: 包含对象属性的字典
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.eip is not None:
            result['eip'] = self.eip
        return result


    def from_dict(self, m):
        """
        从字典初始化对象
        
        :param m: 包含对象属性的字典
        :return: 初始化后的对象
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        return self