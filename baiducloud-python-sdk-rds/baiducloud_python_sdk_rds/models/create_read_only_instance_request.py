"""
Request entity for CreateReadOnlyInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_rds.models.billing import Billing
from baiducloud_python_sdk_rds.models.subnet_map import SubnetMap


class CreateReadOnlyInstanceRequest(AbstractModel):
    """
    Request entity for CreateReadOnlyInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        billing,
        source_instance_id,
        cpu_count,
        memory_capacity,
        volume_capacity,
        client_token=None,
        instance_name=None,
        disk_io_type=None,
        zone_names=None,
        vpc_id=None,
        bcm_group_name=None,
        is_direct_pay=None,
        subnets=None,
        ovip=None,
        entry_port=None,
        resource_group_id=None,
        replica_type=None,
        is_inherit_master_authip=None,
        purchase_count=None,
        resource_type=None,
        auto_renew_time_unit=None,
        auto_renew_time=None,
    ):
        """
        Initialize CreateReadOnlyInstanceRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param billing: billing parameter
        :type billing: Billing (required)

        :param source_instance_id: 主实例ID
        :type source_instance_id: str (required)

        :param instance_name: instance_name parameter
        :type instance_name: str (optional)

        :param cpu_count: cpu_count parameter
        :type cpu_count: int (required)

        :param memory_capacity: memory_capacity parameter
        :type memory_capacity: int (required)

        :param volume_capacity: volume_capacity parameter
        :type volume_capacity: int (required)

        :param disk_io_type: disk_io_type parameter
        :type disk_io_type: str (optional)

        :param zone_names: zone_names parameter
        :type zone_names: List[str] (optional)

        :param vpc_id: 与主实例 vpcId 相同
        :type vpc_id: str (optional)

        :param bcm_group_name: bcm 实例组名称
        :type bcm_group_name: str (optional)

        :param is_direct_pay: 是否进行直接支付，默认false，设置为直接支付的变配订单会直接扣款，不需要在走支付逻辑
        :type is_direct_pay: bool (optional)

        :param subnets: subnets parameter
        :type subnets: List[SubnetMap] (optional)

        :param ovip: ovip parameter
        :type ovip: str (optional)

        :param entry_port: entry_port parameter
        :type entry_port: int (optional)

        :param resource_group_id: 资源分组Id。例如：RESG-bKMxbExtnoG
        :type resource_group_id: str (optional)

        :param replica_type: basic表示基础版只读实例，ha表示高可用版只读实例，不传默认basic
        :type replica_type: str (optional)

        :param is_inherit_master_authip: is_inherit_master_authip parameter
        :type is_inherit_master_authip: bool (optional)

        :param purchase_count: 当前购买实例的个数，默认为1 最大为10
        :type purchase_count: int (optional)

        :param resource_type: resource_type parameter
        :type resource_type: str (optional)

        :param auto_renew_time_unit: 自动续费单位（\"year\";\"month\"）
        :type auto_renew_time_unit: str (optional)

        :param auto_renew_time: 自动续费时长（续费单位为year 不大于3，续费单位为month 不大于9）
        :type auto_renew_time: int (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.billing = billing
        self.source_instance_id = source_instance_id
        self.instance_name = instance_name
        self.cpu_count = cpu_count
        self.memory_capacity = memory_capacity
        self.volume_capacity = volume_capacity
        self.disk_io_type = disk_io_type
        self.zone_names = zone_names
        self.vpc_id = vpc_id
        self.bcm_group_name = bcm_group_name
        self.is_direct_pay = is_direct_pay
        self.subnets = subnets
        self.ovip = ovip
        self.entry_port = entry_port
        self.resource_group_id = resource_group_id
        self.replica_type = replica_type
        self.is_inherit_master_authip = is_inherit_master_authip
        self.purchase_count = purchase_count
        self.resource_type = resource_type
        self.auto_renew_time_unit = auto_renew_time_unit
        self.auto_renew_time = auto_renew_time

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
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        if self.source_instance_id is not None:
            result['sourceInstanceId'] = self.source_instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count
        if self.memory_capacity is not None:
            result['memoryCapacity'] = self.memory_capacity
        if self.volume_capacity is not None:
            result['volumeCapacity'] = self.volume_capacity
        if self.disk_io_type is not None:
            result['diskIoType'] = self.disk_io_type
        if self.zone_names is not None:
            result['zoneNames'] = self.zone_names
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.bcm_group_name is not None:
            result['bcmGroupName'] = self.bcm_group_name
        if self.is_direct_pay is not None:
            result['isDirectPay'] = self.is_direct_pay
        if self.subnets is not None:
            result['subnets'] = [i.to_dict() for i in self.subnets]
        if self.ovip is not None:
            result['ovip'] = self.ovip
        if self.entry_port is not None:
            result['entryPort'] = self.entry_port
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.replica_type is not None:
            result['replicaType'] = self.replica_type
        if self.is_inherit_master_authip is not None:
            result['isInheritMasterAuthip'] = self.is_inherit_master_authip
        if self.purchase_count is not None:
            result['purchaseCount'] = self.purchase_count
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.auto_renew_time_unit is not None:
            result['autoRenewTimeUnit'] = self.auto_renew_time_unit
        if self.auto_renew_time is not None:
            result['autoRenewTime'] = self.auto_renew_time
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateReadOnlyInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('sourceInstanceId') is not None:
            self.source_instance_id = m.get('sourceInstanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')
        if m.get('memoryCapacity') is not None:
            self.memory_capacity = m.get('memoryCapacity')
        if m.get('volumeCapacity') is not None:
            self.volume_capacity = m.get('volumeCapacity')
        if m.get('diskIoType') is not None:
            self.disk_io_type = m.get('diskIoType')
        if m.get('zoneNames') is not None:
            self.zone_names = m.get('zoneNames')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('bcmGroupName') is not None:
            self.bcm_group_name = m.get('bcmGroupName')
        if m.get('isDirectPay') is not None:
            self.is_direct_pay = m.get('isDirectPay')
        if m.get('subnets') is not None:
            self.subnets = [SubnetMap().from_dict(i) for i in m.get('subnets')]
        if m.get('ovip') is not None:
            self.ovip = m.get('ovip')
        if m.get('entryPort') is not None:
            self.entry_port = m.get('entryPort')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('replicaType') is not None:
            self.replica_type = m.get('replicaType')
        if m.get('isInheritMasterAuthip') is not None:
            self.is_inherit_master_authip = m.get('isInheritMasterAuthip')
        if m.get('purchaseCount') is not None:
            self.purchase_count = m.get('purchaseCount')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('autoRenewTimeUnit') is not None:
            self.auto_renew_time_unit = m.get('autoRenewTimeUnit')
        if m.get('autoRenewTime') is not None:
            self.auto_renew_time = m.get('autoRenewTime')
        return self
