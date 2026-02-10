from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.resource_ip import ResourceIp

class QueryTheIpAddressesOccupiedByProductsWithinVpcResponse(BceResponse):
    """
    QueryTheIpAddressesOccupiedByProductsWithinVpcResponse
    """
    def __init__(self, page_no=None, page_size=None, total_count=None, result=None):
        super().__init__()
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count
        self.result = result

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.result is not None:
            result['result'] = [i.to_dict() for i in self.result]
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('result') is not None:
            self.result = [
            ResourceIp().from_dict(i)
            for i in m.get('result')
            ]
        return self