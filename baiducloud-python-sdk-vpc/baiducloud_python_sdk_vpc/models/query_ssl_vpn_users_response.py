from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.ssl_vpn_user_vo import SslVpnUserVo


class QuerySslVpnUsersResponse(BceResponse):
    """
    QuerySslVpnUsersResponse 表示查询SSL VPN用户响应类

    属性:
        marker (str): 标记，用于分页查询
        is_truncated (bool): 指示结果是否被截断
        next_marker (str): 下一页标记
        max_keys (int): 每页最大记录数
        ssl_vpn_users (list[SslVpnUserVo]): SSL VPN用户列表
    """

    def __init__(self, marker=None, is_truncated=None, next_marker=None, max_keys=None, ssl_vpn_users=None):
        super().__init__()
        self.marker = marker
        self.is_truncated = is_truncated
        self.next_marker = next_marker
        self.max_keys = max_keys
        self.ssl_vpn_users = ssl_vpn_users

    def to_dict(self):
        """将对象转换为字典格式

        返回:
            dict: 包含对象属性的字典
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.marker is not None:
            result['marker'] = self.marker
        if self.is_truncated is not None:
            result['isTruncated'] = self.is_truncated
        if self.next_marker is not None:
            result['nextMarker'] = self.next_marker
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        if self.ssl_vpn_users is not None:
            result['sslVpnUsers'] = [i.to_dict() for i in self.ssl_vpn_users]
        return result


    def from_dict(self, m):
        """从字典格式初始化对象

        参数:
            m (dict): 包含对象属性的字典

        返回:
            QuerySslVpnUsersResponse: 初始化后的对象
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('isTruncated') is not None:
            self.is_truncated = m.get('isTruncated')
        if m.get('nextMarker') is not None:
            self.next_marker = m.get('nextMarker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('sslVpnUsers') is not None:
            self.ssl_vpn_users = [
                SslVpnUserVo().from_dict(i)
                for i in m.get('sslVpnUsers')
            ]
        return self