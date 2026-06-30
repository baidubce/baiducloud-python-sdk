"""
InstanceModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bci.models.tag import Tag


class InstanceModel(AbstractModel):
    """
    InstanceModel
    """

    def __init__(
        self,
        instance_id=None,
        instance_name=None,
        status=None,
        zone_name=None,
        cpu_type=None,
        gpu_type=None,
        cpu=None,
        memory=None,
        bandwidth_in_mbps=None,
        internal_ip=None,
        public_ip=None,
        create_time=None,
        update_time=None,
        delete_time=None,
        restart_policy=None,
        tags=None,
    ):
        """
        Initialize InstanceModel instance.

        :param instance_id: 实例ID
        :type instance_id: str (optional)

        :param instance_name: 实例名称（容器组名称）
        :type instance_name: str (optional)

        :param status: 状态：Pending、Running、Succeeded、Failed
        :type status: str (optional)

        :param zone_name: 所属可用区
        :type zone_name: str (optional)

        :param cpu_type: cpu类型
        :type cpu_type: str (optional)

        :param gpu_type: gpu类型
        :type gpu_type: str (optional)

        :param cpu: cpu核数（核）
        :type cpu: float (optional)

        :param memory: memory大小（GiB）
        :type memory: float (optional)

        :param bandwidth_in_mbps: 弹性公网IP带宽（Mb）
        :type bandwidth_in_mbps: int (optional)

        :param internal_ip: 内网IP
        :type internal_ip: str (optional)

        :param public_ip: 外网IP
        :type public_ip: str (optional)

        :param create_time: 系统创建时间（UTC，RFC3339）
        :type create_time: str (optional)

        :param update_time: 实例更新时间
        :type update_time: str (optional)

        :param delete_time: 实例删除时间
        :type delete_time: str (optional)

        :param restart_policy: 重启策略：Never、Always、OnFailure
        :type restart_policy: str (optional)

        :param tags: 标签键值对
        :type tags: List[Tag] (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.status = status
        self.zone_name = zone_name
        self.cpu_type = cpu_type
        self.gpu_type = gpu_type
        self.cpu = cpu
        self.memory = memory
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.internal_ip = internal_ip
        self.public_ip = public_ip
        self.create_time = create_time
        self.update_time = update_time
        self.delete_time = delete_time
        self.restart_policy = restart_policy
        self.tags = tags

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
        if self.status is not None:
            result['status'] = self.status
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.cpu_type is not None:
            result['cpuType'] = self.cpu_type
        if self.gpu_type is not None:
            result['gpuType'] = self.gpu_type
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.memory is not None:
            result['memory'] = self.memory
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.internal_ip is not None:
            result['internalIp'] = self.internal_ip
        if self.public_ip is not None:
            result['publicIp'] = self.public_ip
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.delete_time is not None:
            result['deleteTime'] = self.delete_time
        if self.restart_policy is not None:
            result['restartPolicy'] = self.restart_policy
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
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
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('cpuType') is not None:
            self.cpu_type = m.get('cpuType')
        if m.get('gpuType') is not None:
            self.gpu_type = m.get('gpuType')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('internalIp') is not None:
            self.internal_ip = m.get('internalIp')
        if m.get('publicIp') is not None:
            self.public_ip = m.get('publicIp')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('deleteTime') is not None:
            self.delete_time = m.get('deleteTime')
        if m.get('restartPolicy') is not None:
            self.restart_policy = m.get('restartPolicy')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        return self
