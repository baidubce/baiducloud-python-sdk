"""
Request entity for CreateAPrimaryInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_rds.models.billing import Billing
from baiducloud_python_sdk_rds.models.subnet_map import SubnetMap
from baiducloud_python_sdk_rds.models.tag import Tag
from baiducloud_python_sdk_rds.models.initial_data_reference import InitialDataReference
from baiducloud_python_sdk_rds.models.recovery_to_source_instance_model import RecoveryToSourceInstanceModel


class CreateAPrimaryInstanceRequest(AbstractModel):
    """
    Request entity for CreateAPrimaryInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        billing,
        engine,
        engine_version,
        cpu_count,
        memory_capacity,
        volume_capacity,
        disk_io_type,
        vpc_id,
        initial_data_reference,
        client_token=None,
        purchase_count=None,
        instance_name=None,
        category=None,
        zone_names=None,
        bcm_group_name=None,
        is_direct_pay=None,
        subnets=None,
        tags=None,
        bgw_group_id=None,
        bgw_group_exclusive=None,
        character_set_name=None,
        auto_renew_time_unit=None,
        auto_renew_time=None,
        lower_case_table_names=None,
        parameter_template_id=None,
        ovip=None,
        entry_port=None,
        replication_type=None,
        resource_group_id=None,
        data=None,
        leader_instance_id=None,
        resource_type=None,
    ):
        """
        Initialize CreateAPrimaryInstanceRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param billing: billing parameter
        :type billing: Billing (required)

        :param purchase_count: 批量创建云数据库 RDS 实例个数, 最大不超过10；默认1
        :type purchase_count: int (optional)

        :param instance_name: instance_name parameter
        :type instance_name: str (optional)

        :param engine: engine parameter
        :type engine: str (required)

        :param engine_version: engine_version parameter
        :type engine_version: str (required)

        :param category: category parameter
        :type category: str (optional)

        :param cpu_count: cpu_count parameter
        :type cpu_count: int (required)

        :param memory_capacity: memory_capacity parameter
        :type memory_capacity: int (required)

        :param volume_capacity: volume_capacity parameter
        :type volume_capacity: int (required)

        :param disk_io_type: disk_io_type parameter
        :type disk_io_type: str (required)

        :param zone_names: zone_names parameter
        :type zone_names: List[str] (optional)

        :param bcm_group_name: 默认为空，代表bcm实例组名称
        :type bcm_group_name: str (optional)

        :param vpc_id: vpc_id parameter
        :type vpc_id: str (required)

        :param is_direct_pay: 是否进行直接支付，默认false，设置为直接支付的变配订单会直接扣款，不需要在走支付逻辑
        :type is_direct_pay: bool (optional)

        :param subnets: subnets parameter
        :type subnets: List[SubnetMap] (optional)

        :param tags: 实例绑定的标签信息
        :type tags: List[Tag] (optional)

        :param bgw_group_id: bgw_group_id parameter
        :type bgw_group_id: str (optional)

        :param bgw_group_exclusive: 负载均衡集群属性，true表示指定专属集群，false表示使用共享集群
        :type bgw_group_exclusive: bool (optional)

        :param character_set_name: character_set_name parameter
        :type character_set_name: str (optional)

        :param auto_renew_time_unit: 自动续费单位（\"year\";\"month\"）
        :type auto_renew_time_unit: str (optional)

        :param auto_renew_time: 自动续费时长（续费单位为year 不大于3，续费单位为month 不大于9）
        :type auto_renew_time: int (optional)

        :param lower_case_table_names: 表名是否区分大小写。默认为0，表示大小写敏感，区分大小写；传1表示不区分大小写
        :type lower_case_table_names: int (optional)

        :param parameter_template_id: 参数模板ID
        :type parameter_template_id: str (optional)

        :param ovip: ovip parameter
        :type ovip: str (optional)

        :param entry_port: entry_port parameter
        :type entry_port: int (optional)

        :param replication_type: 数据复制方式。异步复制：async，半同步复制：semi\\_sync
        :type replication_type: str (optional)

        :param resource_group_id: 资源分组ID。例如：RESG-bKMxbExtnoG
        :type resource_group_id: str (optional)

        :param initial_data_reference: initial_data_reference parameter
        :type initial_data_reference: InitialDataReference (required)

        :param data: 库表恢复到新实例，恢复的库表信息
        :type data: List[RecoveryToSourceInstanceModel] (optional)

        :param leader_instance_id: leader_instance_id parameter
        :type leader_instance_id: str (optional)

        :param resource_type: resource_type parameter
        :type resource_type: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.billing = billing
        self.purchase_count = purchase_count
        self.instance_name = instance_name
        self.engine = engine
        self.engine_version = engine_version
        self.category = category
        self.cpu_count = cpu_count
        self.memory_capacity = memory_capacity
        self.volume_capacity = volume_capacity
        self.disk_io_type = disk_io_type
        self.zone_names = zone_names
        self.bcm_group_name = bcm_group_name
        self.vpc_id = vpc_id
        self.is_direct_pay = is_direct_pay
        self.subnets = subnets
        self.tags = tags
        self.bgw_group_id = bgw_group_id
        self.bgw_group_exclusive = bgw_group_exclusive
        self.character_set_name = character_set_name
        self.auto_renew_time_unit = auto_renew_time_unit
        self.auto_renew_time = auto_renew_time
        self.lower_case_table_names = lower_case_table_names
        self.parameter_template_id = parameter_template_id
        self.ovip = ovip
        self.entry_port = entry_port
        self.replication_type = replication_type
        self.resource_group_id = resource_group_id
        self.initial_data_reference = initial_data_reference
        self.data = data
        self.leader_instance_id = leader_instance_id
        self.resource_type = resource_type

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
        if self.purchase_count is not None:
            result['purchaseCount'] = self.purchase_count
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.engine is not None:
            result['engine'] = self.engine
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.category is not None:
            result['category'] = self.category
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
        if self.bcm_group_name is not None:
            result['bcmGroupName'] = self.bcm_group_name
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.is_direct_pay is not None:
            result['isDirectPay'] = self.is_direct_pay
        if self.subnets is not None:
            result['subnets'] = [i.to_dict() for i in self.subnets]
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.bgw_group_id is not None:
            result['bgwGroupId'] = self.bgw_group_id
        if self.bgw_group_exclusive is not None:
            result['bgwGroupExclusive'] = self.bgw_group_exclusive
        if self.character_set_name is not None:
            result['characterSetName'] = self.character_set_name
        if self.auto_renew_time_unit is not None:
            result['autoRenewTimeUnit'] = self.auto_renew_time_unit
        if self.auto_renew_time is not None:
            result['autoRenewTime'] = self.auto_renew_time
        if self.lower_case_table_names is not None:
            result['lowerCaseTableNames'] = self.lower_case_table_names
        if self.parameter_template_id is not None:
            result['parameterTemplateId'] = self.parameter_template_id
        if self.ovip is not None:
            result['ovip'] = self.ovip
        if self.entry_port is not None:
            result['entryPort'] = self.entry_port
        if self.replication_type is not None:
            result['replicationType'] = self.replication_type
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.initial_data_reference is not None:
            result['initialDataReference'] = self.initial_data_reference.to_dict()
        if self.data is not None:
            result['data'] = [i.to_dict() for i in self.data]
        if self.leader_instance_id is not None:
            result['leaderInstanceId'] = self.leader_instance_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAPrimaryInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('purchaseCount') is not None:
            self.purchase_count = m.get('purchaseCount')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('engine') is not None:
            self.engine = m.get('engine')
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('category') is not None:
            self.category = m.get('category')
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
        if m.get('bcmGroupName') is not None:
            self.bcm_group_name = m.get('bcmGroupName')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('isDirectPay') is not None:
            self.is_direct_pay = m.get('isDirectPay')
        if m.get('subnets') is not None:
            self.subnets = [SubnetMap().from_dict(i) for i in m.get('subnets')]
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('bgwGroupId') is not None:
            self.bgw_group_id = m.get('bgwGroupId')
        if m.get('bgwGroupExclusive') is not None:
            self.bgw_group_exclusive = m.get('bgwGroupExclusive')
        if m.get('characterSetName') is not None:
            self.character_set_name = m.get('characterSetName')
        if m.get('autoRenewTimeUnit') is not None:
            self.auto_renew_time_unit = m.get('autoRenewTimeUnit')
        if m.get('autoRenewTime') is not None:
            self.auto_renew_time = m.get('autoRenewTime')
        if m.get('lowerCaseTableNames') is not None:
            self.lower_case_table_names = m.get('lowerCaseTableNames')
        if m.get('parameterTemplateId') is not None:
            self.parameter_template_id = m.get('parameterTemplateId')
        if m.get('ovip') is not None:
            self.ovip = m.get('ovip')
        if m.get('entryPort') is not None:
            self.entry_port = m.get('entryPort')
        if m.get('replicationType') is not None:
            self.replication_type = m.get('replicationType')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('initialDataReference') is not None:
            self.initial_data_reference = InitialDataReference().from_dict(m.get('initialDataReference'))
        if m.get('data') is not None:
            self.data = [RecoveryToSourceInstanceModel().from_dict(i) for i in m.get('data')]
        if m.get('leaderInstanceId') is not None:
            self.leader_instance_id = m.get('leaderInstanceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self
