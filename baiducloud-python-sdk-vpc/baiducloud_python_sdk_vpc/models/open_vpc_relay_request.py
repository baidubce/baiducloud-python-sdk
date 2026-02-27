from baiducloud_python_sdk_core.abstract_model import AbstractModel

class OpenVpcRelayRequest(AbstractModel):
    
    def __init__(self, vpc_id, client_token=None):
        super().__init__()
        self.vpc_id = vpc_id
        self.client_token = client_token

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
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self