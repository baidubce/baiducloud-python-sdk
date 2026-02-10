from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_eip.models.tbsp_protocol_blocking_model import TbspProtocolBlockingModel

class ListTbspProtocolBlockingResponse(BceResponse):
    """
    ListTbspProtocolBlockingResponse
    """
    def __init__(self, protocol_blocking_list=None, id=None):
        super().__init__()
        self.protocol_blocking_list = protocol_blocking_list
        self.id = id

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.protocol_blocking_list is not None:
            result['protocolBlockingList'] = [i.to_dict() for i in self.protocol_blocking_list]
        if self.id is not None:
            result['id'] = self.id
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('protocolBlockingList') is not None:
            self.protocol_blocking_list = [
            TbspProtocolBlockingModel().from_dict(i)
            for i in m.get('protocolBlockingList')
            ]
        if m.get('id') is not None:
            self.id = m.get('id')
        return self