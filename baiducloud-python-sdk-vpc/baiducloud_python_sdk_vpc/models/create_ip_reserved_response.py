from baiducloud_python_sdk_core.bce_response import BceResponse

class CreateIpReservedResponse(BceResponse):
    """
    CreateIpReservedResponse
    """
    def __init__(self, ip_reserve_id=None):
        super().__init__()
        self.ip_reserve_id = ip_reserve_id

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.ip_reserve_id is not None:
            result['ipReserveId'] = self.ip_reserve_id
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('ipReserveId') is not None:
            self.ip_reserve_id = m.get('ipReserveId')
        return self