"""
Request entity for TransformationExampleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_rds.models.subnet_map import SubnetMap


class TransformationExampleRequest(AbstractModel):
    """
    Request entity for TransformationExampleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        cpu_count,
        memory_capacity,
        volume_capacity,
        allocated_memory_in_mb=None,
        node_amount=None,
        is_direct_pay=None,
        is_enhanced=None,
        effective_time=None,
        master_azone=None,
        backup_azone=None,
        disk_io_type=None,
        subnet_id=None,
        edge_subnet_id=None,
        subnets=None,
    ):
        """
        Initialize TransformationExampleRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param cpu_count: CPU核数，最小值是1
        :type cpu_count: int (required)

        :param memory_capacity: 内存大小，单位GB。最小值为1
        :type memory_capacity: int (required)

        :param volume_capacity: volume_capacity parameter
        :type volume_capacity: int (required)

        :param allocated_memory_in_mb: 内存大小，单位MB。最小值为1
        :type allocated_memory_in_mb: int (optional)

        :param node_amount: node_amount parameter
        :type node_amount: int (optional)

        :param is_direct_pay: 是否进行直接支付，默认为否，设置为直接支付的变配订单会直接扣款，不需要在走支付逻辑
        :type is_direct_pay: bool (optional)

        :param is_enhanced: 是否为增强版RDS
        :type is_enhanced: bool (optional)

        :param effective_time: effective_time parameter
        :type effective_time: str (optional)

        :param master_azone: 变配时需要变更主库可用区，此参数需要传值，如：cn-bj-a。不传默认取当前主库az
        :type master_azone: str (optional)

        :param backup_azone: 变配时需要变更备库可用区，此参数需要传值，如：cn-bj-a。不传默认取当前备库az
        :type backup_azone: str (optional)

        :param disk_io_type: disk_io_type parameter
        :type disk_io_type: str (optional)

        :param subnet_id: 子网ID，默认为空
        :type subnet_id: str (optional)

        :param edge_subnet_id: 边缘子网ID
        :type edge_subnet_id: str (optional)

        :param subnets: 变配时如果主库或备库需要变更可用区，此参数需要传值
        :type subnets: List[SubnetMap] (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.cpu_count = cpu_count
        self.memory_capacity = memory_capacity
        self.volume_capacity = volume_capacity
        self.allocated_memory_in_mb = allocated_memory_in_mb
        self.node_amount = node_amount
        self.is_direct_pay = is_direct_pay
        self.is_enhanced = is_enhanced
        self.effective_time = effective_time
        self.master_azone = master_azone
        self.backup_azone = backup_azone
        self.disk_io_type = disk_io_type
        self.subnet_id = subnet_id
        self.edge_subnet_id = edge_subnet_id
        self.subnets = subnets

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
        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count
        if self.memory_capacity is not None:
            result['memoryCapacity'] = self.memory_capacity
        if self.volume_capacity is not None:
            result['volumeCapacity'] = self.volume_capacity
        if self.allocated_memory_in_mb is not None:
            result['allocatedMemoryInMB'] = self.allocated_memory_in_mb
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.is_direct_pay is not None:
            result['isDirectPay'] = self.is_direct_pay
        if self.is_enhanced is not None:
            result['isEnhanced'] = self.is_enhanced
        if self.effective_time is not None:
            result['effectiveTime'] = self.effective_time
        if self.master_azone is not None:
            result['masterAzone'] = self.master_azone
        if self.backup_azone is not None:
            result['backupAzone'] = self.backup_azone
        if self.disk_io_type is not None:
            result['diskIoType'] = self.disk_io_type
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.edge_subnet_id is not None:
            result['edgeSubnetId'] = self.edge_subnet_id
        if self.subnets is not None:
            result['subnets'] = [i.to_dict() for i in self.subnets]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TransformationExampleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
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
        if m.get('allocatedMemoryInMB') is not None:
            self.allocated_memory_in_mb = m.get('allocatedMemoryInMB')
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('isDirectPay') is not None:
            self.is_direct_pay = m.get('isDirectPay')
        if m.get('isEnhanced') is not None:
            self.is_enhanced = m.get('isEnhanced')
        if m.get('effectiveTime') is not None:
            self.effective_time = m.get('effectiveTime')
        if m.get('masterAzone') is not None:
            self.master_azone = m.get('masterAzone')
        if m.get('backupAzone') is not None:
            self.backup_azone = m.get('backupAzone')
        if m.get('diskIoType') is not None:
            self.disk_io_type = m.get('diskIoType')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('edgeSubnetId') is not None:
            self.edge_subnet_id = m.get('edgeSubnetId')
        if m.get('subnets') is not None:
            self.subnets = [SubnetMap().from_dict(i) for i in m.get('subnets')]
        return self
