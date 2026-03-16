from baiducloud_python_sdk_core.abstract_model import AbstractModel

class DeleteSslVpnUserRequest(AbstractModel):
    
    def __init__(self, vpn_id, user_id, client_token=None):
        super().__init__()
        self.vpn_id = vpn_id
        self.user_id = user_id
        self.client_token = client_token

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self