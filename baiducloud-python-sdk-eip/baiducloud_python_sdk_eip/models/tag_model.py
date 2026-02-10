
from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TagModel(AbstractModel):
    """
    TagModel
    """
    def __init__(self, tag_key=None, tag_value=None):
        super().__init__()
        self.tag_key = tag_key
        self.tag_value = tag_value

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self
