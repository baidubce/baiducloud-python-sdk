from baiducloud_python_sdk_core.abstract_model import AbstractModel

class ListTbspIpWhitelistRequest(AbstractModel):
    
    def __init__(self, id, ip=None, ip_cidr=None, marker=None, max_keys=None):
        super().__init__()
        self.id = id
        self.ip = ip
        self.ip_cidr = ip_cidr
        self.marker = marker
        self.max_keys = max_keys

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
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('ipCidr') is not None:
            self.ip_cidr = m.get('ipCidr')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        return self