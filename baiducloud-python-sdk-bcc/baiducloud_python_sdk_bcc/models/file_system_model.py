"""
FileSystemModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FileSystemModel(AbstractModel):
    """
    FileSystemModel
    """

    def __init__(self, fs_id=None, mount_ads=None, path=None, protocol=None):
        """
        Initialize FileSystemModel instance.

        :param fs_id: cfs文件系统ID
        :type fs_id: str (optional)

        :param mount_ads: 挂载目标的地址
        :type mount_ads: str (optional)

        :param path: 挂载目录
        :type path: str (optional)

        :param protocol: cfs文件系统的协议类型，可选值为：nfs，smb
        :type protocol: str (optional)
        """
        super().__init__()
        self.fs_id = fs_id
        self.mount_ads = mount_ads
        self.path = path
        self.protocol = protocol

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
        if self.fs_id is not None:
            result['fsId'] = self.fs_id
        if self.mount_ads is not None:
            result['mountAds'] = self.mount_ads
        if self.path is not None:
            result['path'] = self.path
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FileSystemModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('fsId') is not None:
            self.fs_id = m.get('fsId')
        if m.get('mountAds') is not None:
            self.mount_ads = m.get('mountAds')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self
