
from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TbspIpCleanModel(AbstractModel):
    """
    TbspIpCleanModel
    """
    def __init__(self, ip=None, eip_name=None, eip_id=None, threshold_type=None, ip_clean_mbps=None, ip_clean_pps=None, protect_level=None, turn_off_begin_time=None, turn_off_end_time=None):
        super().__init__()
        self.ip = ip
        self.eip_name = eip_name
        self.eip_id = eip_id
        self.threshold_type = threshold_type
        self.ip_clean_mbps = ip_clean_mbps
        self.ip_clean_pps = ip_clean_pps
        self.protect_level = protect_level
        self.turn_off_begin_time = turn_off_begin_time
        self.turn_off_end_time = turn_off_end_time

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.eip_name is not None:
            result['eipName'] = self.eip_name
        if self.eip_id is not None:
            result['eipId'] = self.eip_id
        if self.threshold_type is not None:
            result['thresholdType'] = self.threshold_type
        if self.ip_clean_mbps is not None:
            result['ipCleanMbps'] = self.ip_clean_mbps
        if self.ip_clean_pps is not None:
            result['ipCleanPps'] = self.ip_clean_pps
        if self.protect_level is not None:
            result['protectLevel'] = self.protect_level
        if self.turn_off_begin_time is not None:
            result['turnOffBeginTime'] = self.turn_off_begin_time
        if self.turn_off_end_time is not None:
            result['turnOffEndTime'] = self.turn_off_end_time
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('eipName') is not None:
            self.eip_name = m.get('eipName')
        if m.get('eipId') is not None:
            self.eip_id = m.get('eipId')
        if m.get('thresholdType') is not None:
            self.threshold_type = m.get('thresholdType')
        if m.get('ipCleanMbps') is not None:
            self.ip_clean_mbps = m.get('ipCleanMbps')
        if m.get('ipCleanPps') is not None:
            self.ip_clean_pps = m.get('ipCleanPps')
        if m.get('protectLevel') is not None:
            self.protect_level = m.get('protectLevel')
        if m.get('turnOffBeginTime') is not None:
            self.turn_off_begin_time = m.get('turnOffBeginTime')
        if m.get('turnOffEndTime') is not None:
            self.turn_off_end_time = m.get('turnOffEndTime')
        return self
