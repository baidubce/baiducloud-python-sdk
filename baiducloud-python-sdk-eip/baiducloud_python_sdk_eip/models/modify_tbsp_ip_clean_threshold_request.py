from baiducloud_python_sdk_core.abstract_model import AbstractModel

class ModifyTbspIpCleanThresholdRequest(AbstractModel):
    
    def __init__(self, id, client_token=None, ip=None, threshold_type=None, clean_mbps=None, clean_pps=None):
        super().__init__()
        self.id = id
        self.client_token = client_token
        self.ip = ip
        self.threshold_type = threshold_type
        self.clean_mbps = clean_mbps
        self.clean_pps = clean_pps

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.threshold_type is not None:
            result['thresholdType'] = self.threshold_type
        if self.clean_mbps is not None:
            result['cleanMbps'] = self.clean_mbps
        if self.clean_pps is not None:
            result['cleanPps'] = self.clean_pps
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('thresholdType') is not None:
            self.threshold_type = m.get('thresholdType')
        if m.get('cleanMbps') is not None:
            self.clean_mbps = m.get('cleanMbps')
        if m.get('cleanPps') is not None:
            self.clean_pps = m.get('cleanPps')
        return self