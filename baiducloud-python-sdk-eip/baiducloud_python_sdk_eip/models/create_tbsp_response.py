from baiducloud_python_sdk_core.bce_response import BceResponse

class CreateTbspResponse(BceResponse):
    """
    CreateTbspResponse
    """
    def __init__(self, id=None):
        super().__init__()
        self.id = id

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.id is not None:
            result['id'] = self.id
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self