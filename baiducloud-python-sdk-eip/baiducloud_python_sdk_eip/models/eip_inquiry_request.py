from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_eip.models.billing import Billing

class EipInquiryRequest(AbstractModel):
    
    def __init__(self, bandwidth_in_mbps, billing, count=None, purchase_type=None):
        super().__init__()
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.count = count
        self.purchase_type = purchase_type
        self.billing = billing

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.count is not None:
            result['count'] = self.count
        if self.purchase_type is not None:
            result['purchaseType'] = self.purchase_type
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('purchaseType') is not None:
            self.purchase_type = m.get('purchaseType')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        return self