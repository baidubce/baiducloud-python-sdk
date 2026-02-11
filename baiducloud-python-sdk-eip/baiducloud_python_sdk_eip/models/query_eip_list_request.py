from baiducloud_python_sdk_core.abstract_model import AbstractModel

class QueryEipListRequest(AbstractModel):
    
    def __init__(self, ip_version=None, eip=None, instance_type=None, instance_id=None, name=None, status=None, eip_ids=None, marker=None, max_keys=None):
        super().__init__()
        self.ip_version = ip_version
        self.eip = eip
        self.instance_type = instance_type
        self.instance_id = instance_id
        self.name = name
        self.status = status
        self.eip_ids = eip_ids
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
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('eipIds') is not None:
            self.eip_ids = m.get('eipIds')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        return self