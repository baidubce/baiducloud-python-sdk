from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.tag_model import TagModel

class CreateSubnetRequest(AbstractModel):
    
    def __init__(self, name, zone_name, cidr, vpc_id, client_token=None, enable_ipv6=None, vpc_secondary_cidr=None, subnet_type=None, description=None, tags=None):
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.enable_ipv6 = enable_ipv6
        self.zone_name = zone_name
        self.cidr = cidr
        self.vpc_id = vpc_id
        self.vpc_secondary_cidr = vpc_secondary_cidr
        self.subnet_type = subnet_type
        self.description = description
        self.tags = tags

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.enable_ipv6 is not None:
            result['enableIpv6'] = self.enable_ipv6
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vpc_secondary_cidr is not None:
            result['vpcSecondaryCidr'] = self.vpc_secondary_cidr
        if self.subnet_type is not None:
            result['subnetType'] = self.subnet_type
        if self.description is not None:
            result['description'] = self.description
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('enableIpv6') is not None:
            self.enable_ipv6 = m.get('enableIpv6')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vpcSecondaryCidr') is not None:
            self.vpc_secondary_cidr = m.get('vpcSecondaryCidr')
        if m.get('subnetType') is not None:
            self.subnet_type = m.get('subnetType')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('tags') is not None:
            self.tags = [
            TagModel().from_dict(i)
            for i in m.get('tags')
            ]
        return self