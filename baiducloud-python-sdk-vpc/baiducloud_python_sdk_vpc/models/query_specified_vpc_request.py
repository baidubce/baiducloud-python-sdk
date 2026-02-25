from baiducloud_python_sdk_core.abstract_model import AbstractModel

class QuerySpecifiedVpcRequest(AbstractModel):
    
    def __init__(self, vpc_id):
        super().__init__()
        self.vpc_id = vpc_id

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self