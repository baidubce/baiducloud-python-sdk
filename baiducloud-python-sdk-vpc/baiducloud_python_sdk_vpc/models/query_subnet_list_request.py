from baiducloud_python_sdk_core.abstract_model import AbstractModel

class QuerySubnetListRequest(AbstractModel):
    
    def __init__(self, marker=None, max_keys=None, vpc_id=None, zone_name=None, subnet_type=None, subnet_ids=None):
        super().__init__()
        self.marker = marker
        self.max_keys = max_keys
        self.vpc_id = vpc_id
        self.zone_name = zone_name
        self.subnet_type = subnet_type
        self.subnet_ids = subnet_ids

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('subnetType') is not None:
            self.subnet_type = m.get('subnetType')
        if m.get('subnetIds') is not None:
            self.subnet_ids = m.get('subnetIds')
        return self