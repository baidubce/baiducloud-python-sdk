
from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Cgw(AbstractModel):
    """
    Cgw
    """
    def __init__(self, cgw_id=None, name=None, ip=None, description=None, created_time=None, updated_time=None):
        super().__init__()
        self.cgw_id = cgw_id
        self.name = name
        self.ip = ip
        self.description = description
        self.created_time = created_time
        self.updated_time = updated_time

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.cgw_id is not None:
            result['cgwId'] = self.cgw_id
        if self.name is not None:
            result['name'] = self.name
        if self.ip is not None:
            result['ip'] = self.ip
        if self.description is not None:
            result['description'] = self.description
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.updated_time is not None:
            result['updatedTime'] = self.updated_time
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('cgwId') is not None:
            self.cgw_id = m.get('cgwId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')
        return self
