from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_eip.models.billing import Billing

class EipRenewalRequest(AbstractModel):
    
    def __init__(self, eip, client_token, billing):
        super().__init__()
        self.eip = eip
        self.client_token = client_token
        self.billing = billing

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        return self