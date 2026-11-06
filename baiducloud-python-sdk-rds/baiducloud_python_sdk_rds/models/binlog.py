"""
Binlog information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Binlog(AbstractModel):
    """
    Binlog
    """

    def __init__(self, download_url=None, download_expires=None):
        """
        Initialize Binlog instance.

        :param download_url: 下载链接
        :type download_url: str (optional)

        :param download_expires: 过期时间
        :type download_expires: str (optional)
        """
        super().__init__()
        self.download_url = download_url
        self.download_expires = download_expires

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
        if self.download_url is not None:
            result['downloadUrl'] = self.download_url
        if self.download_expires is not None:
            result['downloadExpires'] = self.download_expires
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Binlog

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')
        if m.get('downloadExpires') is not None:
            self.download_expires = m.get('downloadExpires')
        return self
