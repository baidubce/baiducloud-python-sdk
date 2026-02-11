from baiducloud_python_sdk_core.abstract_model import AbstractModel

class BindEipRequest(AbstractModel):
    
    def __init__(self, eip, client_token, instance_type, instance_id, instance_ip=None):
        super().__init__()
        self.eip = eip
        self.client_token = client_token
        self.instance_type = instance_type
        self.instance_id = instance_id
        self.instance_ip = instance_ip

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_ip is not None:
            result['instanceIp'] = self.instance_ip
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceIp') is not None:
            self.instance_ip = m.get('instanceIp')
        return self