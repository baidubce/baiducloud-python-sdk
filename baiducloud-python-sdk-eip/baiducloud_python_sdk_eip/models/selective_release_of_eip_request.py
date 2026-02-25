from baiducloud_python_sdk_core.abstract_model import AbstractModel

class SelectiveReleaseOfEipRequest(AbstractModel):
    
    def __init__(self, eip, release_to_recycle=None, client_token=None):
        super().__init__()
        self.eip = eip
        self.release_to_recycle = release_to_recycle
        self.client_token = client_token

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('releaseToRecycle') is not None:
            self.release_to_recycle = m.get('releaseToRecycle')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self