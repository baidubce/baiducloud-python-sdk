"""
Volume information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bci.models.nfs_volume import NfsVolume

from baiducloud_python_sdk_bci.models.empty_dir_volume import EmptyDirVolume

from baiducloud_python_sdk_bci.models.config_file_volume import ConfigFileVolume


class Volume(AbstractModel):
    """
    Volume
    """

    def __init__(self, nfs=None, empty_dir=None, config_file=None):
        """
        Initialize Volume instance.

        :param nfs: NFS类型数据卷（网络文件系统）
        :type nfs: List[NfsVolume] (optional)

        :param empty_dir: EmptyDir类型数据卷（空目录）
        :type empty_dir: List[EmptyDirVolume] (optional)

        :param config_file: ConfigFile类型数据卷（配置文件）
        :type config_file: List[ConfigFileVolume] (optional)
        """
        super().__init__()
        self.nfs = nfs
        self.empty_dir = empty_dir
        self.config_file = config_file

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
        if self.nfs is not None:
            result['nfs'] = [i.to_dict() for i in self.nfs]
        if self.empty_dir is not None:
            result['emptyDir'] = [i.to_dict() for i in self.empty_dir]
        if self.config_file is not None:
            result['configFile'] = [i.to_dict() for i in self.config_file]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Volume

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('nfs') is not None:
            self.nfs = [NfsVolume().from_dict(i) for i in m.get('nfs')]
        if m.get('emptyDir') is not None:
            self.empty_dir = [EmptyDirVolume().from_dict(i) for i in m.get('emptyDir')]
        if m.get('configFile') is not None:
            self.config_file = [ConfigFileVolume().from_dict(i) for i in m.get('configFile')]
        return self
