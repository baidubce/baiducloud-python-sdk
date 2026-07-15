"""
FileUpload information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FileUpload(AbstractModel):
    """
    FileUpload
    """

    def __init__(
        self,
        os=None,
        content=None,
        filename=None,
        filepath=None,
        bos_bucket_name=None,
        bos_file_path=None,
        bos_etag=None,
        user=None,
        group=None,
        mode=None,
        overwrite=None,
    ):
        """
        Initialize FileUpload instance.

        :param os: 操作系统。枚举值：LINUX，WINDOWS
        :type os: str (optional)

        :param content: 文件内容
        :type content: str (optional)

        :param filename: 文件名称
        :type filename: str (optional)

        :param filepath: 目标路径
        :type filepath: str (optional)

        :param bos_bucket_name: bos桶名称
        :type bos_bucket_name: str (optional)

        :param bos_file_path: bos文件路径
        :type bos_file_path: str (optional)

        :param bos_etag: 文件唯一标识符
        :type bos_etag: str (optional)

        :param user: 用户，仅Linux文件上传需要
        :type user: str (optional)

        :param group: 用户组，仅Linux文件上传需要
        :type group: str (optional)

        :param mode: 文件权限，仅Linux文件上传需要
        :type mode: str (optional)

        :param overwrite: 是否覆盖目标路径下的同名文件
        :type overwrite: bool (optional)
        """
        super().__init__()
        self.os = os
        self.content = content
        self.filename = filename
        self.filepath = filepath
        self.bos_bucket_name = bos_bucket_name
        self.bos_file_path = bos_file_path
        self.bos_etag = bos_etag
        self.user = user
        self.group = group
        self.mode = mode
        self.overwrite = overwrite

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
        if self.os is not None:
            result['os'] = self.os
        if self.content is not None:
            result['content'] = self.content
        if self.filename is not None:
            result['filename'] = self.filename
        if self.filepath is not None:
            result['filepath'] = self.filepath
        if self.bos_bucket_name is not None:
            result['bosBucketName'] = self.bos_bucket_name
        if self.bos_file_path is not None:
            result['bosFilePath'] = self.bos_file_path
        if self.bos_etag is not None:
            result['bosEtag'] = self.bos_etag
        if self.user is not None:
            result['user'] = self.user
        if self.group is not None:
            result['group'] = self.group
        if self.mode is not None:
            result['mode'] = self.mode
        if self.overwrite is not None:
            result['overwrite'] = self.overwrite
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FileUpload

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('os') is not None:
            self.os = m.get('os')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('filename') is not None:
            self.filename = m.get('filename')
        if m.get('filepath') is not None:
            self.filepath = m.get('filepath')
        if m.get('bosBucketName') is not None:
            self.bos_bucket_name = m.get('bosBucketName')
        if m.get('bosFilePath') is not None:
            self.bos_file_path = m.get('bosFilePath')
        if m.get('bosEtag') is not None:
            self.bos_etag = m.get('bosEtag')
        if m.get('user') is not None:
            self.user = m.get('user')
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('overwrite') is not None:
            self.overwrite = m.get('overwrite')
        return self
