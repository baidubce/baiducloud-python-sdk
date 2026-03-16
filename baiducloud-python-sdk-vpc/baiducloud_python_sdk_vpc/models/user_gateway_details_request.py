from baiducloud_python_sdk_core.abstract_model import AbstractModel

class UserGatewayDetailsRequest(AbstractModel):
    
    def __init__(self, cgw_id):
        super().__init__()
        self.cgw_id = cgw_id

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('cgwId') is not None:
            self.cgw_id = m.get('cgwId')
        return self