from baiducloud_python_sdk_core.abstract_model import AbstractModel

class ResizeTbspRequest(AbstractModel):
    
    def __init__(self, id, ip_capacity, client_token=None):
        super().__init__()
        self.id = id
        self.client_token = client_token
        self.ip_capacity = ip_capacity

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.ip_capacity is not None:
            result['ipCapacity'] = self.ip_capacity
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ipCapacity') is not None:
            self.ip_capacity = m.get('ipCapacity')
        return self