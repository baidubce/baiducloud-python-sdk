from baiducloud_python_sdk_core.abstract_model import AbstractModel

class CreateIpReservedRequest(AbstractModel):
    
    def __init__(self, subnet_id, ip_cidr, ip_version, client_token=None, description=None):
        super().__init__()
        self.client_token = client_token
        self.subnet_id = subnet_id
        self.ip_cidr = ip_cidr
        self.ip_version = ip_version
        self.description = description

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.ip_cidr is not None:
            result['ipCidr'] = self.ip_cidr
        if self.ip_version is not None:
            result['ipVersion'] = self.ip_version
        if self.description is not None:
            result['description'] = self.description
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('ipCidr') is not None:
            self.ip_cidr = m.get('ipCidr')
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self