
from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TbspProtocolPortModel(AbstractModel):
    """
    TbspProtocolPortModel
    """
    def __init__(self, type=None, port_begin=None, port_end=None):
        super().__init__()
        self.type = type
        self.port_begin = port_begin
        self.port_end = port_end

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.port_begin is not None:
            result['portBegin'] = self.port_begin
        if self.port_end is not None:
            result['portEnd'] = self.port_end
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('portBegin') is not None:
            self.port_begin = m.get('portBegin')
        if m.get('portEnd') is not None:
            self.port_end = m.get('portEnd')
        return self
