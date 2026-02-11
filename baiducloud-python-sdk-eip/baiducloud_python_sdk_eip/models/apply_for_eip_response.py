from baiducloud_python_sdk_core.bce_response import BceResponse

class ApplyForEipResponse(BceResponse):
    """
    ApplyForEipResponse
    """
    def __init__(self, eip=None):
        super().__init__()
        self.eip = eip

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.eip is not None:
            result['eip'] = self.eip
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        return self