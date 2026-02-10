from baiducloud_python_sdk_core.abstract_model import AbstractModel

class UpdateSubnetRequest(AbstractModel):
    
    def __init__(self, subnet_id, name, client_token=None, description=None, enable_ipv6=None):
        super().__init__()
        self.subnet_id = subnet_id
        self.client_token = client_token
        self.name = name
        self.description = description
        self.enable_ipv6 = enable_ipv6

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.enable_ipv6 is not None:
            result['enableIpv6'] = self.enable_ipv6
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enableIpv6') is not None:
            self.enable_ipv6 = m.get('enableIpv6')
        return self