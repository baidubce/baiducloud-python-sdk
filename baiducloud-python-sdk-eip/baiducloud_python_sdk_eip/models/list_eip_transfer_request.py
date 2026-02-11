from baiducloud_python_sdk_core.abstract_model import AbstractModel

class ListEipTransferRequest(AbstractModel):
    
    def __init__(self, max_keys=None, marker=None, direction=None, transfer_id=None, status=None, fuzzy_transfer_id=None, fuzzy_instance_id=None, fuzzy_instance_name=None, fuzzy_instance_ip=None):
        super().__init__()
        self.max_keys = max_keys
        self.marker = marker
        self.direction = direction
        self.transfer_id = transfer_id
        self.status = status
        self.fuzzy_transfer_id = fuzzy_transfer_id
        self.fuzzy_instance_id = fuzzy_instance_id
        self.fuzzy_instance_name = fuzzy_instance_name
        self.fuzzy_instance_ip = fuzzy_instance_ip

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('transferId') is not None:
            self.transfer_id = m.get('transferId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('fuzzyTransferId') is not None:
            self.fuzzy_transfer_id = m.get('fuzzyTransferId')
        if m.get('fuzzyInstanceId') is not None:
            self.fuzzy_instance_id = m.get('fuzzyInstanceId')
        if m.get('fuzzyInstanceName') is not None:
            self.fuzzy_instance_name = m.get('fuzzyInstanceName')
        if m.get('fuzzyInstanceIp') is not None:
            self.fuzzy_instance_ip = m.get('fuzzyInstanceIp')
        return self