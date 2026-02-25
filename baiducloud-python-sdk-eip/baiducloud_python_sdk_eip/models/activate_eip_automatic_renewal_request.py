from baiducloud_python_sdk_core.abstract_model import AbstractModel

class ActivateEipAutomaticRenewalRequest(AbstractModel):
    
    def __init__(self, eip, client_token, auto_renew_time_unit=None, auto_renew_time=None):
        super().__init__()
        self.eip = eip
        self.client_token = client_token
        self.auto_renew_time_unit = auto_renew_time_unit
        self.auto_renew_time = auto_renew_time

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.auto_renew_time_unit is not None:
            result['autoRenewTimeUnit'] = self.auto_renew_time_unit
        if self.auto_renew_time is not None:
            result['autoRenewTime'] = self.auto_renew_time
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('autoRenewTimeUnit') is not None:
            self.auto_renew_time_unit = m.get('autoRenewTimeUnit')
        if m.get('autoRenewTime') is not None:
            self.auto_renew_time = m.get('autoRenewTime')
        return self