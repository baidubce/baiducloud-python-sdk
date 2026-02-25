
from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_vpc.models.tag_model import TagModel


class Vpc(AbstractModel):
    """
    Vpc
    """
    def __init__(self, vpc_id=None, name=None, cidr=None, ipv6_cidr=None, description=None, is_default=None, relay=None, secondary_cidr=None, tags=None):
        super().__init__()
        self.vpc_id = vpc_id
        self.name = name
        self.cidr = cidr
        self.ipv6_cidr = ipv6_cidr
        self.description = description
        self.is_default = is_default
        self.relay = relay
        self.secondary_cidr = secondary_cidr
        self.tags = tags

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.name is not None:
            result['name'] = self.name
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.ipv6_cidr is not None:
            result['ipv6Cidr'] = self.ipv6_cidr
        if self.description is not None:
            result['description'] = self.description
        if self.is_default is not None:
            result['isDefault'] = self.is_default
        if self.relay is not None:
            result['relay'] = self.relay
        if self.secondary_cidr is not None:
            result['secondaryCidr'] = self.secondary_cidr
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('ipv6Cidr') is not None:
            self.ipv6_cidr = m.get('ipv6Cidr')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        if m.get('relay') is not None:
            self.relay = m.get('relay')
        if m.get('secondaryCidr') is not None:
            self.secondary_cidr = m.get('secondaryCidr')
        if m.get('tags') is not None:
            self.tags = [
            TagModel().from_dict(i)
            for i in m.get('tags')
            ]
        return self
