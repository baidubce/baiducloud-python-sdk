from baiducloud_python_sdk_core.bce_response import BceResponse

class SharedDataPackageInquiryResponse(BceResponse):
    """
    SharedDataPackageInquiryResponse
    """
    def __init__(self, price=None):
        super().__init__()
        self.price = price

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.price is not None:
            result['price'] = self.price
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('price') is not None:
            self.price = m.get('price')
        return self