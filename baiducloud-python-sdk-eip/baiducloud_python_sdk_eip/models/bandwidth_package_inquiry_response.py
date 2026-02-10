from baiducloud_python_sdk_core.bce_response import BceResponse

class BandwidthPackageInquiryResponse(BceResponse):
    """
    BandwidthPackageInquiryResponse
    """
    def __init__(self, prices=None):
        super().__init__()
        self.prices = prices

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.prices is not None:
            result['prices'] = self.prices
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('prices') is not None:
            self.prices = m.get('prices')
        return self