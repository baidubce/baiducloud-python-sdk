
from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_eip.models.tbsp_protocol_port_model import TbspProtocolPortModel


class TbspProtocolBlockingModel(AbstractModel):
    """
    TbspProtocolBlockingModel
    """
    def __init__(self, ip=None, protocol_port_list=None):
        super().__init__()
        self.ip = ip
        self.protocol_port_list = protocol_port_list

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.protocol_port_list is not None:
            result['protocolPortList'] = [i.to_dict() for i in self.protocol_port_list]
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('protocolPortList') is not None:
            self.protocol_port_list = [
            TbspProtocolPortModel().from_dict(i)
            for i in m.get('protocolPortList')
            ]
        return self
