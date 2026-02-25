from baiducloud_python_sdk_core.abstract_model import AbstractModel

class DisableTbspIpCleanRequest(AbstractModel):
    
    def __init__(self, id, client_token=None, ip=None, turn_off_duration=None):
        super().__init__()
        self.id = id
        self.client_token = client_token
        self.ip = ip
        self.turn_off_duration = turn_off_duration

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.turn_off_duration is not None:
            result['turnOffDuration'] = self.turn_off_duration
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('turnOffDuration') is not None:
            self.turn_off_duration = m.get('turnOffDuration')
        return self