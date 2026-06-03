"""
CacheDeployGroupInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rapidfs.models.disk_info import DiskInfo


class CacheDeployGroupInfo(AbstractModel):
    """
    CacheDeployGroupInfo
    """

    def __init__(
        self,
        cache_deploy_group_name=None,
        instance_id=None,
        cache_deploy_group_ns=None,
        status=None,
        expected_num=None,
        running_num=None,
        capacity_mi_b=None,
        capacity_used_mi_b=None,
        capacity_used_percentage=None,
        deploy_path=None,
        config=None,
        create_time=None,
        modify_time=None,
        disk_infos=None,
    ):
        """
        Initialize CacheDeployGroupInfo instance.

        :param cache_deploy_group_name: 缓存部署组名称
        :type cache_deploy_group_name: str (optional)

        :param instance_id: RapidFS 实例 ID
        :type instance_id: str (optional)

        :param cache_deploy_group_ns: K8s 集群的命名空间
        :type cache_deploy_group_ns: str (optional)

        :param status: 部署组状态，参考 CacheDeployGroupStatus
        :type status: str (optional)

        :param expected_num: 期望节点数量
        :type expected_num: int (optional)

        :param running_num: 运行中节点数量
        :type running_num: int (optional)

        :param capacity_mi_b: 总容量，单位 MiB
        :type capacity_mi_b: int (optional)

        :param capacity_used_mi_b: 已使用容量，单位 MiB
        :type capacity_used_mi_b: int (optional)

        :param capacity_used_percentage: 容量使用百分比
        :type capacity_used_percentage: float (optional)

        :param deploy_path: 部署路径
        :type deploy_path: str (optional)

        :param config: config attribute
        :type config: str (optional)

        :param create_time: 创建时间，例如 2026-06-01T23:00:10Z\"
        :type create_time: str (optional)

        :param modify_time: 修改时间，例如 2026-06-01T23:00:10Z\"
        :type modify_time: str (optional)

        :param disk_infos: 磁盘信息列表
        :type disk_infos: List[DiskInfo] (optional)
        """
        super().__init__()
        self.cache_deploy_group_name = cache_deploy_group_name
        self.instance_id = instance_id
        self.cache_deploy_group_ns = cache_deploy_group_ns
        self.status = status
        self.expected_num = expected_num
        self.running_num = running_num
        self.capacity_mi_b = capacity_mi_b
        self.capacity_used_mi_b = capacity_used_mi_b
        self.capacity_used_percentage = capacity_used_percentage
        self.deploy_path = deploy_path
        self.config = config
        self.create_time = create_time
        self.modify_time = modify_time
        self.disk_infos = disk_infos

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
        if self.cache_deploy_group_name is not None:
            result['cacheDeployGroupName'] = self.cache_deploy_group_name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.cache_deploy_group_ns is not None:
            result['cacheDeployGroupNS'] = self.cache_deploy_group_ns
        if self.status is not None:
            result['status'] = self.status
        if self.expected_num is not None:
            result['expectedNum'] = self.expected_num
        if self.running_num is not None:
            result['runningNum'] = self.running_num
        if self.capacity_mi_b is not None:
            result['capacityMiB'] = self.capacity_mi_b
        if self.capacity_used_mi_b is not None:
            result['capacityUsedMiB'] = self.capacity_used_mi_b
        if self.capacity_used_percentage is not None:
            result['capacityUsedPercentage'] = self.capacity_used_percentage
        if self.deploy_path is not None:
            result['deployPath'] = self.deploy_path
        if self.config is not None:
            result['config'] = self.config
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.disk_infos is not None:
            result['diskInfos'] = [i.to_dict() for i in self.disk_infos]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CacheDeployGroupInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cacheDeployGroupName') is not None:
            self.cache_deploy_group_name = m.get('cacheDeployGroupName')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('cacheDeployGroupNS') is not None:
            self.cache_deploy_group_ns = m.get('cacheDeployGroupNS')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('expectedNum') is not None:
            self.expected_num = m.get('expectedNum')
        if m.get('runningNum') is not None:
            self.running_num = m.get('runningNum')
        if m.get('capacityMiB') is not None:
            self.capacity_mi_b = m.get('capacityMiB')
        if m.get('capacityUsedMiB') is not None:
            self.capacity_used_mi_b = m.get('capacityUsedMiB')
        if m.get('capacityUsedPercentage') is not None:
            self.capacity_used_percentage = m.get('capacityUsedPercentage')
        if m.get('deployPath') is not None:
            self.deploy_path = m.get('deployPath')
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('diskInfos') is not None:
            self.disk_infos = [DiskInfo().from_dict(i) for i in m.get('diskInfos')]
        return self
