from baiducloud_python_sdk_core.abstract_model import AbstractModel

class CreateEipTransferRequest(AbstractModel):
    
    def __init__(self, transfer_type, transfer_resource_list, to_user_id, client_token=None):
        super().__init__()
        self.client_token = client_token
        self.transfer_type = transfer_type
        self.transfer_resource_list = transfer_resource_list
        self.to_user_id = to_user_id

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.transfer_type is not None:
            result['transferType'] = self.transfer_type
        if self.transfer_resource_list is not None:
            result['transferResourceList'] = self.transfer_resource_list
        if self.to_user_id is not None:
            result['toUserId'] = self.to_user_id
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('transferType') is not None:
            self.transfer_type = m.get('transferType')
        if m.get('transferResourceList') is not None:
            self.transfer_resource_list = m.get('transferResourceList')
        if m.get('toUserId') is not None:
            self.to_user_id = m.get('toUserId')
        return self