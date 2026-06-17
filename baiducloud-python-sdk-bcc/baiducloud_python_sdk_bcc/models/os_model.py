"""
OsModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class OsModel(AbstractModel):
    """
    OsModel
    """

    def __init__(
        self,
        instance_id=None,
        os_arch=None,
        os_name=None,
        os_version=None,
        os_type=None,
        os_lang=None,
        special_version=None,
    ):
        """
        Initialize OsModel instance.

        :param instance_id: 实例ID
        :type instance_id: str (optional)

        :param os_arch: 操作系统架构
        :type os_arch: str (optional)

        :param os_name: 操作系统名称
        :type os_name: str (optional)

        :param os_version: 操作系统版本
        :type os_version: str (optional)

        :param os_type: 操作系统类型，如linux、windows
        :type os_type: str (optional)

        :param os_lang: 操作系统语言
        :type os_lang: str (optional)

        :param special_version: 特殊版本信息
        :type special_version: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.os_arch = os_arch
        self.os_name = os_name
        self.os_version = os_version
        self.os_type = os_type
        self.os_lang = os_lang
        self.special_version = special_version

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.os_arch is not None:
            result['osArch'] = self.os_arch
        if self.os_name is not None:
            result['osName'] = self.os_name
        if self.os_version is not None:
            result['osVersion'] = self.os_version
        if self.os_type is not None:
            result['osType'] = self.os_type
        if self.os_lang is not None:
            result['osLang'] = self.os_lang
        if self.special_version is not None:
            result['specialVersion'] = self.special_version
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: OsModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('osArch') is not None:
            self.os_arch = m.get('osArch')
        if m.get('osName') is not None:
            self.os_name = m.get('osName')
        if m.get('osVersion') is not None:
            self.os_version = m.get('osVersion')
        if m.get('osType') is not None:
            self.os_type = m.get('osType')
        if m.get('osLang') is not None:
            self.os_lang = m.get('osLang')
        if m.get('specialVersion') is not None:
            self.special_version = m.get('specialVersion')
        return self
