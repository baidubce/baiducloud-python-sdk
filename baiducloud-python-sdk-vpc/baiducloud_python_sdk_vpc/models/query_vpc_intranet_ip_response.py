from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.vpc_private_ip_address import VpcPrivateIpAddress

class QueryVpcIntranetIpResponse(BceResponse):
    """
    QueryVpcIntranetIpResponse
    """
    def __init__(self, vpc_private_ip_addresses=None):
        super().__init__()
        self.vpc_private_ip_addresses = vpc_private_ip_addresses

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.vpc_private_ip_addresses is not None:
            result['vpcPrivateIpAddresses'] = [i.to_dict() for i in self.vpc_private_ip_addresses]
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('vpcPrivateIpAddresses') is not None:
            self.vpc_private_ip_addresses = [
            VpcPrivateIpAddress().from_dict(i)
            for i in m.get('vpcPrivateIpAddresses')
            ]
        return self