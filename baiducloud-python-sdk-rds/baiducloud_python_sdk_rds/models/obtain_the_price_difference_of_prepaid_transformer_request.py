"""
Request entity for ObtainThePriceDifferenceOfPrepaidTransformerRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ObtainThePriceDifferenceOfPrepaidTransformerRequest(AbstractModel):
    """
    Request entity for ObtainThePriceDifferenceOfPrepaidTransformerRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, instance_id, cpu_count, allocated_memory_in_gb, allocated_storage_in_gb, disk_io_type, category=None
    ):
        """
        Initialize ObtainThePriceDifferenceOfPrepaidTransformerRequest request entity.

        :param instance_id: 实例 ID。
        :type instance_id: str (required)

        :param cpu_count: CPU 个数。
        :type cpu_count: int (required)

        :param allocated_memory_in_gb: 内存大小，单位是 MB。
        :type allocated_memory_in_gb: int (required)

        :param allocated_storage_in_gb: 存储大小，单位是 GB。
        :type allocated_storage_in_gb: int (required)

        :param disk_io_type: disk_io_type parameter
        :type disk_io_type: str (required)

        :param category: 不传值的话默认为双机版，传 Singleton 则指定为单机版。
        :type category: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.cpu_count = cpu_count
        self.allocated_memory_in_gb = allocated_memory_in_gb
        self.allocated_storage_in_gb = allocated_storage_in_gb
        self.disk_io_type = disk_io_type
        self.category = category

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count
        if self.allocated_memory_in_gb is not None:
            result['allocatedMemoryInGB'] = self.allocated_memory_in_gb
        if self.allocated_storage_in_gb is not None:
            result['allocatedStorageInGB'] = self.allocated_storage_in_gb
        if self.disk_io_type is not None:
            result['diskIoType'] = self.disk_io_type
        if self.category is not None:
            result['category'] = self.category
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ObtainThePriceDifferenceOfPrepaidTransformerRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')
        if m.get('allocatedMemoryInGB') is not None:
            self.allocated_memory_in_gb = m.get('allocatedMemoryInGB')
        if m.get('allocatedStorageInGB') is not None:
            self.allocated_storage_in_gb = m.get('allocatedStorageInGB')
        if m.get('diskIoType') is not None:
            self.disk_io_type = m.get('diskIoType')
        if m.get('category') is not None:
            self.category = m.get('category')
        return self
