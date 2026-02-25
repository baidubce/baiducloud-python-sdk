from baiducloud_python_sdk_core.bce_response import BceResponse

class CreateVpcResponse(BceResponse):
    """
    CreateVpcResponse
    """
    def __init__(self, vpc_id=None):
        super().__init__()
        self.vpc_id = vpc_id

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self