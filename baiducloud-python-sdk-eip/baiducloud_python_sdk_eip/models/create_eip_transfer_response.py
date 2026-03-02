from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_eip.models.transfer_info import TransferInfo

class CreateEipTransferResponse(BceResponse):
    """
    CreateEipTransferResponse
    """
    def __init__(self, transfers=None):
        super().__init__()
        self.transfers = transfers

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.transfers is not None:
            result['transfers'] = [i.to_dict() for i in self.transfers]
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('transfers') is not None:
            self.transfers = [
            TransferInfo().from_dict(i)
            for i in m.get('transfers')
            ]
        return self