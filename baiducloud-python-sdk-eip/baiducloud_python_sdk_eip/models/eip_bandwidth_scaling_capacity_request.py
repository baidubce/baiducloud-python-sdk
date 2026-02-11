from baiducloud_python_sdk_core.abstract_model import AbstractModel

class EipBandwidthScalingCapacityRequest(AbstractModel):
    
    def __init__(self, eip, new_bandwidth_in_mbps, client_token=None):
        super().__init__()
        self.eip = eip
        self.client_token = client_token
        self.new_bandwidth_in_mbps = new_bandwidth_in_mbps

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.new_bandwidth_in_mbps is not None:
            result['newBandwidthInMbps'] = self.new_bandwidth_in_mbps
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('newBandwidthInMbps') is not None:
            self.new_bandwidth_in_mbps = m.get('newBandwidthInMbps')
        return self