from baiducloud_python_sdk_core.abstract_model import AbstractModel

class AddTbspAreaBlockingRequest(AbstractModel):
    
    def __init__(self, id, client_token=None, ip=None, block_time=None, block_type=None):
        super().__init__()
        self.id = id
        self.client_token = client_token
        self.ip = ip
        self.block_time = block_time
        self.block_type = block_type

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.block_time is not None:
            result['blockTime'] = self.block_time
        if self.block_type is not None:
            result['blockType'] = self.block_type
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('blockTime') is not None:
            self.block_time = m.get('blockTime')
        if m.get('blockType') is not None:
            self.block_type = m.get('blockType')
        return self