
from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TbspIpWhitelistModel(AbstractModel):
    """
    TbspIpWhitelistModel
    """
    def __init__(self, ip=None, whitelist_id=None, ip_cidr=None):
        super().__init__()
        self.ip = ip
        self.whitelist_id = whitelist_id
        self.ip_cidr = ip_cidr

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.whitelist_id is not None:
            result['whitelistId'] = self.whitelist_id
        if self.ip_cidr is not None:
            result['ipCidr'] = self.ip_cidr
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('whitelistId') is not None:
            self.whitelist_id = m.get('whitelistId')
        if m.get('ipCidr') is not None:
            self.ip_cidr = m.get('ipCidr')
        return self
