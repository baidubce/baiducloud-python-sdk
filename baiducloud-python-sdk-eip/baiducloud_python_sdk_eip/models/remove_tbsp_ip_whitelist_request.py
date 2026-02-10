from baiducloud_python_sdk_core.abstract_model import AbstractModel

class RemoveTbspIpWhitelistRequest(AbstractModel):
    
    def __init__(self, id, client_token=None, ip=None, whitelist_id=None):
        super().__init__()
        self.id = id
        self.client_token = client_token
        self.ip = ip
        self.whitelist_id = whitelist_id

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('whitelistId') is not None:
            self.whitelist_id = m.get('whitelistId')
        return self