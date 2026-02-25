from baiducloud_python_sdk_core.abstract_model import AbstractModel

class QuerySpecifiedSubnetRequest(AbstractModel):
    
    def __init__(self, subnet_id):
        super().__init__()
        self.subnet_id = subnet_id

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
        return self