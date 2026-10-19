"""
ReplicaRequest information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ReplicaRequest(AbstractModel):
    """
    ReplicaRequest
    """

    def __init__(
        self, instance_id=None, cpu_count=None, memory_capacity=None, volume_capacity=None, disk_io_type=None
    ):
        """
        Initialize ReplicaRequest instance.

        :param instance_id: 批量变配的只读实例ID
        :type instance_id: str (optional)

        :param cpu_count: 只读实例CPU核数，最小值是1
        :type cpu_count: int (optional)

        :param memory_capacity: 只读实例内存大小，单位GB。最小值为1
        :type memory_capacity: int (optional)

        :param volume_capacity: volume_capacity attribute
        :type volume_capacity: int (optional)

        :param disk_io_type: disk_io_type attribute
        :type disk_io_type: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.cpu_count = cpu_count
        self.memory_capacity = memory_capacity
        self.volume_capacity = volume_capacity
        self.disk_io_type = disk_io_type

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
        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count
        if self.memory_capacity is not None:
            result['memoryCapacity'] = self.memory_capacity
        if self.volume_capacity is not None:
            result['volumeCapacity'] = self.volume_capacity
        if self.disk_io_type is not None:
            result['diskIoType'] = self.disk_io_type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ReplicaRequest

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')
        if m.get('memoryCapacity') is not None:
            self.memory_capacity = m.get('memoryCapacity')
        if m.get('volumeCapacity') is not None:
            self.volume_capacity = m.get('volumeCapacity')
        if m.get('diskIoType') is not None:
            self.disk_io_type = m.get('diskIoType')
        return self
