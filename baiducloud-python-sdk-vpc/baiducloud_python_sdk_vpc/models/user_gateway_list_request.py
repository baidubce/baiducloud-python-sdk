from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UserGatewayListRequest(AbstractModel):
    """
    用户网关列表请求类
    """
    
    def __init__(self, marker=None, max_keys=None):
        """
        初始化UserGatewayListRequest实例
        
        :param marker: 标记位置，用于分页查询
        :param max_keys: 每次返回的最大数量，用于分页查询
        """
        super().__init__()
        self.marker = marker
        self.max_keys = max_keys

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
        从字典初始化对象属性
        
        :param m: 包含对象属性的字典
        :type m: dict
        :return: 初始化后的对象本身
        :rtype: UserGatewayListRequest
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        return self