from baiducloud_python_sdk_core.abstract_model import AbstractModel

class BandwidthPackageInquiryRequest(AbstractModel):
    
    def __init__(self, bandwidth_in_mbps, count=None, type=None):
        super().__init__()
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.count = count
        self.type = type

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.count is not None:
            result['count'] = self.count
        if self.type is not None:
            result['type'] = self.type
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self