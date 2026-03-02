
from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TransferInfo(AbstractModel):
    """
    TransferInfo
    """
    def __init__(self, transfer_id=None, instance_id=None):
        super().__init__()
        self.transfer_id = transfer_id
        self.instance_id = instance_id

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.transfer_id is not None:
            result['transferId'] = self.transfer_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('transferId') is not None:
            self.transfer_id = m.get('transferId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self
