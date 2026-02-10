from baiducloud_python_sdk_core.abstract_model import AbstractModel

class RemoveTbspAreaBlockingRequest(AbstractModel):
    
    def __init__(self, id, ip=None, block_type=None, client_token=None):
        super().__init__()
        self.id = id
        self.ip = ip
        self.block_type = block_type
        self.client_token = client_token

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
        if m.get('blockType') is not None:
            self.block_type = m.get('blockType')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self