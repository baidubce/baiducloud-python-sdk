"""
ClusterItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_scs.models.sync_flow_item import SyncFlowItem


class ClusterItem(AbstractModel):
    """
    ClusterItem
    """

    def __init__(
        self,
        cluster_show_id=None,
        cluster_name=None,
        region=None,
        cluster_status=None,
        cluster_engine=None,
        create_time=None,
        total_capacity_in_gb=None,
        used_capacity_in_gb=None,
        expired_time=None,
        shard_list=None,
        sync_flow=None,
    ):
        """
        Initialize ClusterItem instance.

        :param cluster_show_id: 成员集群的ID。
        :type cluster_show_id: str (optional)

        :param cluster_name: 成员集群的名称。
        :type cluster_name: str (optional)

        :param region: 成员集群所在地域。
        :type region: str (optional)

        :param cluster_status: 集群状态。此状态为集群在实例组中的状态，非集群本身状态。
        :type cluster_status: str (optional)

        :param cluster_engine: 集群引擎类型。
        :type cluster_engine: str (optional)

        :param create_time: 集群创建时间。
        :type create_time: str (optional)

        :param total_capacity_in_gb: 集群总容量。
        :type total_capacity_in_gb: float (optional)

        :param used_capacity_in_gb: 集群已用容量。
        :type used_capacity_in_gb: float (optional)

        :param expired_time: 集群到期时间。
        :type expired_time: str (optional)

        :param shard_list: 集群分片列表。查询多活组监控数据时使用。
        :type shard_list: List[str] (optional)

        :param sync_flow: 集群BLB信息列表。查询多活组监控数据时使用。
        :type sync_flow: List[SyncFlowItem] (optional)
        """
        super().__init__()
        self.cluster_show_id = cluster_show_id
        self.cluster_name = cluster_name
        self.region = region
        self.cluster_status = cluster_status
        self.cluster_engine = cluster_engine
        self.create_time = create_time
        self.total_capacity_in_gb = total_capacity_in_gb
        self.used_capacity_in_gb = used_capacity_in_gb
        self.expired_time = expired_time
        self.shard_list = shard_list
        self.sync_flow = sync_flow

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
        if self.cluster_show_id is not None:
            result['clusterShowId'] = self.cluster_show_id
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.region is not None:
            result['region'] = self.region
        if self.cluster_status is not None:
            result['clusterStatus'] = self.cluster_status
        if self.cluster_engine is not None:
            result['clusterEngine'] = self.cluster_engine
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.total_capacity_in_gb is not None:
            result['totalCapacityInGb'] = self.total_capacity_in_gb
        if self.used_capacity_in_gb is not None:
            result['usedCapacityInGb'] = self.used_capacity_in_gb
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.shard_list is not None:
            result['shardList'] = self.shard_list
        if self.sync_flow is not None:
            result['syncFlow'] = [i.to_dict() for i in self.sync_flow]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ClusterItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterShowId') is not None:
            self.cluster_show_id = m.get('clusterShowId')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('clusterStatus') is not None:
            self.cluster_status = m.get('clusterStatus')
        if m.get('clusterEngine') is not None:
            self.cluster_engine = m.get('clusterEngine')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('totalCapacityInGb') is not None:
            self.total_capacity_in_gb = m.get('totalCapacityInGb')
        if m.get('usedCapacityInGb') is not None:
            self.used_capacity_in_gb = m.get('usedCapacityInGb')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('shardList') is not None:
            self.shard_list = m.get('shardList')
        if m.get('syncFlow') is not None:
            self.sync_flow = [SyncFlowItem().from_dict(i) for i in m.get('syncFlow')]
        return self
