"""
Request entity for GetInstanceDetailResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_scs.models.replication_item import ReplicationItem
from baiducloud_python_sdk_scs.models.subnet import Subnet
from baiducloud_python_sdk_scs.models.proxy_item import ProxyItem
from baiducloud_python_sdk_scs.models.cache_cluster_node import CacheClusterNode
from baiducloud_python_sdk_scs.models.redis_node import RedisNode
from baiducloud_python_sdk_scs.models.tag import Tag
from baiducloud_python_sdk_scs.models.instance_full_version_info import InstanceFullVersionInfo
from baiducloud_python_sdk_scs.models.maintain_time import MaintainTime
from baiducloud_python_sdk_scs.models.feature_switches import FeatureSwitches
from baiducloud_python_sdk_scs.models.entrance_item import EntranceItem


class GetInstanceDetailResponse(BceResponse):
    """
    GetInstanceDetailResponse
    """

    def __init__(
        self,
        instance_id=None,
        instance_name=None,
        instance_status=None,
        cluster_type=None,
        engine=None,
        engine_version=None,
        node_type=None,
        store_type=None,
        shard_num=None,
        vnet_ip=None,
        eip=None,
        domain=None,
        public_domain=None,
        port=None,
        instance_create_time=None,
        instance_expire_time=None,
        capacity=None,
        used_capacity=None,
        payment_timing=None,
        zone_names=None,
        replication_num=None,
        replication_info=None,
        disk_flavor=None,
        enable_read_only=None,
        vpc_id=None,
        subnets=None,
        auto_renew=None,
        entrance=None,
        enable_slow_log=None,
        bns_group=None,
        proxy_list=None,
        cache_cluster_instances=None,
        redis_list=None,
        tags=None,
        resource_group_id=None,
        resource_group_name=None,
        full_version_info=None,
        maintain_time=None,
        enable_hotkey=None,
        order_status=None,
        feature_switches=None,
        cross_az_nearest=None,
        entrance_list=None,
        support_sentinel_commands=None,
    ):
        """
        Initialize GetInstanceDetailResponse response.

        :param instance_id: 实例ID
        :type instance_id: str (optional)

        :param instance_name: 实例名称
        :type instance_name: str (optional)

        :param instance_status: 实例状态
        :type instance_status: str (optional)

        :param cluster_type: [集群类型](#ClusterType)
        :type cluster_type: str (optional)

        :param engine: [引擎类型](#Engine)
        :type engine: str (optional)

        :param engine_version: 引擎版本
        :type engine_version: str (optional)

        :param node_type: 节点规格
        :type node_type: str (optional)

        :param store_type: 存储类型
        :type store_type: int (optional)

        :param shard_num: 分片数量
        :type shard_num: int (optional)

        :param vnet_ip: 私网IP
        :type vnet_ip: str (optional)

        :param eip: 公网IP
        :type eip: str (optional)

        :param domain: 内网域名
        :type domain: str (optional)

        :param public_domain: 公网域名
        :type public_domain: str (optional)

        :param port: 内网端口
        :type port: int (optional)

        :param instance_create_time: 创建时间（格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC）
        :type instance_create_time: datetime (optional)

        :param instance_expire_time: 到期时间（格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC）
        :type instance_expire_time: datetime (optional)

        :param capacity: 总容量，单位GB
        :type capacity: float (optional)

        :param used_capacity: 已用容量，单位GB
        :type used_capacity: float (optional)

        :param payment_timing: 付费方式。包年包月：Prepaid，按量付费：Postpaid
        :type payment_timing: str (optional)

        :param zone_names: 可用区列表
        :type zone_names: List[str] (optional)

        :param replication_num: 副本数
        :type replication_num: int (optional)

        :param replication_info: 副本信息
        :type replication_info: List[ReplicationItem] (optional)

        :param disk_flavor: 存储容量
        :type disk_flavor: int (optional)

        :param enable_read_only: 副本只读开关。1：打开 2：关闭
        :type enable_read_only: int (optional)

        :param vpc_id: VPC的ID
        :type vpc_id: str (optional)

        :param subnets: 子网列表
        :type subnets: List[Subnet] (optional)

        :param auto_renew: 是否自动续费。是：true，否：false
        :type auto_renew: bool (optional)

        :param entrance: 统一读入口地址。开启统一读入口后生效。
        :type entrance: str (optional)

        :param enable_slow_log: 慢日志是否开启
        :type enable_slow_log: int (optional)

        :param bns_group: 集团云创建的实例绑定bnsGroup
        :type bns_group: str (optional)

        :param proxy_list: 代理节点列表
        :type proxy_list: List[ProxyItem] (optional)

        :param cache_cluster_instances: 分片信息
        :type cache_cluster_instances: List[CacheClusterNode] (optional)

        :param redis_list: 节点信息
        :type redis_list: List[RedisNode] (optional)

        :param tags: 标签
        :type tags: List[Tag] (optional)

        :param resource_group_id: 资源分组ID
        :type resource_group_id: str (optional)

        :param resource_group_name: 资源分组名称
        :type resource_group_name: str (optional)

        :param full_version_info: full_version_info field
        :type full_version_info: InstanceFullVersionInfo (optional)

        :param maintain_time: maintain_time field
        :type maintain_time: MaintainTime (optional)

        :param enable_hotkey: 是否开启热key
        :type enable_hotkey: bool (optional)

        :param order_status: 预转后、后转预的标记。to_postpay: 预付费转后付费，to_prepay: 后付费转预付费
        :type order_status: str (optional)

        :param feature_switches: feature_switches field
        :type feature_switches: FeatureSwitches (optional)

        :param cross_az_nearest: 跨AZ就近是否开启: yes 开启, no 未开启
        :type cross_az_nearest: str (optional)

        :param entrance_list: 就近访问入口列表
        :type entrance_list: List[EntranceItem] (optional)

        :param support_sentinel_commands: sentinel命令兼容开启情况。true: 开启, false: 关闭
        :type support_sentinel_commands: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_status = instance_status
        self.cluster_type = cluster_type
        self.engine = engine
        self.engine_version = engine_version
        self.node_type = node_type
        self.store_type = store_type
        self.shard_num = shard_num
        self.vnet_ip = vnet_ip
        self.eip = eip
        self.domain = domain
        self.public_domain = public_domain
        self.port = port
        self.instance_create_time = instance_create_time
        self.instance_expire_time = instance_expire_time
        self.capacity = capacity
        self.used_capacity = used_capacity
        self.payment_timing = payment_timing
        self.zone_names = zone_names
        self.replication_num = replication_num
        self.replication_info = replication_info
        self.disk_flavor = disk_flavor
        self.enable_read_only = enable_read_only
        self.vpc_id = vpc_id
        self.subnets = subnets
        self.auto_renew = auto_renew
        self.entrance = entrance
        self.enable_slow_log = enable_slow_log
        self.bns_group = bns_group
        self.proxy_list = proxy_list
        self.cache_cluster_instances = cache_cluster_instances
        self.redis_list = redis_list
        self.tags = tags
        self.resource_group_id = resource_group_id
        self.resource_group_name = resource_group_name
        self.full_version_info = full_version_info
        self.maintain_time = maintain_time
        self.enable_hotkey = enable_hotkey
        self.order_status = order_status
        self.feature_switches = feature_switches
        self.cross_az_nearest = cross_az_nearest
        self.entrance_list = entrance_list
        self.support_sentinel_commands = support_sentinel_commands

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type
        if self.engine is not None:
            result['engine'] = self.engine
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.store_type is not None:
            result['storeType'] = self.store_type
        if self.shard_num is not None:
            result['shardNum'] = self.shard_num
        if self.vnet_ip is not None:
            result['vnetIp'] = self.vnet_ip
        if self.eip is not None:
            result['eip'] = self.eip
        if self.domain is not None:
            result['domain'] = self.domain
        if self.public_domain is not None:
            result['publicDomain'] = self.public_domain
        if self.port is not None:
            result['port'] = self.port
        if self.instance_create_time is not None:
            result['instanceCreateTime'] = self.instance_create_time
        if self.instance_expire_time is not None:
            result['instanceExpireTime'] = self.instance_expire_time
        if self.capacity is not None:
            result['capacity'] = self.capacity
        if self.used_capacity is not None:
            result['usedCapacity'] = self.used_capacity
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.zone_names is not None:
            result['zoneNames'] = self.zone_names
        if self.replication_num is not None:
            result['replicationNum'] = self.replication_num
        if self.replication_info is not None:
            result['replicationInfo'] = [i.to_dict() for i in self.replication_info]
        if self.disk_flavor is not None:
            result['diskFlavor'] = self.disk_flavor
        if self.enable_read_only is not None:
            result['enableReadOnly'] = self.enable_read_only
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.subnets is not None:
            result['subnets'] = [i.to_dict() for i in self.subnets]
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.entrance is not None:
            result['entrance'] = self.entrance
        if self.enable_slow_log is not None:
            result['enableSlowLog'] = self.enable_slow_log
        if self.bns_group is not None:
            result['bnsGroup'] = self.bns_group
        if self.proxy_list is not None:
            result['proxyList'] = [i.to_dict() for i in self.proxy_list]
        if self.cache_cluster_instances is not None:
            result['cacheClusterInstances'] = [i.to_dict() for i in self.cache_cluster_instances]
        if self.redis_list is not None:
            result['redisList'] = [i.to_dict() for i in self.redis_list]
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.resource_group_name is not None:
            result['resourceGroupName'] = self.resource_group_name
        if self.full_version_info is not None:
            result['fullVersionInfo'] = self.full_version_info.to_dict()
        if self.maintain_time is not None:
            result['maintainTime'] = self.maintain_time.to_dict()
        if self.enable_hotkey is not None:
            result['enableHotkey'] = self.enable_hotkey
        if self.order_status is not None:
            result['orderStatus'] = self.order_status
        if self.feature_switches is not None:
            result['featureSwitches'] = self.feature_switches.to_dict()
        if self.cross_az_nearest is not None:
            result['crossAzNearest'] = self.cross_az_nearest
        if self.entrance_list is not None:
            result['entranceList'] = [i.to_dict() for i in self.entrance_list]
        if self.support_sentinel_commands is not None:
            result['supportSentinelCommands'] = self.support_sentinel_commands
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetInstanceDetailResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')
        if m.get('engine') is not None:
            self.engine = m.get('engine')
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        if m.get('shardNum') is not None:
            self.shard_num = m.get('shardNum')
        if m.get('vnetIp') is not None:
            self.vnet_ip = m.get('vnetIp')
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('publicDomain') is not None:
            self.public_domain = m.get('publicDomain')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('instanceCreateTime') is not None:
            self.instance_create_time = m.get('instanceCreateTime')
        if m.get('instanceExpireTime') is not None:
            self.instance_expire_time = m.get('instanceExpireTime')
        if m.get('capacity') is not None:
            self.capacity = m.get('capacity')
        if m.get('usedCapacity') is not None:
            self.used_capacity = m.get('usedCapacity')
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('zoneNames') is not None:
            self.zone_names = m.get('zoneNames')
        if m.get('replicationNum') is not None:
            self.replication_num = m.get('replicationNum')
        if m.get('replicationInfo') is not None:
            self.replication_info = [ReplicationItem().from_dict(i) for i in m.get('replicationInfo')]
        if m.get('diskFlavor') is not None:
            self.disk_flavor = m.get('diskFlavor')
        if m.get('enableReadOnly') is not None:
            self.enable_read_only = m.get('enableReadOnly')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('subnets') is not None:
            self.subnets = [Subnet().from_dict(i) for i in m.get('subnets')]
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('entrance') is not None:
            self.entrance = m.get('entrance')
        if m.get('enableSlowLog') is not None:
            self.enable_slow_log = m.get('enableSlowLog')
        if m.get('bnsGroup') is not None:
            self.bns_group = m.get('bnsGroup')
        if m.get('proxyList') is not None:
            self.proxy_list = [ProxyItem().from_dict(i) for i in m.get('proxyList')]
        if m.get('cacheClusterInstances') is not None:
            self.cache_cluster_instances = [CacheClusterNode().from_dict(i) for i in m.get('cacheClusterInstances')]
        if m.get('redisList') is not None:
            self.redis_list = [RedisNode().from_dict(i) for i in m.get('redisList')]
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('resourceGroupName') is not None:
            self.resource_group_name = m.get('resourceGroupName')
        if m.get('fullVersionInfo') is not None:
            self.full_version_info = InstanceFullVersionInfo().from_dict(m.get('fullVersionInfo'))
        if m.get('maintainTime') is not None:
            self.maintain_time = MaintainTime().from_dict(m.get('maintainTime'))
        if m.get('enableHotkey') is not None:
            self.enable_hotkey = m.get('enableHotkey')
        if m.get('orderStatus') is not None:
            self.order_status = m.get('orderStatus')
        if m.get('featureSwitches') is not None:
            self.feature_switches = FeatureSwitches().from_dict(m.get('featureSwitches'))
        if m.get('crossAzNearest') is not None:
            self.cross_az_nearest = m.get('crossAzNearest')
        if m.get('entranceList') is not None:
            self.entrance_list = [EntranceItem().from_dict(i) for i in m.get('entranceList')]
        if m.get('supportSentinelCommands') is not None:
            self.support_sentinel_commands = m.get('supportSentinelCommands')
        return self
