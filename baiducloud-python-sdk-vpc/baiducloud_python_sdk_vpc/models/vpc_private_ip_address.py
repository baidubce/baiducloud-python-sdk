
from baiducloud_python_sdk_core.abstract_model import AbstractModel


class VpcPrivateIpAddress(AbstractModel):
    """
    VpcPrivateIpAddress
    """
    def __init__(self, cidr=None, private_ip_address=None, private_ip_address_type=None, created_time=None):
        super().__init__()
        self.cidr = cidr
        self.private_ip_address = private_ip_address
        self.private_ip_address_type = private_ip_address_type
        self.created_time = created_time

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.private_ip_address is not None:
            result['privateIpAddress'] = self.private_ip_address
        if self.private_ip_address_type is not None:
            result['privateIpAddressType'] = self.private_ip_address_type
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('privateIpAddress') is not None:
            self.private_ip_address = m.get('privateIpAddress')
        if m.get('privateIpAddressType') is not None:
            self.private_ip_address_type = m.get('privateIpAddressType')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        return self
