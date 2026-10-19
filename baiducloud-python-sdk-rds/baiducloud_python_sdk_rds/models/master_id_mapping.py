"""
MasterIdMapping information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MasterIdMapping(AbstractModel):
    """
    MasterIdMapping
    """

    def __init__(
        self,
        app_id=None,
        app_id_short=None,
        status=None,
        allocated_memory_in_mb=None,
        cpu_count=None,
        allocated_storage_in_gb=None,
        used_storage_in_gb=None,
    ):
        """
        Initialize MasterIdMapping instance.

        :param app_id: 只读实例ID。
        :type app_id: str (optional)

        :param app_id_short: 只读实例短ID。
        :type app_id_short: str (optional)

        :param status: status attribute
        :type status: str (optional)

        :param allocated_memory_in_mb: 分配内存大小（单位:MB）。
        :type allocated_memory_in_mb: int (optional)

        :param cpu_count: cpu个数。
        :type cpu_count: int (optional)

        :param allocated_storage_in_gb: 分配存储大小（单位GB）。
        :type allocated_storage_in_gb: int (optional)

        :param used_storage_in_gb: 分配存储大小（单位GB）。
        :type used_storage_in_gb: float (optional)
        """
        super().__init__()
        self.app_id = app_id
        self.app_id_short = app_id_short
        self.status = status
        self.allocated_memory_in_mb = allocated_memory_in_mb
        self.cpu_count = cpu_count
        self.allocated_storage_in_gb = allocated_storage_in_gb
        self.used_storage_in_gb = used_storage_in_gb

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
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.app_id_short is not None:
            result['appIdShort'] = self.app_id_short
        if self.status is not None:
            result['status'] = self.status
        if self.allocated_memory_in_mb is not None:
            result['allocatedMemoryInMB'] = self.allocated_memory_in_mb
        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count
        if self.allocated_storage_in_gb is not None:
            result['allocatedStorageInGB'] = self.allocated_storage_in_gb
        if self.used_storage_in_gb is not None:
            result['usedStorageInGB'] = self.used_storage_in_gb
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MasterIdMapping

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('appIdShort') is not None:
            self.app_id_short = m.get('appIdShort')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('allocatedMemoryInMB') is not None:
            self.allocated_memory_in_mb = m.get('allocatedMemoryInMB')
        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')
        if m.get('allocatedStorageInGB') is not None:
            self.allocated_storage_in_gb = m.get('allocatedStorageInGB')
        if m.get('usedStorageInGB') is not None:
            self.used_storage_in_gb = m.get('usedStorageInGB')
        return self
