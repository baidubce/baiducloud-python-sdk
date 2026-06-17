"""
Callback information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcm.models.mention import Mention


class Callback(AbstractModel):
    """
    Callback
    """

    def __init__(self, url=None, mention=None):
        """
        Initialize Callback instance.

        :param url: 回调URL，支持HTTP/HTTPS
        :type url: str (optional)

        :param mention: mention attribute
        :type mention: Mention (optional)
        """
        super().__init__()
        self.url = url
        self.mention = mention

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.url is not None:
            result['url'] = self.url
        if self.mention is not None:
            result['mention'] = self.mention.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Callback

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('mention') is not None:
            self.mention = Mention().from_dict(m.get('mention'))
        return self
