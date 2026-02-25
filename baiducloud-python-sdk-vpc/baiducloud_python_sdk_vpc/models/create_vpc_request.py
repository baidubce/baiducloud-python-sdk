from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.tag_model import TagModel

class CreateVpcRequest(AbstractModel):
    
    def __init__(self, name, cidr, client_token=None, description=None, enable_ipv6=None, tags=None):
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.description = description
        self.cidr = cidr
        self.enable_ipv6 = enable_ipv6
        self.tags = tags

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.enable_ipv6 is not None:
            result['enableIpv6'] = self.enable_ipv6
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('enableIpv6') is not None:
            self.enable_ipv6 = m.get('enableIpv6')
        if m.get('tags') is not None:
            self.tags = [
            TagModel().from_dict(i)
            for i in m.get('tags')
            ]
        return self