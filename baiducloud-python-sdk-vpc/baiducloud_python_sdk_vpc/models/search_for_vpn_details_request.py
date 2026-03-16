from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SearchForVpnDetailsRequest(AbstractModel):
    """
    SearchForVpnDetailsRequest 类用于封装搜索VPN详情的请求参数
    """
    
    def __init__(self, vpn_id):
        """
        初始化SearchForVpnDetailsRequest实例
        
        :param vpn_id: VPN实例ID
        :type vpn_id: str
        """
        super().__init__()
        self.vpn_id = vpn_id

    def to_dict(self):
        """
        将对象转换为字典格式
        
        :return: 包含对象属性的字典
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        return result


    def from_dict(self, m):
        """
        从字典数据初始化对象属性
        
        :param m: 包含对象属性的字典
        :type m: dict
        :return: 初始化后的对象
        :rtype: SearchForVpnDetailsRequest
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        return self