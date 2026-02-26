from baiducloud_python_sdk_core.abstract_model import AbstractModel

class CancelEipTransferRequest(AbstractModel):
    
    def __init__(self, transfer_id_list, client_token=None):
        super().__init__()
        self.client_token = client_token
        self.transfer_id_list = transfer_id_list

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.transfer_id_list is not None:
            result['transferIdList'] = self.transfer_id_list
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('transferIdList') is not None:
            self.transfer_id_list = m.get('transferIdList')
        return self