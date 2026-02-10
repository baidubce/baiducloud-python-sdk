from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.show_vpc_model import ShowVpcModel

class QuerySpecifiedVpcResponse(BceResponse):
    """
    QuerySpecifiedVpcResponse
    """
    def __init__(self, vpc=None):
        super().__init__()
        self.vpc = vpc

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.vpc is not None:
            result['vpc'] = self.vpc.to_dict()
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('vpc') is not None:
            self.vpc = ShowVpcModel().from_dict(m.get('vpc'))
        return self