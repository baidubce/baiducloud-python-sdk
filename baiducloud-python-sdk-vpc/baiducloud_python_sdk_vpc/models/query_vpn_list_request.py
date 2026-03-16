from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QueryVpnListRequest(AbstractModel):
    """
    查询VPN列表请求参数
    """
    
    def __init__(self, vpc_id, marker=None, max_keys=None, eip=None, type=None):
        """
        初始化查询VPN列表请求参数
        
        Args:
            vpc_id (str): VPC ID
            marker (str, optional): 查询起始位置. Defaults to None.
            max_keys (int, optional): 每次查询的最大数量. Defaults to None.
            eip (str, optional): 弹性IP. Defaults to None.
            type (str, optional): VPN类型. Defaults to None.
        """
        super().__init__()
        self.marker = marker
        self.max_keys = max_keys
        self.vpc_id = vpc_id
        self.eip = eip
        self.type = type

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
        return result


    def from_dict(self, m):
        """
        从字典初始化对象
        
        Args:
            m (dict): 包含对象属性的字典
            
        Returns:
            QueryVpnListRequest: 初始化后的对象
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self