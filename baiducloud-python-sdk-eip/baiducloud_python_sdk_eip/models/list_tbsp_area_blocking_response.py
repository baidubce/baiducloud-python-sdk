from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_eip.models.tbsp_area_blocking_model import TbspAreaBlockingModel

class ListTbspAreaBlockingResponse(BceResponse):
    """
    ListTbspAreaBlockingResponse
    """
    def __init__(self, area_blocking_list=None, id=None):
        super().__init__()
        self.area_blocking_list = area_blocking_list
        self.id = id

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.area_blocking_list is not None:
            result['areaBlockingList'] = [i.to_dict() for i in self.area_blocking_list]
        if self.id is not None:
            result['id'] = self.id
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('areaBlockingList') is not None:
            self.area_blocking_list = [
            TbspAreaBlockingModel().from_dict(i)
            for i in m.get('areaBlockingList')
            ]
        if m.get('id') is not None:
            self.id = m.get('id')
        return self