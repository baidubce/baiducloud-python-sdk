
from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TbspAttackRecordModel(AbstractModel):
    """
    TbspAttackRecordModel
    """
    def __init__(self, ip=None, start_time=None):
        super().__init__()
        self.ip = ip
        self.start_time = start_time

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self
