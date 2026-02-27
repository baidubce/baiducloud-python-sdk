from baiducloud_python_sdk_core.abstract_model import AbstractModel

class UpdateEipDeleteProtectRequest(AbstractModel):
    
    def __init__(self, eip, delete_protect, client_token=None):
        super().__init__()
        self.eip = eip
        self.client_token = client_token
        self.delete_protect = delete_protect

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.delete_protect is not None:
            result['deleteProtect'] = self.delete_protect
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('deleteProtect') is not None:
            self.delete_protect = m.get('deleteProtect')
        return self