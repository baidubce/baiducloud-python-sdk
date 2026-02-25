
from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TbspIpModel(AbstractModel):
    """
    TbspIpModel
    """
    def __init__(self, ip=None, status=None):
        super().__init__()
        self.ip = ip
        self.status = status

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.status is not None:
            result['status'] = self.status
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
