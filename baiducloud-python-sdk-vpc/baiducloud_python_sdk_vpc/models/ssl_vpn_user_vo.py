from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SslVpnUserVo(AbstractModel):
    """
    SslVpnUserVo 类表示SSL VPN用户信息
    
    Attributes:
        client_name (str): 客户端名称
        user_name (str): 用户名
        user_id (str): 用户ID
        description (str): 描述信息
    """
    
    def __init__(self, client_name=None, user_name=None, user_id=None, description=None):
        """
        初始化SslVpnUserVo实例
        
        Args:
            client_name (str, optional): 客户端名称. Defaults to None.
            user_name (str, optional): 用户名. Defaults to None.
            user_id (str, optional): 用户ID. Defaults to None.
            description (str, optional): 描述信息. Defaults to None.
        """
        super().__init__()
        self.client_name = client_name
        self.user_name = user_name
        self.user_id = user_id
        self.description = description

    def to_dict(self):
        """
        将对象转换为字典格式
        
        Returns:
            dict: 包含对象属性的字典
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.client_name is not None:
            result['clientName'] = self.client_name
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.description is not None:
            result['description'] = self.description
        return result


    def from_dict(self, m):
        """
        从字典初始化对象
        
        Args:
            m (dict): 包含对象属性的字典
            
        Returns:
            SslVpnUserVo: 当前对象
        """
        m = m or dict()
        if m.get('clientName') is not None:
            self.client_name = m.get('clientName')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self