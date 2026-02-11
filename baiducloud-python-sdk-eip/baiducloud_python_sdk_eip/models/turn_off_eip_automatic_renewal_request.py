from baiducloud_python_sdk_core.abstract_model import AbstractModel

class TurnOffEipAutomaticRenewalRequest(AbstractModel):
    
    def __init__(self, eip, client_token):
        super().__init__()
        self.eip = eip
        self.client_token = client_token

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self