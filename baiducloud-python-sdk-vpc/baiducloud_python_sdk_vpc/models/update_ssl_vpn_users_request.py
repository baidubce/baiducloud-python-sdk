from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateSslVpnUsersRequest(AbstractModel):
    """
    更新SSL VPN用户请求类
    """
    
    def __init__(self, vpn_id, user_id, client_token=None, client_name=None, password=None, description=None):
        """
        初始化UpdateSslVpnUsersRequest实例
        
        Args:
            vpn_id (str): VPN实例ID
            user_id (str): 用户ID
            client_token (str, optional): 客户端token
            client_name (str, optional): 客户端名称
            password (str, optional): 密码
            description (str, optional): 描述信息
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.user_id = user_id
        self.client_token = client_token
        self.client_name = client_name
        self.password = password
        self.description = description

    def to_dict(self):
        """
        将对象转换为字典
        
        Returns:
            dict: 包含对象属性的字典
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.client_name is not None:
            result['clientName'] = self.client_name
        if self.password is not None:
            result['password'] = self.password
        if self.description is not None:
            result['description'] = self.description
        return result


    def from_dict(self, m):
        """
        从字典初始化对象
        
        Args:
            m (dict): 包含对象属性的字典
            
        Returns:
            UpdateSslVpnUsersRequest: 初始化后的对象
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('clientName') is not None:
            self.client_name = m.get('clientName')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self