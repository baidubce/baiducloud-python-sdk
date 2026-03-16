from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.ssl_vpn_user import SslVpnUser


class BatchCreateSslVpnUsersRequest(AbstractModel):
    """
    批量创建SSL VPN用户请求类

    Attributes:
        vpn_id (str): VPN实例ID
        ssl_vpn_users (list[SslVpnUser]): SSL VPN用户列表
        client_token (str): 客户端token，用于保证请求的幂等性
    """
    
    def __init__(self, vpn_id, ssl_vpn_users, client_token=None):
        """
        初始化批量创建SSL VPN用户请求

        Args:
            vpn_id (str): VPN实例ID
            ssl_vpn_users (list[SslVpnUser]): SSL VPN用户列表
            client_token (str, optional): 客户端token，用于保证请求的幂等性
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.client_token = client_token
        self.ssl_vpn_users = ssl_vpn_users

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
        if self.ssl_vpn_users is not None:
            result['sslVpnUsers'] = [i.to_dict() for i in self.ssl_vpn_users]
        return result


    def from_dict(self, m):
        """
        从字典格式初始化对象

        Args:
            m (dict): 包含对象属性的字典

        Returns:
            BatchCreateSslVpnUsersRequest: 初始化后的对象
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('sslVpnUsers') is not None:
            self.ssl_vpn_users = [
            SslVpnUser().from_dict(i)
            for i in m.get('sslVpnUsers')
            ]
        return self