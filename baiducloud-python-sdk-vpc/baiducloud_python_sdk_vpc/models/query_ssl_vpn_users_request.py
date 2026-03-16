from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QuerySslVpnUsersRequest(AbstractModel):
    """
    查询SSL VPN用户请求类
    """
    
    def __init__(self, vpn_id, marker=None, max_keys=None, user_name=None):
        """
        初始化查询SSL VPN用户请求
        
        :param vpn_id: VPN实例ID
        :param marker: 分页标记
        :param max_keys: 每页返回的最大数量
        :param user_name: 用户名
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.marker = marker
        self.max_keys = max_keys
        self.user_name = user_name

    def to_dict(self):
        """
        将对象转换为字典
        
        :return: 包含对象属性的字典
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
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
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self