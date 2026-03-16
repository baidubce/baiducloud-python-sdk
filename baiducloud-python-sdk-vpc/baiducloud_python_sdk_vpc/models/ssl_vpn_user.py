
from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SslVpnUser(AbstractModel):
    """
    SslVpnUser
    """
    def __init__(self, user_name=None, password=None, description=None):
        super().__init__()
        self.user_name = user_name
        self.password = password
        self.description = description

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.password is not None:
            result['password'] = self.password
        if self.description is not None:
            result['description'] = self.description
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
