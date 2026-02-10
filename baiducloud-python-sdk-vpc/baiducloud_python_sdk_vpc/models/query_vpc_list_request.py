from baiducloud_python_sdk_core.abstract_model import AbstractModel

class QueryVpcListRequest(AbstractModel):
    
    def __init__(self, marker=None, max_keys=None, is_default=None, vpc_ids=None):
        super().__init__()
        self.marker = marker
        self.max_keys = max_keys
        self.is_default = is_default
        self.vpc_ids = vpc_ids

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        if m.get('vpcIds') is not None:
            self.vpc_ids = m.get('vpcIds')
        return self