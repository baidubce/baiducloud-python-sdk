"""
DiskInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DiskInfo(AbstractModel):
    """
    DiskInfo
    """

    def __init__(self, storage_type=None, max_disk_size=None, min_disk_size=None):
        """
        Initialize DiskInfo instance.

        :param storage_type: storage_type attribute
        :type storage_type: str (optional)

        :param max_disk_size: 最大单盘可创建磁盘容量
        :type max_disk_size: int (optional)

        :param min_disk_size: 最小单盘创建磁盘容量
        :type min_disk_size: int (optional)
        """
        super().__init__()
        self.storage_type = storage_type
        self.max_disk_size = max_disk_size
        self.min_disk_size = min_disk_size

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
        if self.storage_type is not None:
            result['storageType'] = self.storage_type
        if self.max_disk_size is not None:
            result['maxDiskSize'] = self.max_disk_size
        if self.min_disk_size is not None:
            result['minDiskSize'] = self.min_disk_size
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
        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')
        if m.get('maxDiskSize') is not None:
            self.max_disk_size = m.get('maxDiskSize')
        if m.get('minDiskSize') is not None:
            self.min_disk_size = m.get('minDiskSize')
        return self
