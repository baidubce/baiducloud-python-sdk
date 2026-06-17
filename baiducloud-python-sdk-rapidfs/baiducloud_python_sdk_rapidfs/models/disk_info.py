"""
DiskInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DiskInfo(AbstractModel):
    """
    DiskInfo
    """

    def __init__(self, dev=None, mount_path=None, disk_quota_gi_b=None, format=None, disk_type=None):
        """
        Initialize DiskInfo instance.

        :param dev: 设备名
        :type dev: str (optional)

        :param mount_path: 挂载路径
        :type mount_path: str (optional)

        :param disk_quota_gi_b: 磁盘配额，单位 GiB
        :type disk_quota_gi_b: int (optional)

        :param format: 是否格式化：format=true 时必须给出 dev；format=false 时必须给出 diskQuotaGiB
        :type format: bool (optional)

        :param disk_type: 磁盘类型（可选）
        :type disk_type: str (optional)
        """
        super().__init__()
        self.dev = dev
        self.mount_path = mount_path
        self.disk_quota_gi_b = disk_quota_gi_b
        self.format = format
        self.disk_type = disk_type

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
        if self.dev is not None:
            result['dev'] = self.dev
        if self.mount_path is not None:
            result['mountPath'] = self.mount_path
        if self.disk_quota_gi_b is not None:
            result['diskQuotaGiB'] = self.disk_quota_gi_b
        if self.format is not None:
            result['format'] = self.format
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DiskInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('dev') is not None:
            self.dev = m.get('dev')
        if m.get('mountPath') is not None:
            self.mount_path = m.get('mountPath')
        if m.get('diskQuotaGiB') is not None:
            self.disk_quota_gi_b = m.get('diskQuotaGiB')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self
