from baiducloud_python_sdk_core.abstract_model import AbstractModel

class ModifyTbspIpProtectLevelRequest(AbstractModel):
    
    def __init__(self, id, client_token=None, ip=None, protect_level=None):
        super().__init__()
        self.id = id
        self.client_token = client_token
        self.ip = ip
        self.protect_level = protect_level

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.protect_level is not None:
            result['protectLevel'] = self.protect_level
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('protectLevel') is not None:
            self.protect_level = m.get('protectLevel')
        return self