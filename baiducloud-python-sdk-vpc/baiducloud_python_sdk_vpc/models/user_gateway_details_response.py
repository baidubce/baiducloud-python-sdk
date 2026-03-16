from baiducloud_python_sdk_core.bce_response import BceResponse


class UserGatewayDetailsResponse(BceResponse):
    """
    UserGatewayDetailsResponse类，用于表示用户网关详情响应

    Attributes:
        cgw_id (str): 网关ID
        name (str): 网关名称
        ip (str): 网关IP地址
        description (str): 网关描述信息
        created_time (str): 创建时间
        updated_time (str): 更新时间
    """
    
    def __init__(self, cgw_id=None, name=None, ip=None, description=None, created_time=None, updated_time=None):
        """
        初始化UserGatewayDetailsResponse实例

        Args:
            cgw_id (str, optional): 网关ID. Defaults to None.
            name (str, optional): 网关名称. Defaults to None.
            ip (str, optional): 网关IP地址. Defaults to None.
            description (str, optional): 网关描述信息. Defaults to None.
            created_time (str, optional): 创建时间. Defaults to None.
            updated_time (str, optional): 更新时间. Defaults to None.
        """
        super().__init__()
        self.cgw_id = cgw_id
        self.name = name
        self.ip = ip
        self.description = description
        self.created_time = created_time
        self.updated_time = updated_time

    def to_dict(self):
        """
        将UserGatewayDetailsResponse对象转换为字典

        Returns:
            dict: 包含对象属性的字典
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.cgw_id is not None:
            result['cgwId'] = self.cgw_id
        if self.name is not None:
            result['name'] = self.name
        if self.ip is not None:
            result['ip'] = self.ip
        if self.description is not None:
            result['description'] = self.description
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.updated_time is not None:
            result['updatedTime'] = self.updated_time
        return result

    def from_dict(self, m):
        """
        从字典初始化UserGatewayDetailsResponse对象

        Args:
            m (dict): 包含对象属性的字典

        Returns:
            UserGatewayDetailsResponse: 初始化后的对象
        """
        m = m or dict()
        if m.get('cgwId') is not None:
            self.cgw_id = m.get('cgwId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')
        return self