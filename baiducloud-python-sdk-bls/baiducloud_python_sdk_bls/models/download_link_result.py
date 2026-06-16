"""
DownloadLinkResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DownloadLinkResult(AbstractModel):
    """
    DownloadLinkResult
    """

    def __init__(self, file_dir=None, file_name=None, link=None):
        """
        Initialize DownloadLinkResult instance.

        :param file_dir: 下载文件目录
        :type file_dir: str (optional)

        :param file_name: 下载文件名称
        :type file_name: str (optional)

        :param link: 下载文件的下载链接
        :type link: str (optional)
        """
        super().__init__()
        self.file_dir = file_dir
        self.file_name = file_name
        self.link = link

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
        if self.file_dir is not None:
            result['fileDir'] = self.file_dir
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.link is not None:
            result['link'] = self.link
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DownloadLinkResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('fileDir') is not None:
            self.file_dir = m.get('fileDir')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('link') is not None:
            self.link = m.get('link')
        return self
