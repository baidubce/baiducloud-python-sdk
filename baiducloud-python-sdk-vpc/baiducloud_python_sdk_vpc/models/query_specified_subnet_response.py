from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.subnet_detail import SubnetDetail

class QuerySpecifiedSubnetResponse(BceResponse):
    """
    QuerySpecifiedSubnetResponse
    """
    def __init__(self, subnet=None):
        super().__init__()
        self.subnet = subnet

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.subnet is not None:
            result['subnet'] = self.subnet.to_dict()
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('subnet') is not None:
            self.subnet = SubnetDetail().from_dict(m.get('subnet'))
        return self