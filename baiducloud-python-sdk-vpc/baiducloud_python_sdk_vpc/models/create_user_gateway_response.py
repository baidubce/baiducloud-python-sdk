from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateUserGatewayResponse(BceResponse):
    """
    CreateUserGatewayResponse 类用于表示创建用户网关的响应

    Attributes:
        cgw_id (str): 用户网关ID
    """
    
    def __init__(self, cgw_id=None):
        """
        初始化CreateUserGatewayResponse实例

        Args:
            cgw_id (str, optional): 用户网关ID. Defaults to None.
        """
        super().__init__()
        self.cgw_id = cgw_id

    def to_dict(self):
        """
        将响应对象转换为字典格式

        Returns:
            dict: 包含响应数据的字典
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.cgw_id is not None:
            result['cgwId'] = self.cgw_id
        return result

    def from_dict(self, m):
        """
        从字典数据初始化响应对象

        Args:
            m (dict): 包含响应数据的字典

        Returns:
            CreateUserGatewayResponse: 初始化后的响应对象
        """
        m = m or dict()
        if m.get('cgwId') is not None:
            self.cgw_id = m.get('cgwId')
        return self