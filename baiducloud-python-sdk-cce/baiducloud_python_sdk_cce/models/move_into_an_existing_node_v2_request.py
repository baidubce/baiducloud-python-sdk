"""
Request entity for MoveIntoAnExistingNodeV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_cce.models.instance_set import InstanceSet
from baiducloud_python_sdk_cce.models.existed_instance_in_cluster import ExistedInstanceInCluster


class MoveIntoAnExistingNodeV2Request(AbstractModel):
    """
    Request entity for MoveIntoAnExistingNodeV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        cluster_id,
        instance_group_id,
        in_cluster,
        use_instance_group_config,
        use_instance_group_config_with_disk_info=None,
        install_gpu_driver=None,
        existed_instances=None,
        existed_instances_in_cluster=None,
    ):
        """
        Initialize MoveIntoAnExistingNodeV2Request request entity.

        :param cluster_id: cluster_id parameter
        :type cluster_id: str (required)

        :param instance_group_id: instance_group_id parameter
        :type instance_group_id: str (required)

        :param in_cluster: 是否是集群内节点。
        :type in_cluster: bool (required)

        :param use_instance_group_config: 针对集群外节点生效，设置为 true 将使用节点组配置。
        :type use_instance_group_config: bool (required)

        :param use_instance_group_config_with_disk_info: 针对集群外节点生效，设置为 true 将使用节点组配置（含磁盘信息）。
        :type use_instance_group_config_with_disk_info: bool (optional)

        :param install_gpu_driver: 是否安装 GPU 驱动
        :type install_gpu_driver: bool (optional)

        :param existed_instances: 配置集群外节点的详细信息。
        :type existed_instances: List[InstanceSet] (optional)

        :param existed_instances_in_cluster: 配置集群内节点的详细信息。
        :type existed_instances_in_cluster: List[ExistedInstanceInCluster] (optional)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.instance_group_id = instance_group_id
        self.in_cluster = in_cluster
        self.use_instance_group_config = use_instance_group_config
        self.use_instance_group_config_with_disk_info = use_instance_group_config_with_disk_info
        self.install_gpu_driver = install_gpu_driver
        self.existed_instances = existed_instances
        self.existed_instances_in_cluster = existed_instances_in_cluster

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
        if self.in_cluster is not None:
            result['inCluster'] = self.in_cluster
        if self.use_instance_group_config is not None:
            result['useInstanceGroupConfig'] = self.use_instance_group_config
        if self.use_instance_group_config_with_disk_info is not None:
            result['useInstanceGroupConfigWithDiskInfo'] = self.use_instance_group_config_with_disk_info
        if self.install_gpu_driver is not None:
            result['installGpuDriver'] = self.install_gpu_driver
        if self.existed_instances is not None:
            result['existedInstances'] = [i.to_dict() for i in self.existed_instances]
        if self.existed_instances_in_cluster is not None:
            result['existedInstancesInCluster'] = [i.to_dict() for i in self.existed_instances_in_cluster]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MoveIntoAnExistingNodeV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterID') is not None:
            self.cluster_id = m.get('clusterID')
        if m.get('instanceGroupID') is not None:
            self.instance_group_id = m.get('instanceGroupID')
        if m.get('inCluster') is not None:
            self.in_cluster = m.get('inCluster')
        if m.get('useInstanceGroupConfig') is not None:
            self.use_instance_group_config = m.get('useInstanceGroupConfig')
        if m.get('useInstanceGroupConfigWithDiskInfo') is not None:
            self.use_instance_group_config_with_disk_info = m.get('useInstanceGroupConfigWithDiskInfo')
        if m.get('installGpuDriver') is not None:
            self.install_gpu_driver = m.get('installGpuDriver')
        if m.get('existedInstances') is not None:
            self.existed_instances = [InstanceSet().from_dict(i) for i in m.get('existedInstances')]
        if m.get('existedInstancesInCluster') is not None:
            self.existed_instances_in_cluster = [
                ExistedInstanceInCluster().from_dict(i) for i in m.get('existedInstancesInCluster')
            ]
        return self
