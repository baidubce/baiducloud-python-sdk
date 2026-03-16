from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.billing import Billing


class RenewVpnRequest(AbstractModel):
    """
    RenewVpnRequest 类用于表示续订VPN连接的请求

    Attributes:
        vpn_id (str): VPN连接的ID
        client_token (str): 客户端令牌，用于保证请求的幂等性
        billing (Billing): 计费信息对象
    """
    
    def __init__(self, vpn_id, billing, client_token=None):
        """
        初始化RenewVpnRequest实例

        Args:
            vpn_id (str): VPN连接的ID
            billing (Billing): 计费信息对象
            client_token (str, optional): 客户端令牌. 默认为None.
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.client_token = client_token
        self.billing = billing

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
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        return result


    def from_dict(self, m):
        """
        从字典初始化对象

        Args:
            m (dict): 包含对象属性的字典

        Returns:
            RenewVpnRequest: 初始化后的对象
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        return self