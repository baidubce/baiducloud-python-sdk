"""
ImageModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcc.models.snapshot_model import SnapshotModel


class ImageModel(AbstractModel):
    """
    ImageModel
    """

    def __init__(
        self,
        id=None,
        name=None,
        type=None,
        os_type=None,
        os_version=None,
        os_arch=None,
        os_name=None,
        os_build=None,
        os_lang=None,
        special_version=None,
        create_time=None,
        status=None,
        encrypted=None,
        package=None,
        desc=None,
        disk_size=None,
        min_disk_gb=None,
        ephemeral_size=None,
        snapshots=None,
    ):
        """
        Initialize ImageModel instance.

        :param id: 镜像ID（查询镜像列表、查询镜像详情）
        :type id: str (optional)

        :param name: 镜像名称（查询镜像列表、查询镜像详情）
        :type name: str (optional)

        :param type: 镜像类型（查询镜像列表、查询镜像详情）
        :type type: str (optional)

        :param os_type: 操作系统类型，如linux、windows（查询镜像列表、查询镜像详情）
        :type os_type: str (optional)

        :param os_version: 操作系统版本（查询镜像列表、查询镜像详情）
        :type os_version: str (optional)

        :param os_arch: 操作系统架构（查询镜像列表、查询镜像详情）
        :type os_arch: str (optional)

        :param os_name: 操作系统名称（查询镜像列表、查询镜像详情）
        :type os_name: str (optional)

        :param os_build: 操作系统构建版本（查询镜像列表、查询镜像详情）
        :type os_build: str (optional)

        :param os_lang: 操作系统语言（查询镜像列表、查询镜像详情）
        :type os_lang: str (optional)

        :param special_version: 特殊版本信息（查询镜像列表、查询镜像详情）
        :type special_version: str (optional)

        :param create_time: 镜像创建时间（查询镜像列表、查询镜像详情）
        :type create_time: str (optional)

        :param status: 镜像状态（查询镜像列表、查询镜像详情）
        :type status: str (optional)

        :param encrypted: 镜像是否加密（查询镜像列表、查询镜像详情）
        :type encrypted: bool (optional)

        :param package: 是否为大镜像（包含所有CDS盘）（查询镜像列表、查询镜像详情）
        :type package: bool (optional)

        :param desc: 镜像描述（查询镜像列表、查询镜像详情）
        :type desc: str (optional)

        :param disk_size: 磁盘大小（查询镜像详情）
        :type disk_size: int (optional)

        :param min_disk_gb: 创建实例时所需的最小磁盘大小，单位GB（查询镜像详情）
        :type min_disk_gb: int (optional)

        :param ephemeral_size: 临时盘大小（查询镜像详情）
        :type ephemeral_size: int (optional)

        :param snapshots: 镜像关联的快照列表（查询镜像详情）
        :type snapshots: List[SnapshotModel] (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.type = type
        self.os_type = os_type
        self.os_version = os_version
        self.os_arch = os_arch
        self.os_name = os_name
        self.os_build = os_build
        self.os_lang = os_lang
        self.special_version = special_version
        self.create_time = create_time
        self.status = status
        self.encrypted = encrypted
        self.package = package
        self.desc = desc
        self.disk_size = disk_size
        self.min_disk_gb = min_disk_gb
        self.ephemeral_size = ephemeral_size
        self.snapshots = snapshots

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
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.os_type is not None:
            result['osType'] = self.os_type
        if self.os_version is not None:
            result['osVersion'] = self.os_version
        if self.os_arch is not None:
            result['osArch'] = self.os_arch
        if self.os_name is not None:
            result['osName'] = self.os_name
        if self.os_build is not None:
            result['osBuild'] = self.os_build
        if self.os_lang is not None:
            result['osLang'] = self.os_lang
        if self.special_version is not None:
            result['specialVersion'] = self.special_version
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.status is not None:
            result['status'] = self.status
        if self.encrypted is not None:
            result['encrypted'] = self.encrypted
        if self.package is not None:
            result['package'] = self.package
        if self.desc is not None:
            result['desc'] = self.desc
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.min_disk_gb is not None:
            result['minDiskGb'] = self.min_disk_gb
        if self.ephemeral_size is not None:
            result['ephemeralSize'] = self.ephemeral_size
        if self.snapshots is not None:
            result['snapshots'] = [i.to_dict() for i in self.snapshots]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ImageModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('osType') is not None:
            self.os_type = m.get('osType')
        if m.get('osVersion') is not None:
            self.os_version = m.get('osVersion')
        if m.get('osArch') is not None:
            self.os_arch = m.get('osArch')
        if m.get('osName') is not None:
            self.os_name = m.get('osName')
        if m.get('osBuild') is not None:
            self.os_build = m.get('osBuild')
        if m.get('osLang') is not None:
            self.os_lang = m.get('osLang')
        if m.get('specialVersion') is not None:
            self.special_version = m.get('specialVersion')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')
        if m.get('package') is not None:
            self.package = m.get('package')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('minDiskGb') is not None:
            self.min_disk_gb = m.get('minDiskGb')
        if m.get('ephemeralSize') is not None:
            self.ephemeral_size = m.get('ephemeralSize')
        if m.get('snapshots') is not None:
            self.snapshots = [SnapshotModel().from_dict(i) for i in m.get('snapshots')]
        return self
