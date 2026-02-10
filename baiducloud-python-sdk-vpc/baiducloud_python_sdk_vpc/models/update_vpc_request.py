from baiducloud_python_sdk_core.abstract_model import AbstractModel

class UpdateVpcRequest(AbstractModel):
    
    def __init__(self, vpc_id, name, client_token=None, description=None, enable_ipv6=None, secondary_cidr=None):
        super().__init__()
        self.vpc_id = vpc_id
        self.client_token = client_token
        self.name = name
        self.description = description
        self.enable_ipv6 = enable_ipv6
        self.secondary_cidr = secondary_cidr

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
        if self.secondary_cidr is not None:
            result['secondaryCidr'] = self.secondary_cidr
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enableIpv6') is not None:
            self.enable_ipv6 = m.get('enableIpv6')
        if m.get('secondaryCidr') is not None:
            self.secondary_cidr = m.get('secondaryCidr')
        return self