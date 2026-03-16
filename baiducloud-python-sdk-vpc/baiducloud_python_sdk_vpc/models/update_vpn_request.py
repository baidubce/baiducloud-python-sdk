from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateVpnRequest(AbstractModel):
    """
    更新VPN请求类
    """
    
    def __init__(self, vpn_id, client_token=None, vpn_name=None, description=None):
        """
        初始化UpdateVpnRequest实例
        
        :param vpn_id: VPN ID
        :param client_token: 客户端token
        :param vpn_name: VPN名称
        :param description: VPN描述
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.client_token = client_token
        self.vpn_name = vpn_name
        self.description = description

    def to_dict(self):
        """
        将对象转换为字典
        
        :return: 包含对象属性的字典
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.vpn_name is not None:
            result['vpnName'] = self.vpn_name
        if self.description is not None:
            result['description'] = self.description
        return result


    def from_dict(self, m):
        """
        从字典初始化对象
        
        :param m: 包含对象属性的字典
        :type m: dict
        :return: 初始化后的对象
        :rtype: UpdateVpnRequest
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('vpnName') is not None:
            self.vpn_name = m.get('vpnName')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self