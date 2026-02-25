from baiducloud_python_sdk_core.abstract_model import AbstractModel

class QueryTheIpAddressesOccupiedByProductsWithinVpcRequest(AbstractModel):
    
    def __init__(self, vpc_id, subnet_id=None, resource_type=None, page_no=None, page_size=None):
        super().__init__()
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.resource_type = resource_type
        self.page_no = page_no
        self.page_size = page_size

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
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self