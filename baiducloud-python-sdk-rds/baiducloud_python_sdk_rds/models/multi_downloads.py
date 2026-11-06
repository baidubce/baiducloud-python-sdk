"""
MultiDownloads information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MultiDownloads(AbstractModel):
    """
    MultiDownloads
    """

    def __init__(self, db_name=None, download_name=None, download_size=None, download_url=None):
        """
        Initialize MultiDownloads instance.

        :param db_name: 数据库名称
        :type db_name: str (optional)

        :param download_name: 下载链接名称
        :type download_name: str (optional)

        :param download_size: 备份大小，单位为 Byte
        :type download_size: int (optional)

        :param download_url: 备份下载链接
        :type download_url: str (optional)
        """
        super().__init__()
        self.db_name = db_name
        self.download_name = download_name
        self.download_size = download_size
        self.download_url = download_url

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
        if self.db_name is not None:
            result['dbName'] = self.db_name
        if self.download_name is not None:
            result['downloadName'] = self.download_name
        if self.download_size is not None:
            result['downloadSize'] = self.download_size
        if self.download_url is not None:
            result['downloadUrl'] = self.download_url
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MultiDownloads

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')
        if m.get('downloadName') is not None:
            self.download_name = m.get('downloadName')
        if m.get('downloadSize') is not None:
            self.download_size = m.get('downloadSize')
        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')
        return self
