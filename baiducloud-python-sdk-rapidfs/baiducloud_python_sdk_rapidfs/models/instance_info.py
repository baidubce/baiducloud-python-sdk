"""
InstanceInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rapidfs.models.tag import Tag


class InstanceInfo(AbstractModel):
    """
    InstanceInfo
    """

    def __init__(
        self,
        instance_name=None,
        instance_id=None,
        description=None,
        status=None,
        region=None,
        zone=None,
        capacity_mi_b=None,
        capacity_used_mi_b=None,
        capacity_used_percentage=None,
        vpc_id=None,
        subnet_id=None,
        managed_mode=None,
        meta_spec=None,
        data_spec=None,
        type=None,
        resize_status=None,
        allocated_quota_mi_b=None,
        cce_cluster_id=None,
        aihc_resource_pool_id=None,
        k8s_controller_id=None,
        tags=None,
        create_time=None,
    ):
        """
        Initialize InstanceInfo instance.

        :param instance_name: RapidFS 实例名称
        :type instance_name: str (optional)

        :param instance_id: RapidFS 实例唯一 ID
        :type instance_id: str (optional)

        :param description: RapidFS 实例描述信息
        :type description: str (optional)

        :param status: RapidFS 实例状态， 见 InstanceStatus
        :type status: str (optional)

        :param region: 地域缩写，bd，bj ……
        :type region: str (optional)

        :param zone: 可用区，ZoneA，ZoneB ……
        :type zone: str (optional)

        :param capacity_mi_b: 缓存总容量，单位 MiB
        :type capacity_mi_b: int (optional)

        :param capacity_used_mi_b: 已使用缓存总容量，单位 MiB
        :type capacity_used_mi_b: int (optional)

        :param capacity_used_percentage: 缓存使用率，百分比
        :type capacity_used_percentage: float (optional)

        :param vpc_id: RapidFS 实例所在 vpc，短 ID
        :type vpc_id: str (optional)

        :param subnet_id: RapidFS 实例所在子网，短 ID
        :type subnet_id: str (optional)

        :param managed_mode: managed_mode attribute
        :type managed_mode: str (optional)

        :param meta_spec: meta_spec attribute
        :type meta_spec: str (optional)

        :param data_spec: data_spec attribute
        :type data_spec: str (optional)

        :param type: type attribute
        :type type: str (optional)

        :param resize_status: RapidFS实例扩缩容状态，见 ResizeStatus：状态非 Normal 时需要用户发起二次确认
        :type resize_status: str (optional)

        :param allocated_quota_mi_b: 实例内所有数据源已分配 Quota 的容量之和
        :type allocated_quota_mi_b: int (optional)

        :param cce_cluster_id: cce_cluster_id attribute
        :type cce_cluster_id: str (optional)

        :param aihc_resource_pool_id: aihc_resource_pool_id attribute
        :type aihc_resource_pool_id: str (optional)

        :param k8s_controller_id: k8s_controller_id attribute
        :type k8s_controller_id: str (optional)

        :param tags: 标签列表
        :type tags: List[Tag] (optional)

        :param create_time: RapidFS 实例创建时间，例如 2026-06-01T23:00:10Z\"
        :type create_time: str (optional)
        """
        super().__init__()
        self.instance_name = instance_name
        self.instance_id = instance_id
        self.description = description
        self.status = status
        self.region = region
        self.zone = zone
        self.capacity_mi_b = capacity_mi_b
        self.capacity_used_mi_b = capacity_used_mi_b
        self.capacity_used_percentage = capacity_used_percentage
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.managed_mode = managed_mode
        self.meta_spec = meta_spec
        self.data_spec = data_spec
        self.type = type
        self.resize_status = resize_status
        self.allocated_quota_mi_b = allocated_quota_mi_b
        self.cce_cluster_id = cce_cluster_id
        self.aihc_resource_pool_id = aihc_resource_pool_id
        self.k8s_controller_id = k8s_controller_id
        self.tags = tags
        self.create_time = create_time

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
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.description is not None:
            result['description'] = self.description
        if self.status is not None:
            result['status'] = self.status
        if self.region is not None:
            result['region'] = self.region
        if self.zone is not None:
            result['zone'] = self.zone
        if self.capacity_mi_b is not None:
            result['capacityMiB'] = self.capacity_mi_b
        if self.capacity_used_mi_b is not None:
            result['capacityUsedMiB'] = self.capacity_used_mi_b
        if self.capacity_used_percentage is not None:
            result['capacityUsedPercentage'] = self.capacity_used_percentage
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.managed_mode is not None:
            result['managedMode'] = self.managed_mode
        if self.meta_spec is not None:
            result['metaSpec'] = self.meta_spec
        if self.data_spec is not None:
            result['dataSpec'] = self.data_spec
        if self.type is not None:
            result['type'] = self.type
        if self.resize_status is not None:
            result['resizeStatus'] = self.resize_status
        if self.allocated_quota_mi_b is not None:
            result['allocatedQuotaMiB'] = self.allocated_quota_mi_b
        if self.cce_cluster_id is not None:
            result['cceClusterId'] = self.cce_cluster_id
        if self.aihc_resource_pool_id is not None:
            result['aihcResourcePoolId'] = self.aihc_resource_pool_id
        if self.k8s_controller_id is not None:
            result['k8sControllerId'] = self.k8s_controller_id
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.create_time is not None:
            result['createTime'] = self.create_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        if m.get('capacityMiB') is not None:
            self.capacity_mi_b = m.get('capacityMiB')
        if m.get('capacityUsedMiB') is not None:
            self.capacity_used_mi_b = m.get('capacityUsedMiB')
        if m.get('capacityUsedPercentage') is not None:
            self.capacity_used_percentage = m.get('capacityUsedPercentage')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('managedMode') is not None:
            self.managed_mode = m.get('managedMode')
        if m.get('metaSpec') is not None:
            self.meta_spec = m.get('metaSpec')
        if m.get('dataSpec') is not None:
            self.data_spec = m.get('dataSpec')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('resizeStatus') is not None:
            self.resize_status = m.get('resizeStatus')
        if m.get('allocatedQuotaMiB') is not None:
            self.allocated_quota_mi_b = m.get('allocatedQuotaMiB')
        if m.get('cceClusterId') is not None:
            self.cce_cluster_id = m.get('cceClusterId')
        if m.get('aihcResourcePoolId') is not None:
            self.aihc_resource_pool_id = m.get('aihcResourcePoolId')
        if m.get('k8sControllerId') is not None:
            self.k8s_controller_id = m.get('k8sControllerId')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        return self
