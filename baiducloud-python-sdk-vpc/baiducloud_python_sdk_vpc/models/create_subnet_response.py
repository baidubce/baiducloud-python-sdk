from baiducloud_python_sdk_core.bce_response import BceResponse

class CreateSubnetResponse(BceResponse):
    """
    CreateSubnetResponse
    """
    def __init__(self, subnet_id=None):
        super().__init__()
        self.subnet_id = subnet_id

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        return self