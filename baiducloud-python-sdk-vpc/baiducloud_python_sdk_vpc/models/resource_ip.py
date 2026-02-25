
from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ResourceIp(AbstractModel):
    """
    ResourceIp
    """
    def __init__(self, ip=None, resource_type=None):
        super().__init__()
        self.ip = ip
        self.resource_type = resource_type

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self
