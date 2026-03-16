from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateVpnReleaseProtectionRequest(AbstractModel):
    """
    更新VPN释放保护请求类

    Attributes:
        vpn_id (str): VPN实例ID
        client_token (str): 幂等性令牌
        delete_protect (bool): 是否开启删除保护
    """
    
    def __init__(self, vpn_id, client_token=None, delete_protect=None):
        """
        初始化更新VPN释放保护请求

        Args:
            vpn_id (str): VPN实例ID
            client_token (str, optional): 幂等性令牌. Defaults to None.
            delete_protect (bool, optional): 是否开启删除保护. Defaults to None.
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.client_token = client_token
        self.delete_protect = delete_protect

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
        if self.delete_protect is not None:
            result['deleteProtect'] = self.delete_protect
        return result


    def from_dict(self, m):
        """
        从字典初始化对象

        Args:
            m (dict): 包含对象属性的字典

        Returns:
            UpdateVpnReleaseProtectionRequest: 初始化后的对象
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('deleteProtect') is not None:
            self.delete_protect = m.get('deleteProtect')
        return self