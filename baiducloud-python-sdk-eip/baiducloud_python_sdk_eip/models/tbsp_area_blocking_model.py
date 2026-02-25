
from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TbspAreaBlockingModel(AbstractModel):
    """
    TbspAreaBlockingModel
    """
    def __init__(self, ip=None, block_area=None, block_begin_time=None, block_end_time=None, block_type=None):
        super().__init__()
        self.ip = ip
        self.block_area = block_area
        self.block_begin_time = block_begin_time
        self.block_end_time = block_end_time
        self.block_type = block_type

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.block_area is not None:
            result['blockArea'] = self.block_area
        if self.block_begin_time is not None:
            result['blockBeginTime'] = self.block_begin_time
        if self.block_end_time is not None:
            result['blockEndTime'] = self.block_end_time
        if self.block_type is not None:
            result['blockType'] = self.block_type
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('blockArea') is not None:
            self.block_area = m.get('blockArea')
        if m.get('blockBeginTime') is not None:
            self.block_begin_time = m.get('blockBeginTime')
        if m.get('blockEndTime') is not None:
            self.block_end_time = m.get('blockEndTime')
        if m.get('blockType') is not None:
            self.block_type = m.get('blockType')
        return self
