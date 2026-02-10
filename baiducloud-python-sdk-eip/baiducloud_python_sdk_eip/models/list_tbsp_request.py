from baiducloud_python_sdk_core.abstract_model import AbstractModel

class ListTbspRequest(AbstractModel):
    
    def __init__(self, id=None, name=None, status=None, marker=None, max_keys=None):
        super().__init__()
        self.id = id
        self.name = name
        self.status = status
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
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        return self