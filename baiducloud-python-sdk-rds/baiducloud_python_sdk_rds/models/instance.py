"""
Instance information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rds.models.endpoint import Endpoint

from baiducloud_python_sdk_rds.models.snapshot_policy import SnapshotPolicy

from baiducloud_python_sdk_rds.models.blb_service import BlbService

from baiducloud_python_sdk_rds.models.topology import Topology

from baiducloud_python_sdk_rds.models.dcc_host_info import DccHostInfo

from baiducloud_python_sdk_rds.models.role_info import RoleInfo

from baiducloud_python_sdk_rds.models.role_info import RoleInfo

from baiducloud_python_sdk_rds.models.role_info import RoleInfo

from baiducloud_python_sdk_rds.models.role_info import RoleInfo

from baiducloud_python_sdk_rds.models.ro_group import RoGroup

from baiducloud_python_sdk_rds.models.role_info import RoleInfo

from baiducloud_python_sdk_rds.models.role_info import RoleInfo

from baiducloud_python_sdk_rds.models.tag import Tag

from baiducloud_python_sdk_rds.models.machine_po import MachinePO

from baiducloud_python_sdk_rds.models.resource_groups_detail_full import ResourceGroupsDetailFull


class Instance(AbstractModel):
    """
    Instance
    """

    def __init__(
        self,
        instance_id=None,
        instance_short_id=None,
        instance_name=None,
        engine=None,
        engine_version=None,
        rds_minor_version=None,
        character_set_name=None,
        endpoint=None,
        instance_class=None,
        allocated_memory_in_mb=None,
        allocated_memory_in_gb=None,
        memory_capacity=None,
        allocated_storage_in_gb=None,
        volume_capacity=None,
        total_storage_in_gb=None,
        used_storage_in_mb=None,
        used_storage_in_gb=None,
        used_storage=None,
        cpu_count=None,
        instance_type=None,
        source_instance_id=None,
        read_replica_num=None,
        read_replica=None,
        instance_status=None,
        lock_mode=None,
        eip_status=None,
        public_access_status=None,
        super_user_flag=None,
        replication_type=None,
        sync_mode=None,
        sqlserver_br_type=None,
        backup_policy=None,
        blb_service=None,
        publicly_accessible=None,
        instance_create_time=None,
        instance_expire_time=None,
        product_type=None,
        payment_timing=None,
        topology=None,
        azone=None,
        vpc_id=None,
        subnet_id=None,
        physical_zone=None,
        region=None,
        source_region=None,
        billing_status=None,
        application_type=None,
        node_amount=None,
        old_instance=None,
        online_status=None,
        is_single=None,
        dcc_host_ids=None,
        machine_type=None,
        weight=None,
        node_type=None,
        repair_start_time=None,
        repair_end_time=None,
        quot_status=None,
        node_read_replica=None,
        node_master=None,
        node_slave=None,
        node_proxy=None,
        disk_io_type=None,
        group_id=None,
        group_name=None,
        tde_status=None,
        user_id=None,
        bgw_group_id=None,
        bgw_group_exclusive=None,
        ro_group_list=None,
        ro_group_abnormal=None,
        disk_type=None,
        cds_type=None,
        maintain_start_time=None,
        maintain_duration=None,
        maintain_period=None,
        instance_sub_status=None,
        bcm_send_cycle=None,
        auto_resize_disk=None,
        auto_resize_cpu=None,
        edge_region=None,
        edge_region_name=None,
        edge_vpc_id=None,
        edge_subnet_id=None,
        gtid_type=None,
        node_master_read_replica=None,
        node_backup_read_replica=None,
        ha_strategy=None,
        is_dbrs_enable=None,
        replica_type=None,
        resource_type=None,
        cds_encrypt=None,
        cds_encrypt_key=None,
        resource_platform=None,
        location=None,
        has_slave=None,
        expire_date=None,
        has_proxy=None,
        vpc_name=None,
        resource_uuid=None,
        tags=None,
        task=None,
        order_status=None,
        vpc_cidr=None,
        zone_names=None,
        dcc_hosts=None,
        category=None,
        name=None,
        resource_group=None,
        resource_group_id=None,
        resource_group_name=None,
        is_charge_proxy=None,
        single=None,
    ):
        """
        Initialize Instance instance.

        :param instance_id: 实例ID
        :type instance_id: str (optional)

        :param instance_short_id: 实例短ID
        :type instance_short_id: str (optional)

        :param instance_name: 实例名称
        :type instance_name: str (optional)

        :param engine: engine attribute
        :type engine: str (optional)

        :param engine_version: engine_version attribute
        :type engine_version: str (optional)

        :param rds_minor_version: 实例小版本
        :type rds_minor_version: str (optional)

        :param character_set_name: character_set_name attribute
        :type character_set_name: str (optional)

        :param endpoint: endpoint attribute
        :type endpoint: Endpoint (optional)

        :param instance_class: 实例分类 。MASTER(主实例)，REPLICA（只读实例）,PROXY（代理实例）
        :type instance_class: str (optional)

        :param allocated_memory_in_mb: 分配内大小（单位：MB）
        :type allocated_memory_in_mb: int (optional)

        :param allocated_memory_in_gb: 分配内存大小（单位：GB）
        :type allocated_memory_in_gb: float (optional)

        :param memory_capacity: 实例内存（单位：GB）
        :type memory_capacity: float (optional)

        :param allocated_storage_in_gb: 分配存储存空间（单位：GB）
        :type allocated_storage_in_gb: int (optional)

        :param volume_capacity: 存储空间（单位：GB）
        :type volume_capacity: int (optional)

        :param total_storage_in_gb: 磁盘总大小（单位：GB）
        :type total_storage_in_gb: int (optional)

        :param used_storage_in_mb: 已经使用存储空间（单位：MB）
        :type used_storage_in_mb: int (optional)

        :param used_storage_in_gb: 已经使用存储空间（单位GB）
        :type used_storage_in_gb: float (optional)

        :param used_storage: 已用存储空间（单位GB）
        :type used_storage: float (optional)

        :param cpu_count: CPU核数
        :type cpu_count: int (optional)

        :param instance_type: instance_type attribute
        :type instance_type: str (optional)

        :param source_instance_id: 主实例ID，如果为主实例则为空
        :type source_instance_id: str (optional)

        :param read_replica_num: 只读实例数量
        :type read_replica_num: int (optional)

        :param read_replica: 只读实例名称的集合
        :type read_replica: List[str] (optional)

        :param instance_status: instance_status attribute
        :type instance_status: str (optional)

        :param lock_mode: lock_mode attribute
        :type lock_mode: str (optional)

        :param eip_status: eip_status attribute
        :type eip_status: str (optional)

        :param public_access_status: public_access_status attribute
        :type public_access_status: str (optional)

        :param super_user_flag: 账号权限类型，取值是super或common super：读写账号  common：只读账号
        :type super_user_flag: str (optional)

        :param replication_type: 数据复制方式： async：异步复制 semi\\_sync：半同步复制
        :type replication_type: str (optional)

        :param sync_mode: sync_mode attribute
        :type sync_mode: str (optional)

        :param sqlserver_br_type: SQLServer备份恢复类型，非SQLServer实例返回null
        :type sqlserver_br_type: str (optional)

        :param backup_policy: backup_policy attribute
        :type backup_policy: SnapshotPolicy (optional)

        :param blb_service: blb_service attribute
        :type blb_service: BlbService (optional)

        :param publicly_accessible: 是否可访问公网， true 可以，false不可以
        :type publicly_accessible: bool (optional)

        :param instance_create_time: instance_create_time attribute
        :type instance_create_time: datetime (optional)

        :param instance_expire_time: instance_expire_time attribute
        :type instance_expire_time: datetime (optional)

        :param product_type: 付费方式，预付费：postpay，后付费：prepay
        :type product_type: str (optional)

        :param payment_timing: 付费方式， 预付费：Prepaid，后付费：Postpaid
        :type payment_timing: str (optional)

        :param topology: topology attribute
        :type topology: Topology (optional)

        :param azone: 实例的逻辑可用区名字 ,多个逗号分隔。如：zoneD,zoneE
        :type azone: str (optional)

        :param vpc_id: 实例所属VPC的ID
        :type vpc_id: str (optional)

        :param subnet_id: subnet_id attribute
        :type subnet_id: Dict[str, str] (optional)

        :param physical_zone: 实例所在物理可用区信息，格式为 {zone: 值}
        :type physical_zone: Dict[str, str] (optional)

        :param region: 该实例的地域首字母。如bj
        :type region: str (optional)

        :param source_region: 该实例的主实例的区域。如bj
        :type source_region: str (optional)

        :param billing_status: billing_status attribute
        :type billing_status: str (optional)

        :param application_type: 所属系列，single：单机基础版，normal：双机高可用版
        :type application_type: str (optional)

        :param node_amount: 节点数（代理实例）
        :type node_amount: int (optional)

        :param old_instance: 旧实例数量
        :type old_instance: int (optional)

        :param online_status: 在线状态，0：下线、1：上线
        :type online_status: int (optional)

        :param is_single: 是否单机实例，true：是，false：否
        :type is_single: bool (optional)

        :param dcc_host_ids: dcc_host_ids attribute
        :type dcc_host_ids: DccHostInfo (optional)

        :param machine_type: 主机类型，默认只有dcc
        :type machine_type: str (optional)

        :param weight: 权重
        :type weight: int (optional)

        :param node_type: 节点类型,默认为空，没有返回值
        :type node_type: str (optional)

        :param repair_start_time: repair_start_time attribute
        :type repair_start_time: datetime (optional)

        :param repair_end_time: repair_end_time attribute
        :type repair_end_time: datetime (optional)

        :param quot_status: 分配状态： pendingRepair（待分配） processing（分配中） solved（已分配）
        :type quot_status: str (optional)

        :param node_read_replica: node_read_replica attribute
        :type node_read_replica: RoleInfo (optional)

        :param node_master: node_master attribute
        :type node_master: RoleInfo (optional)

        :param node_slave: node_slave attribute
        :type node_slave: RoleInfo (optional)

        :param node_proxy: node_proxy attribute
        :type node_proxy: RoleInfo (optional)

        :param disk_io_type: disk_io_type attribute
        :type disk_io_type: str (optional)

        :param group_id: 分组ID
        :type group_id: str (optional)

        :param group_name: 分组名称
        :type group_name: str (optional)

        :param tde_status: 透明数据加密状态：close：（关闭）、open（打开）
        :type tde_status: str (optional)

        :param user_id: 用户ID
        :type user_id: str (optional)

        :param bgw_group_id: bgw_group_id attribute
        :type bgw_group_id: str (optional)

        :param bgw_group_exclusive: 负载均衡集群属性，true表示指定专属集群，false表示使用共享集群。
        :type bgw_group_exclusive: bool (optional)

        :param ro_group_list: 只读组列表
        :type ro_group_list: List[RoGroup] (optional)

        :param ro_group_abnormal: 是否为异常只读组。true：是，false：不是；默认是false
        :type ro_group_abnormal: bool (optional)

        :param disk_type: disk_type attribute
        :type disk_type: str (optional)

        :param cds_type: cds_type attribute
        :type cds_type: str (optional)

        :param maintain_start_time: 维护时间窗口
        :type maintain_start_time: str (optional)

        :param maintain_duration: 维护时间窗口时长（单位:小时）
        :type maintain_duration: int (optional)

        :param maintain_period: 维护时间窗口的持续时间
        :type maintain_period: str (optional)

        :param instance_sub_status: instance_sub_status attribute
        :type instance_sub_status: str (optional)

        :param bcm_send_cycle: 监控数据发送周期（单位：分钟）
        :type bcm_send_cycle: str (optional)

        :param auto_resize_disk: 自动扩容磁盘大小（单位：GB）
        :type auto_resize_disk: int (optional)

        :param auto_resize_cpu: 自动扩容CPU核数
        :type auto_resize_cpu: int (optional)

        :param edge_region: 边缘区域
        :type edge_region: str (optional)

        :param edge_region_name: 边缘区域名称
        :type edge_region_name: str (optional)

        :param edge_vpc_id: 边缘 VpcID
        :type edge_vpc_id: str (optional)

        :param edge_subnet_id: 边缘子网ID
        :type edge_subnet_id: str (optional)

        :param gtid_type: GTID模式类型
        :type gtid_type: int (optional)

        :param node_master_read_replica: node_master_read_replica attribute
        :type node_master_read_replica: RoleInfo (optional)

        :param node_backup_read_replica: node_backup_read_replica attribute
        :type node_backup_read_replica: RoleInfo (optional)

        :param ha_strategy: 高可用切换策略。0：立即切换，1：维护时间切换
        :type ha_strategy: int (optional)

        :param is_dbrs_enable: 是否开启数据库回收站功能
        :type is_dbrs_enable: bool (optional)

        :param replica_type: 副本类型
        :type replica_type: str (optional)

        :param resource_type: 资源类型，如shared（共享）
        :type resource_type: str (optional)

        :param cds_encrypt: 云磁盘是否加密。0：否
        :type cds_encrypt: int (optional)

        :param cds_encrypt_key: 云磁盘加密密钥ID
        :type cds_encrypt_key: str (optional)

        :param resource_platform: 资源平台
        :type resource_platform: str (optional)

        :param location: 区域位置
        :type location: str (optional)

        :param has_slave: 是否有从节，true：有、false：没有；默认是false
        :type has_slave: bool (optional)

        :param expire_date: 过期日期，默认是0
        :type expire_date: int (optional)

        :param has_proxy: 是否有代理，true：有、false：没有；默认是false
        :type has_proxy: bool (optional)

        :param vpc_name: vpc名称
        :type vpc_name: str (optional)

        :param resource_uuid: 资源，唯一序列ID
        :type resource_uuid: str (optional)

        :param tags: 分组标签
        :type tags: List[Tag] (optional)

        :param task: 相关任务， 如自动续费（目前只有这个）
        :type task: str (optional)

        :param order_status: 相关联的计费变更订单的类型to\\_prepay、 to\\_postpay两种
        :type order_status: str (optional)

        :param vpc_cidr: VPC的IP地址及子网掩码
        :type vpc_cidr: str (optional)

        :param zone_names: 实例的可用区名称，数组列表
        :type zone_names: List[str] (optional)

        :param dcc_hosts: dcc主机对象
        :type dcc_hosts: List[MachinePO] (optional)

        :param category: 所属系列。Singleton：单机基础版，null：双机高可用版
        :type category: str (optional)

        :param name: 实例名称，只给iam的实例列表接口使用，其他接口不要用
        :type name: str (optional)

        :param resource_group: resource_group attribute
        :type resource_group: ResourceGroupsDetailFull (optional)

        :param resource_group_id: 资源分组ID
        :type resource_group_id: str (optional)

        :param resource_group_name: 资源分组名称
        :type resource_group_name: str (optional)

        :param is_charge_proxy: 是否对代理节点计费
        :type is_charge_proxy: bool (optional)

        :param single: 是否单机实例（内部字段）
        :type single: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.instance_short_id = instance_short_id
        self.instance_name = instance_name
        self.engine = engine
        self.engine_version = engine_version
        self.rds_minor_version = rds_minor_version
        self.character_set_name = character_set_name
        self.endpoint = endpoint
        self.instance_class = instance_class
        self.allocated_memory_in_mb = allocated_memory_in_mb
        self.allocated_memory_in_gb = allocated_memory_in_gb
        self.memory_capacity = memory_capacity
        self.allocated_storage_in_gb = allocated_storage_in_gb
        self.volume_capacity = volume_capacity
        self.total_storage_in_gb = total_storage_in_gb
        self.used_storage_in_mb = used_storage_in_mb
        self.used_storage_in_gb = used_storage_in_gb
        self.used_storage = used_storage
        self.cpu_count = cpu_count
        self.instance_type = instance_type
        self.source_instance_id = source_instance_id
        self.read_replica_num = read_replica_num
        self.read_replica = read_replica
        self.instance_status = instance_status
        self.lock_mode = lock_mode
        self.eip_status = eip_status
        self.public_access_status = public_access_status
        self.super_user_flag = super_user_flag
        self.replication_type = replication_type
        self.sync_mode = sync_mode
        self.sqlserver_br_type = sqlserver_br_type
        self.backup_policy = backup_policy
        self.blb_service = blb_service
        self.publicly_accessible = publicly_accessible
        self.instance_create_time = instance_create_time
        self.instance_expire_time = instance_expire_time
        self.product_type = product_type
        self.payment_timing = payment_timing
        self.topology = topology
        self.azone = azone
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.physical_zone = physical_zone
        self.region = region
        self.source_region = source_region
        self.billing_status = billing_status
        self.application_type = application_type
        self.node_amount = node_amount
        self.old_instance = old_instance
        self.online_status = online_status
        self.is_single = is_single
        self.dcc_host_ids = dcc_host_ids
        self.machine_type = machine_type
        self.weight = weight
        self.node_type = node_type
        self.repair_start_time = repair_start_time
        self.repair_end_time = repair_end_time
        self.quot_status = quot_status
        self.node_read_replica = node_read_replica
        self.node_master = node_master
        self.node_slave = node_slave
        self.node_proxy = node_proxy
        self.disk_io_type = disk_io_type
        self.group_id = group_id
        self.group_name = group_name
        self.tde_status = tde_status
        self.user_id = user_id
        self.bgw_group_id = bgw_group_id
        self.bgw_group_exclusive = bgw_group_exclusive
        self.ro_group_list = ro_group_list
        self.ro_group_abnormal = ro_group_abnormal
        self.disk_type = disk_type
        self.cds_type = cds_type
        self.maintain_start_time = maintain_start_time
        self.maintain_duration = maintain_duration
        self.maintain_period = maintain_period
        self.instance_sub_status = instance_sub_status
        self.bcm_send_cycle = bcm_send_cycle
        self.auto_resize_disk = auto_resize_disk
        self.auto_resize_cpu = auto_resize_cpu
        self.edge_region = edge_region
        self.edge_region_name = edge_region_name
        self.edge_vpc_id = edge_vpc_id
        self.edge_subnet_id = edge_subnet_id
        self.gtid_type = gtid_type
        self.node_master_read_replica = node_master_read_replica
        self.node_backup_read_replica = node_backup_read_replica
        self.ha_strategy = ha_strategy
        self.is_dbrs_enable = is_dbrs_enable
        self.replica_type = replica_type
        self.resource_type = resource_type
        self.cds_encrypt = cds_encrypt
        self.cds_encrypt_key = cds_encrypt_key
        self.resource_platform = resource_platform
        self.location = location
        self.has_slave = has_slave
        self.expire_date = expire_date
        self.has_proxy = has_proxy
        self.vpc_name = vpc_name
        self.resource_uuid = resource_uuid
        self.tags = tags
        self.task = task
        self.order_status = order_status
        self.vpc_cidr = vpc_cidr
        self.zone_names = zone_names
        self.dcc_hosts = dcc_hosts
        self.category = category
        self.name = name
        self.resource_group = resource_group
        self.resource_group_id = resource_group_id
        self.resource_group_name = resource_group_name
        self.is_charge_proxy = is_charge_proxy
        self.single = single

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
        if self.instance_short_id is not None:
            result['instanceShortId'] = self.instance_short_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.engine is not None:
            result['engine'] = self.engine
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.rds_minor_version is not None:
            result['rdsMinorVersion'] = self.rds_minor_version
        if self.character_set_name is not None:
            result['characterSetName'] = self.character_set_name
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint.to_dict()
        if self.instance_class is not None:
            result['instanceClass'] = self.instance_class
        if self.allocated_memory_in_mb is not None:
            result['allocatedMemoryInMB'] = self.allocated_memory_in_mb
        if self.allocated_memory_in_gb is not None:
            result['allocatedMemoryInGB'] = self.allocated_memory_in_gb
        if self.memory_capacity is not None:
            result['memoryCapacity'] = self.memory_capacity
        if self.allocated_storage_in_gb is not None:
            result['allocatedStorageInGB'] = self.allocated_storage_in_gb
        if self.volume_capacity is not None:
            result['volumeCapacity'] = self.volume_capacity
        if self.total_storage_in_gb is not None:
            result['totalStorageInGB'] = self.total_storage_in_gb
        if self.used_storage_in_mb is not None:
            result['usedStorageInMB'] = self.used_storage_in_mb
        if self.used_storage_in_gb is not None:
            result['usedStorageInGB'] = self.used_storage_in_gb
        if self.used_storage is not None:
            result['usedStorage'] = self.used_storage
        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.source_instance_id is not None:
            result['sourceInstanceId'] = self.source_instance_id
        if self.read_replica_num is not None:
            result['readReplicaNum'] = self.read_replica_num
        if self.read_replica is not None:
            result['readReplica'] = self.read_replica
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.eip_status is not None:
            result['eipStatus'] = self.eip_status
        if self.public_access_status is not None:
            result['publicAccessStatus'] = self.public_access_status
        if self.super_user_flag is not None:
            result['superUserFlag'] = self.super_user_flag
        if self.replication_type is not None:
            result['replicationType'] = self.replication_type
        if self.sync_mode is not None:
            result['syncMode'] = self.sync_mode
        if self.sqlserver_br_type is not None:
            result['sqlserverBrType'] = self.sqlserver_br_type
        if self.backup_policy is not None:
            result['backupPolicy'] = self.backup_policy.to_dict()
        if self.blb_service is not None:
            result['blbService'] = self.blb_service.to_dict()
        if self.publicly_accessible is not None:
            result['publiclyAccessible'] = self.publicly_accessible
        if self.instance_create_time is not None:
            result['instanceCreateTime'] = self.instance_create_time
        if self.instance_expire_time is not None:
            result['instanceExpireTime'] = self.instance_expire_time
        if self.product_type is not None:
            result['productType'] = self.product_type
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.topology is not None:
            result['topology'] = self.topology.to_dict()
        if self.azone is not None:
            result['azone'] = self.azone
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.physical_zone is not None:
            result['physicalZone'] = self.physical_zone
        if self.region is not None:
            result['region'] = self.region
        if self.source_region is not None:
            result['sourceRegion'] = self.source_region
        if self.billing_status is not None:
            result['billingStatus'] = self.billing_status
        if self.application_type is not None:
            result['applicationType'] = self.application_type
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.old_instance is not None:
            result['oldInstance'] = self.old_instance
        if self.online_status is not None:
            result['onlineStatus'] = self.online_status
        if self.is_single is not None:
            result['isSingle'] = self.is_single
        if self.dcc_host_ids is not None:
            result['dccHostIds'] = self.dcc_host_ids.to_dict()
        if self.machine_type is not None:
            result['machineType'] = self.machine_type
        if self.weight is not None:
            result['weight'] = self.weight
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.repair_start_time is not None:
            result['repairStartTime'] = self.repair_start_time
        if self.repair_end_time is not None:
            result['repairEndTime'] = self.repair_end_time
        if self.quot_status is not None:
            result['quotStatus'] = self.quot_status
        if self.node_read_replica is not None:
            result['nodeReadReplica'] = self.node_read_replica.to_dict()
        if self.node_master is not None:
            result['nodeMaster'] = self.node_master.to_dict()
        if self.node_slave is not None:
            result['nodeSlave'] = self.node_slave.to_dict()
        if self.node_proxy is not None:
            result['nodeProxy'] = self.node_proxy.to_dict()
        if self.disk_io_type is not None:
            result['diskIoType'] = self.disk_io_type
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.tde_status is not None:
            result['tdeStatus'] = self.tde_status
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.bgw_group_id is not None:
            result['bgwGroupId'] = self.bgw_group_id
        if self.bgw_group_exclusive is not None:
            result['bgwGroupExclusive'] = self.bgw_group_exclusive
        if self.ro_group_list is not None:
            result['roGroupList'] = [i.to_dict() for i in self.ro_group_list]
        if self.ro_group_abnormal is not None:
            result['roGroupAbnormal'] = self.ro_group_abnormal
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.cds_type is not None:
            result['cdsType'] = self.cds_type
        if self.maintain_start_time is not None:
            result['maintainStartTime'] = self.maintain_start_time
        if self.maintain_duration is not None:
            result['maintainDuration'] = self.maintain_duration
        if self.maintain_period is not None:
            result['maintainPeriod'] = self.maintain_period
        if self.instance_sub_status is not None:
            result['instanceSubStatus'] = self.instance_sub_status
        if self.bcm_send_cycle is not None:
            result['bcmSendCycle'] = self.bcm_send_cycle
        if self.auto_resize_disk is not None:
            result['autoResizeDisk'] = self.auto_resize_disk
        if self.auto_resize_cpu is not None:
            result['autoResizeCpu'] = self.auto_resize_cpu
        if self.edge_region is not None:
            result['edgeRegion'] = self.edge_region
        if self.edge_region_name is not None:
            result['edgeRegionName'] = self.edge_region_name
        if self.edge_vpc_id is not None:
            result['edgeVpcId'] = self.edge_vpc_id
        if self.edge_subnet_id is not None:
            result['edgeSubnetId'] = self.edge_subnet_id
        if self.gtid_type is not None:
            result['gtidType'] = self.gtid_type
        if self.node_master_read_replica is not None:
            result['nodeMasterReadReplica'] = self.node_master_read_replica.to_dict()
        if self.node_backup_read_replica is not None:
            result['nodeBackupReadReplica'] = self.node_backup_read_replica.to_dict()
        if self.ha_strategy is not None:
            result['haStrategy'] = self.ha_strategy
        if self.is_dbrs_enable is not None:
            result['isDBRSEnable'] = self.is_dbrs_enable
        if self.replica_type is not None:
            result['replicaType'] = self.replica_type
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.cds_encrypt is not None:
            result['cdsEncrypt'] = self.cds_encrypt
        if self.cds_encrypt_key is not None:
            result['cdsEncryptKey'] = self.cds_encrypt_key
        if self.resource_platform is not None:
            result['resourcePlatform'] = self.resource_platform
        if self.location is not None:
            result['location'] = self.location
        if self.has_slave is not None:
            result['hasSlave'] = self.has_slave
        if self.expire_date is not None:
            result['expireDate'] = self.expire_date
        if self.has_proxy is not None:
            result['hasProxy'] = self.has_proxy
        if self.vpc_name is not None:
            result['vpcName'] = self.vpc_name
        if self.resource_uuid is not None:
            result['resourceUuid'] = self.resource_uuid
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.task is not None:
            result['task'] = self.task
        if self.order_status is not None:
            result['orderStatus'] = self.order_status
        if self.vpc_cidr is not None:
            result['vpcCidr'] = self.vpc_cidr
        if self.zone_names is not None:
            result['zoneNames'] = self.zone_names
        if self.dcc_hosts is not None:
            result['dccHosts'] = [i.to_dict() for i in self.dcc_hosts]
        if self.category is not None:
            result['category'] = self.category
        if self.name is not None:
            result['name'] = self.name
        if self.resource_group is not None:
            result['resourceGroup'] = self.resource_group.to_dict()
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.resource_group_name is not None:
            result['resourceGroupName'] = self.resource_group_name
        if self.is_charge_proxy is not None:
            result['isChargeProxy'] = self.is_charge_proxy
        if self.single is not None:
            result['single'] = self.single
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Instance

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceShortId') is not None:
            self.instance_short_id = m.get('instanceShortId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('engine') is not None:
            self.engine = m.get('engine')
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('rdsMinorVersion') is not None:
            self.rds_minor_version = m.get('rdsMinorVersion')
        if m.get('characterSetName') is not None:
            self.character_set_name = m.get('characterSetName')
        if m.get('endpoint') is not None:
            self.endpoint = Endpoint().from_dict(m.get('endpoint'))
        if m.get('instanceClass') is not None:
            self.instance_class = m.get('instanceClass')
        if m.get('allocatedMemoryInMB') is not None:
            self.allocated_memory_in_mb = m.get('allocatedMemoryInMB')
        if m.get('allocatedMemoryInGB') is not None:
            self.allocated_memory_in_gb = m.get('allocatedMemoryInGB')
        if m.get('memoryCapacity') is not None:
            self.memory_capacity = m.get('memoryCapacity')
        if m.get('allocatedStorageInGB') is not None:
            self.allocated_storage_in_gb = m.get('allocatedStorageInGB')
        if m.get('volumeCapacity') is not None:
            self.volume_capacity = m.get('volumeCapacity')
        if m.get('totalStorageInGB') is not None:
            self.total_storage_in_gb = m.get('totalStorageInGB')
        if m.get('usedStorageInMB') is not None:
            self.used_storage_in_mb = m.get('usedStorageInMB')
        if m.get('usedStorageInGB') is not None:
            self.used_storage_in_gb = m.get('usedStorageInGB')
        if m.get('usedStorage') is not None:
            self.used_storage = m.get('usedStorage')
        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('sourceInstanceId') is not None:
            self.source_instance_id = m.get('sourceInstanceId')
        if m.get('readReplicaNum') is not None:
            self.read_replica_num = m.get('readReplicaNum')
        if m.get('readReplica') is not None:
            self.read_replica = m.get('readReplica')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('eipStatus') is not None:
            self.eip_status = m.get('eipStatus')
        if m.get('publicAccessStatus') is not None:
            self.public_access_status = m.get('publicAccessStatus')
        if m.get('superUserFlag') is not None:
            self.super_user_flag = m.get('superUserFlag')
        if m.get('replicationType') is not None:
            self.replication_type = m.get('replicationType')
        if m.get('syncMode') is not None:
            self.sync_mode = m.get('syncMode')
        if m.get('sqlserverBrType') is not None:
            self.sqlserver_br_type = m.get('sqlserverBrType')
        if m.get('backupPolicy') is not None:
            self.backup_policy = SnapshotPolicy().from_dict(m.get('backupPolicy'))
        if m.get('blbService') is not None:
            self.blb_service = BlbService().from_dict(m.get('blbService'))
        if m.get('publiclyAccessible') is not None:
            self.publicly_accessible = m.get('publiclyAccessible')
        if m.get('instanceCreateTime') is not None:
            self.instance_create_time = m.get('instanceCreateTime')
        if m.get('instanceExpireTime') is not None:
            self.instance_expire_time = m.get('instanceExpireTime')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('topology') is not None:
            self.topology = Topology().from_dict(m.get('topology'))
        if m.get('azone') is not None:
            self.azone = m.get('azone')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('physicalZone') is not None:
            self.physical_zone = m.get('physicalZone')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('sourceRegion') is not None:
            self.source_region = m.get('sourceRegion')
        if m.get('billingStatus') is not None:
            self.billing_status = m.get('billingStatus')
        if m.get('applicationType') is not None:
            self.application_type = m.get('applicationType')
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('oldInstance') is not None:
            self.old_instance = m.get('oldInstance')
        if m.get('onlineStatus') is not None:
            self.online_status = m.get('onlineStatus')
        if m.get('isSingle') is not None:
            self.is_single = m.get('isSingle')
        if m.get('dccHostIds') is not None:
            self.dcc_host_ids = DccHostInfo().from_dict(m.get('dccHostIds'))
        if m.get('machineType') is not None:
            self.machine_type = m.get('machineType')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('repairStartTime') is not None:
            self.repair_start_time = m.get('repairStartTime')
        if m.get('repairEndTime') is not None:
            self.repair_end_time = m.get('repairEndTime')
        if m.get('quotStatus') is not None:
            self.quot_status = m.get('quotStatus')
        if m.get('nodeReadReplica') is not None:
            self.node_read_replica = RoleInfo().from_dict(m.get('nodeReadReplica'))
        if m.get('nodeMaster') is not None:
            self.node_master = RoleInfo().from_dict(m.get('nodeMaster'))
        if m.get('nodeSlave') is not None:
            self.node_slave = RoleInfo().from_dict(m.get('nodeSlave'))
        if m.get('nodeProxy') is not None:
            self.node_proxy = RoleInfo().from_dict(m.get('nodeProxy'))
        if m.get('diskIoType') is not None:
            self.disk_io_type = m.get('diskIoType')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('tdeStatus') is not None:
            self.tde_status = m.get('tdeStatus')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('bgwGroupId') is not None:
            self.bgw_group_id = m.get('bgwGroupId')
        if m.get('bgwGroupExclusive') is not None:
            self.bgw_group_exclusive = m.get('bgwGroupExclusive')
        if m.get('roGroupList') is not None:
            self.ro_group_list = [RoGroup().from_dict(i) for i in m.get('roGroupList')]
        if m.get('roGroupAbnormal') is not None:
            self.ro_group_abnormal = m.get('roGroupAbnormal')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('cdsType') is not None:
            self.cds_type = m.get('cdsType')
        if m.get('maintainStartTime') is not None:
            self.maintain_start_time = m.get('maintainStartTime')
        if m.get('maintainDuration') is not None:
            self.maintain_duration = m.get('maintainDuration')
        if m.get('maintainPeriod') is not None:
            self.maintain_period = m.get('maintainPeriod')
        if m.get('instanceSubStatus') is not None:
            self.instance_sub_status = m.get('instanceSubStatus')
        if m.get('bcmSendCycle') is not None:
            self.bcm_send_cycle = m.get('bcmSendCycle')
        if m.get('autoResizeDisk') is not None:
            self.auto_resize_disk = m.get('autoResizeDisk')
        if m.get('autoResizeCpu') is not None:
            self.auto_resize_cpu = m.get('autoResizeCpu')
        if m.get('edgeRegion') is not None:
            self.edge_region = m.get('edgeRegion')
        if m.get('edgeRegionName') is not None:
            self.edge_region_name = m.get('edgeRegionName')
        if m.get('edgeVpcId') is not None:
            self.edge_vpc_id = m.get('edgeVpcId')
        if m.get('edgeSubnetId') is not None:
            self.edge_subnet_id = m.get('edgeSubnetId')
        if m.get('gtidType') is not None:
            self.gtid_type = m.get('gtidType')
        if m.get('nodeMasterReadReplica') is not None:
            self.node_master_read_replica = RoleInfo().from_dict(m.get('nodeMasterReadReplica'))
        if m.get('nodeBackupReadReplica') is not None:
            self.node_backup_read_replica = RoleInfo().from_dict(m.get('nodeBackupReadReplica'))
        if m.get('haStrategy') is not None:
            self.ha_strategy = m.get('haStrategy')
        if m.get('isDBRSEnable') is not None:
            self.is_dbrs_enable = m.get('isDBRSEnable')
        if m.get('replicaType') is not None:
            self.replica_type = m.get('replicaType')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('cdsEncrypt') is not None:
            self.cds_encrypt = m.get('cdsEncrypt')
        if m.get('cdsEncryptKey') is not None:
            self.cds_encrypt_key = m.get('cdsEncryptKey')
        if m.get('resourcePlatform') is not None:
            self.resource_platform = m.get('resourcePlatform')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('hasSlave') is not None:
            self.has_slave = m.get('hasSlave')
        if m.get('expireDate') is not None:
            self.expire_date = m.get('expireDate')
        if m.get('hasProxy') is not None:
            self.has_proxy = m.get('hasProxy')
        if m.get('vpcName') is not None:
            self.vpc_name = m.get('vpcName')
        if m.get('resourceUuid') is not None:
            self.resource_uuid = m.get('resourceUuid')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('task') is not None:
            self.task = m.get('task')
        if m.get('orderStatus') is not None:
            self.order_status = m.get('orderStatus')
        if m.get('vpcCidr') is not None:
            self.vpc_cidr = m.get('vpcCidr')
        if m.get('zoneNames') is not None:
            self.zone_names = m.get('zoneNames')
        if m.get('dccHosts') is not None:
            self.dcc_hosts = [MachinePO().from_dict(i) for i in m.get('dccHosts')]
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resourceGroup') is not None:
            self.resource_group = ResourceGroupsDetailFull().from_dict(m.get('resourceGroup'))
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('resourceGroupName') is not None:
            self.resource_group_name = m.get('resourceGroupName')
        if m.get('isChargeProxy') is not None:
            self.is_charge_proxy = m.get('isChargeProxy')
        if m.get('single') is not None:
            self.single = m.get('single')
        return self
