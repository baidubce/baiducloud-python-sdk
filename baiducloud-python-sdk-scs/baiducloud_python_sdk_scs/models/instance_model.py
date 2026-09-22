"""
InstanceModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_scs.models.tag import Tag

from baiducloud_python_sdk_scs.models.vpc_info import VpcInfo

from baiducloud_python_sdk_scs.models.subnet_info import SubnetInfo


class InstanceModel(AbstractModel):
    """
    InstanceModel
    """

    def __init__(
        self,
        instance_id=None,
        instance_name=None,
        instance_status=None,
        isolated_status=None,
        cluster_type=None,
        engine=None,
        engine_version=None,
        vnet_ip=None,
        domain=None,
        port=None,
        instance_create_time=None,
        capacity=None,
        used_capacity=None,
        payment_timing=None,
        zone_names=None,
        disk_flavor=None,
        eip=None,
        instance_expire_time=None,
        replication_num=None,
        node_type=None,
        store_type=None,
        shard_num=None,
        tags=None,
        resource_group_id=None,
        resource_group_name=None,
        order_status=None,
        deploy_id_list=None,
        vpc=None,
        subnets=None,
    ):
        """
        Initialize InstanceModel instance.

        :param instance_id: 实例ID
        :type instance_id: str (optional)

        :param instance_name: 实例名
        :type instance_name: str (optional)

        :param instance_status: [实例状态](#InstanceStatus)
        :type instance_status: str (optional)

        :param isolated_status: 已隔离:Isolated(实例在回收站内)
        :type isolated_status: str (optional)

        :param cluster_type: [集群类型](#ClusterType)
        :type cluster_type: str (optional)

        :param engine: [引擎类型](#Engine)
        :type engine: str (optional)

        :param engine_version: 引擎版本
        :type engine_version: str (optional)

        :param vnet_ip: 私网IP
        :type vnet_ip: str (optional)

        :param domain: 内网域名
        :type domain: str (optional)

        :param port: 链接端口
        :type port: int (optional)

        :param instance_create_time: 创建时间（格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC）
        :type instance_create_time: datetime (optional)

        :param capacity: 总容量，单位GB
        :type capacity: float (optional)

        :param used_capacity: 已用容量，单位GB
        :type used_capacity: float (optional)

        :param payment_timing: 付费方式。预付费：Prepaid，后付费：Postpaid
        :type payment_timing: str (optional)

        :param zone_names: 可用区列表
        :type zone_names: List[str] (optional)

        :param disk_flavor: 集群存储空间
        :type disk_flavor: int (optional)

        :param eip: 公网IP
        :type eip: str (optional)

        :param instance_expire_time: 到期时间（格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC）
        :type instance_expire_time: datetime (optional)

        :param replication_num: 副本数
        :type replication_num: int (optional)

        :param node_type: 节点规格
        :type node_type: str (optional)

        :param store_type: 存储类型
        :type store_type: int (optional)

        :param shard_num: 分片数
        :type shard_num: int (optional)

        :param tags: 标签列表
        :type tags: List[Tag] (optional)

        :param resource_group_id: 资源分组ID
        :type resource_group_id: str (optional)

        :param resource_group_name: 资源分组名称
        :type resource_group_name: str (optional)

        :param order_status: 预转后、后转预的标记。 <li>to_postpay: 预付费转后付费<li> to_prepay: 后付费转预付费
        :type order_status: str (optional)

        :param deploy_id_list: 集群绑定的部署集ID列表。
        :type deploy_id_list: List[str] (optional)

        :param vpc: vpc attribute
        :type vpc: VpcInfo (optional)

        :param subnets: 子网信息
        :type subnets: List[SubnetInfo] (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_status = instance_status
        self.isolated_status = isolated_status
        self.cluster_type = cluster_type
        self.engine = engine
        self.engine_version = engine_version
        self.vnet_ip = vnet_ip
        self.domain = domain
        self.port = port
        self.instance_create_time = instance_create_time
        self.capacity = capacity
        self.used_capacity = used_capacity
        self.payment_timing = payment_timing
        self.zone_names = zone_names
        self.disk_flavor = disk_flavor
        self.eip = eip
        self.instance_expire_time = instance_expire_time
        self.replication_num = replication_num
        self.node_type = node_type
        self.store_type = store_type
        self.shard_num = shard_num
        self.tags = tags
        self.resource_group_id = resource_group_id
        self.resource_group_name = resource_group_name
        self.order_status = order_status
        self.deploy_id_list = deploy_id_list
        self.vpc = vpc
        self.subnets = subnets

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
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.isolated_status is not None:
            result['isolatedStatus'] = self.isolated_status
        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type
        if self.engine is not None:
            result['engine'] = self.engine
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.vnet_ip is not None:
            result['vnetIp'] = self.vnet_ip
        if self.domain is not None:
            result['domain'] = self.domain
        if self.port is not None:
            result['port'] = self.port
        if self.instance_create_time is not None:
            result['instanceCreateTime'] = self.instance_create_time
        if self.capacity is not None:
            result['capacity'] = self.capacity
        if self.used_capacity is not None:
            result['usedCapacity'] = self.used_capacity
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.zone_names is not None:
            result['zoneNames'] = self.zone_names
        if self.disk_flavor is not None:
            result['diskFlavor'] = self.disk_flavor
        if self.eip is not None:
            result['eip'] = self.eip
        if self.instance_expire_time is not None:
            result['instanceExpireTime'] = self.instance_expire_time
        if self.replication_num is not None:
            result['replicationNum'] = self.replication_num
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.store_type is not None:
            result['storeType'] = self.store_type
        if self.shard_num is not None:
            result['shardNum'] = self.shard_num
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.resource_group_name is not None:
            result['resourceGroupName'] = self.resource_group_name
        if self.order_status is not None:
            result['orderStatus'] = self.order_status
        if self.deploy_id_list is not None:
            result['deployIdList'] = self.deploy_id_list
        if self.vpc is not None:
            result['vpc'] = self.vpc.to_dict()
        if self.subnets is not None:
            result['subnets'] = [i.to_dict() for i in self.subnets]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('isolatedStatus') is not None:
            self.isolated_status = m.get('isolatedStatus')
        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')
        if m.get('engine') is not None:
            self.engine = m.get('engine')
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('vnetIp') is not None:
            self.vnet_ip = m.get('vnetIp')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('instanceCreateTime') is not None:
            self.instance_create_time = m.get('instanceCreateTime')
        if m.get('capacity') is not None:
            self.capacity = m.get('capacity')
        if m.get('usedCapacity') is not None:
            self.used_capacity = m.get('usedCapacity')
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('zoneNames') is not None:
            self.zone_names = m.get('zoneNames')
        if m.get('diskFlavor') is not None:
            self.disk_flavor = m.get('diskFlavor')
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('instanceExpireTime') is not None:
            self.instance_expire_time = m.get('instanceExpireTime')
        if m.get('replicationNum') is not None:
            self.replication_num = m.get('replicationNum')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        if m.get('shardNum') is not None:
            self.shard_num = m.get('shardNum')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('resourceGroupName') is not None:
            self.resource_group_name = m.get('resourceGroupName')
        if m.get('orderStatus') is not None:
            self.order_status = m.get('orderStatus')
        if m.get('deployIdList') is not None:
            self.deploy_id_list = m.get('deployIdList')
        if m.get('vpc') is not None:
            self.vpc = VpcInfo().from_dict(m.get('vpc'))
        if m.get('subnets') is not None:
            self.subnets = [SubnetInfo().from_dict(i) for i in m.get('subnets')]
        return self
