"""
SystemImageModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SystemImageModel(AbstractModel):
    """
    SystemImageModel
    """

    def __init__(
        self,
        image_id=None,
        image_name=None,
        os_type=None,
        os_version=None,
        os_arch=None,
        os_name=None,
        os_lang=None,
        min_size_in_gi_b=None,
    ):
        """
        Initialize SystemImageModel instance.

        :param image_id: 镜像ID
        :type image_id: str (optional)

        :param image_name: 镜像名称
        :type image_name: str (optional)

        :param os_type: 操作系统类型，如linux、windows
        :type os_type: str (optional)

        :param os_version: 操作系统版本
        :type os_version: str (optional)

        :param os_arch: 操作系统架构
        :type os_arch: str (optional)

        :param os_name: 操作系统名称
        :type os_name: str (optional)

        :param os_lang: 操作系统语言
        :type os_lang: str (optional)

        :param min_size_in_gi_b: 创建实例时所需的最小磁盘大小，单位GiB
        :type min_size_in_gi_b: int (optional)
        """
        super().__init__()
        self.image_id = image_id
        self.image_name = image_name
        self.os_type = os_type
        self.os_version = os_version
        self.os_arch = os_arch
        self.os_name = os_name
        self.os_lang = os_lang
        self.min_size_in_gi_b = min_size_in_gi_b

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
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.image_name is not None:
            result['imageName'] = self.image_name
        if self.os_type is not None:
            result['osType'] = self.os_type
        if self.os_version is not None:
            result['osVersion'] = self.os_version
        if self.os_arch is not None:
            result['osArch'] = self.os_arch
        if self.os_name is not None:
            result['osName'] = self.os_name
        if self.os_lang is not None:
            result['osLang'] = self.os_lang
        if self.min_size_in_gi_b is not None:
            result['minSizeInGiB'] = self.min_size_in_gi_b
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SystemImageModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('imageName') is not None:
            self.image_name = m.get('imageName')
        if m.get('osType') is not None:
            self.os_type = m.get('osType')
        if m.get('osVersion') is not None:
            self.os_version = m.get('osVersion')
        if m.get('osArch') is not None:
            self.os_arch = m.get('osArch')
        if m.get('osName') is not None:
            self.os_name = m.get('osName')
        if m.get('osLang') is not None:
            self.os_lang = m.get('osLang')
        if m.get('minSizeInGiB') is not None:
            self.min_size_in_gi_b = m.get('minSizeInGiB')
        return self
