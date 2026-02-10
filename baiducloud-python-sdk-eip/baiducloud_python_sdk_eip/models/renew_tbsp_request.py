from baiducloud_python_sdk_core.abstract_model import AbstractModel

class RenewTbspRequest(AbstractModel):
    
    def __init__(self, id, renew_time, renew_time_unit, client_token=None):
        super().__init__()
        self.id = id
        self.client_token = client_token
        self.renew_time = renew_time
        self.renew_time_unit = renew_time_unit

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.renew_time is not None:
            result['renewTime'] = self.renew_time
        if self.renew_time_unit is not None:
            result['renewTimeUnit'] = self.renew_time_unit
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('renewTime') is not None:
            self.renew_time = m.get('renewTime')
        if m.get('renewTimeUnit') is not None:
            self.renew_time_unit = m.get('renewTimeUnit')
        return self