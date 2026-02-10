from baiducloud_python_sdk_core.abstract_model import AbstractModel

class DeleteSubnetRequest(AbstractModel):
    
    def __init__(self, subnet_id, client_token=None):
        super().__init__()
        self.subnet_id = subnet_id
        self.client_token = client_token

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self