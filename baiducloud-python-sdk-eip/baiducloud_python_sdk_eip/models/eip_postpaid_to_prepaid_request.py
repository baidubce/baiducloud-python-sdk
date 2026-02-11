from baiducloud_python_sdk_core.abstract_model import AbstractModel

class EipPostpaidToPrepaidRequest(AbstractModel):
    
    def __init__(self, eip, client_token, purchase_length, band_width):
        super().__init__()
        self.eip = eip
        self.client_token = client_token
        self.purchase_length = purchase_length
        self.band_width = band_width

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.purchase_length is not None:
            result['purchaseLength'] = self.purchase_length
        if self.band_width is not None:
            result['bandWidth'] = self.band_width
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('purchaseLength') is not None:
            self.purchase_length = m.get('purchaseLength')
        if m.get('bandWidth') is not None:
            self.band_width = m.get('bandWidth')
        return self