from baiducloud_python_sdk_core.abstract_model import AbstractModel

class QueryTheListOfEipsInTheRecyclingBinRequest(AbstractModel):
    
    def __init__(self, eip=None, name=None, marker=None, max_keys=None):
        super().__init__()
        self.eip = eip
        self.name = name
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
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        return self