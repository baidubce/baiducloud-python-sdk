from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateUserGatewayRequest(AbstractModel):
    """
    创建用户网关请求类
    """
    
    def __init__(self, name, ip, client_token=None, description=None):
        """
        初始化创建用户网关请求
        
        Args:
            name (str): 网关名称
            ip (str): 网关IP地址
            client_token (str, optional): 客户端令牌，用于幂等性控制
            description (str, optional): 网关描述信息
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.ip = ip
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
        if self.name is not None:
            result['name'] = self.name
        if self.ip is not None:
            result['ip'] = self.ip
        if self.description is not None:
            result['description'] = self.description
        return result


    def from_dict(self, m):
        """
        从字典初始化对象
        
        Args:
            m (dict): 包含对象属性的字典
            
        Returns:
            CreateUserGatewayRequest: 初始化后的对象
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self