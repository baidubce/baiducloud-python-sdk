from baiducloud_python_sdk_core.abstract_model import AbstractModel

class BindTbspProtectionObjectRequest(AbstractModel):
    
    def __init__(self, id, ip_list, client_token=None):
        super().__init__()
        self.id = id
        self.client_token = client_token
        self.ip_list = ip_list

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.ip_list is not None:
            result['ipList'] = self.ip_list
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ipList') is not None:
            self.ip_list = m.get('ipList')
        return self