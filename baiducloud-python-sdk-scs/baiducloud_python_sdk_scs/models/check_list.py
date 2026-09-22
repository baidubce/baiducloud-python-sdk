"""
CheckList information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CheckList(AbstractModel):
    """
    CheckList
    """

    def __init__(
        self,
        cluster_instance_status=None,
        cluster_topology=None,
        cluster_redis_is_alived=None,
        cluster_delay=None,
        leader_read_only=None,
    ):
        """
        Initialize CheckList instance.

        :param cluster_instance_status: 集群实例状态是否正常。Yes表示检查通过，No表示检查不通过。
        :type cluster_instance_status: str (optional)

        :param cluster_topology: 集群拓扑是否正常。Yes表示检查通过，No表示检查不通过。
        :type cluster_topology: str (optional)

        :param cluster_redis_is_alived: 集群实例是否都存活。Yes表示检查通过，No表示检查不通过。
        :type cluster_redis_is_alived: str (optional)

        :param cluster_delay: 集群是否存在延迟。Yes表示检查通过，No表示检查不通过。
        :type cluster_delay: str (optional)

        :param leader_read_only: 主节点只读检查是否通过。Yes表示检查通过，No表示检查不通过。
        :type leader_read_only: str (optional)
        """
        super().__init__()
        self.cluster_instance_status = cluster_instance_status
        self.cluster_topology = cluster_topology
        self.cluster_redis_is_alived = cluster_redis_is_alived
        self.cluster_delay = cluster_delay
        self.leader_read_only = leader_read_only

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
        if self.cluster_instance_status is not None:
            result['clusterInstanceStatus'] = self.cluster_instance_status
        if self.cluster_topology is not None:
            result['clusterTopology'] = self.cluster_topology
        if self.cluster_redis_is_alived is not None:
            result['clusterRedisIsAlived'] = self.cluster_redis_is_alived
        if self.cluster_delay is not None:
            result['clusterDelay'] = self.cluster_delay
        if self.leader_read_only is not None:
            result['leaderReadOnly'] = self.leader_read_only
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CheckList

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterInstanceStatus') is not None:
            self.cluster_instance_status = m.get('clusterInstanceStatus')
        if m.get('clusterTopology') is not None:
            self.cluster_topology = m.get('clusterTopology')
        if m.get('clusterRedisIsAlived') is not None:
            self.cluster_redis_is_alived = m.get('clusterRedisIsAlived')
        if m.get('clusterDelay') is not None:
            self.cluster_delay = m.get('clusterDelay')
        if m.get('leaderReadOnly') is not None:
            self.leader_read_only = m.get('leaderReadOnly')
        return self
