"""
Leader information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Leader(AbstractModel):
    """
    Leader
    """

    def __init__(
        self,
        group_name=None,
        leader_id=None,
        leader_region=None,
        cluster_name=None,
        cluster_show_id=None,
        region=None,
        status=None,
        total_capacity_in_gb=None,
        used_capacity_in_gb=None,
        shard_num=None,
        flavor=None,
        qps_write=None,
        qps_read=None,
        stale_readable=None,
        forbid_write=None,
        availability_zone=None,
        expired_time=None,
    ):
        """
        Initialize Leader instance.

        :param group_name: 热活实例组名称。规则：支持大小写字母、数字以及-_.等特殊字符，长度6~32
        :type group_name: str (optional)

        :param leader_id: 热活实例组主角色实例ID
        :type leader_id: str (optional)

        :param leader_region: 热活实例组主角色所在地域
        :type leader_region: str (optional)

        :param cluster_name: 主角色实例名称
        :type cluster_name: str (optional)

        :param cluster_show_id: 主角色实例ID
        :type cluster_show_id: str (optional)

        :param region: 主角色地域
        :type region: str (optional)

        :param status: 主角色实例状态
        :type status: str (optional)

        :param total_capacity_in_gb: 总容量
        :type total_capacity_in_gb: float (optional)

        :param used_capacity_in_gb: 已用容量
        :type used_capacity_in_gb: int (optional)

        :param shard_num: 分片数
        :type shard_num: int (optional)

        :param flavor: 单分片容量
        :type flavor: int (optional)

        :param qps_write: 写流量阈值
        :type qps_write: int (optional)

        :param qps_read: 读流量阈值
        :type qps_read: int (optional)

        :param stale_readable: 从角色脏读开关状态（true:打开， false:关闭）
        :type stale_readable: bool (optional)

        :param forbid_write: 禁写标志（0 未禁写， 1 禁写）
        :type forbid_write: int (optional)

        :param availability_zone: 可用区
        :type availability_zone: str (optional)

        :param expired_time: 过期时间
        :type expired_time: date (optional)
        """
        super().__init__()
        self.group_name = group_name
        self.leader_id = leader_id
        self.leader_region = leader_region
        self.cluster_name = cluster_name
        self.cluster_show_id = cluster_show_id
        self.region = region
        self.status = status
        self.total_capacity_in_gb = total_capacity_in_gb
        self.used_capacity_in_gb = used_capacity_in_gb
        self.shard_num = shard_num
        self.flavor = flavor
        self.qps_write = qps_write
        self.qps_read = qps_read
        self.stale_readable = stale_readable
        self.forbid_write = forbid_write
        self.availability_zone = availability_zone
        self.expired_time = expired_time

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
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.leader_id is not None:
            result['leaderId'] = self.leader_id
        if self.leader_region is not None:
            result['leaderRegion'] = self.leader_region
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.cluster_show_id is not None:
            result['clusterShowId'] = self.cluster_show_id
        if self.region is not None:
            result['region'] = self.region
        if self.status is not None:
            result['status'] = self.status
        if self.total_capacity_in_gb is not None:
            result['totalCapacityInGB'] = self.total_capacity_in_gb
        if self.used_capacity_in_gb is not None:
            result['usedCapacityInGB'] = self.used_capacity_in_gb
        if self.shard_num is not None:
            result['shardNum'] = self.shard_num
        if self.flavor is not None:
            result['flavor'] = self.flavor
        if self.qps_write is not None:
            result['qpsWrite'] = self.qps_write
        if self.qps_read is not None:
            result['qpsRead'] = self.qps_read
        if self.stale_readable is not None:
            result['staleReadable'] = self.stale_readable
        if self.forbid_write is not None:
            result['forbidWrite'] = self.forbid_write
        if self.availability_zone is not None:
            result['availabilityZone'] = self.availability_zone
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Leader

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('leaderId') is not None:
            self.leader_id = m.get('leaderId')
        if m.get('leaderRegion') is not None:
            self.leader_region = m.get('leaderRegion')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('clusterShowId') is not None:
            self.cluster_show_id = m.get('clusterShowId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('totalCapacityInGB') is not None:
            self.total_capacity_in_gb = m.get('totalCapacityInGB')
        if m.get('usedCapacityInGB') is not None:
            self.used_capacity_in_gb = m.get('usedCapacityInGB')
        if m.get('shardNum') is not None:
            self.shard_num = m.get('shardNum')
        if m.get('flavor') is not None:
            self.flavor = m.get('flavor')
        if m.get('qpsWrite') is not None:
            self.qps_write = m.get('qpsWrite')
        if m.get('qpsRead') is not None:
            self.qps_read = m.get('qpsRead')
        if m.get('staleReadable') is not None:
            self.stale_readable = m.get('staleReadable')
        if m.get('forbidWrite') is not None:
            self.forbid_write = m.get('forbidWrite')
        if m.get('availabilityZone') is not None:
            self.availability_zone = m.get('availabilityZone')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        return self
