from baiducloud_python_sdk_core.abstract_model import AbstractModel

class QueryVpcIntranetIpRequest(AbstractModel):
    
    def __init__(self, vpc_id, private_ip_addresses=None, private_ip_range=None):
        super().__init__()
        self.vpc_id = vpc_id
        self.private_ip_addresses = private_ip_addresses
        self.private_ip_range = private_ip_range

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('privateIpAddresses') is not None:
            self.private_ip_addresses = m.get('privateIpAddresses')
        if m.get('privateIpRange') is not None:
            self.private_ip_range = m.get('privateIpRange')
        return self