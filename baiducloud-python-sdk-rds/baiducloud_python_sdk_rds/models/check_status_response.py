"""
CheckStatusResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CheckStatusResponse(BceResponse):
    """
    CheckStatusResponse
    """

    def __init__(
        self,
        cluster_instance_status=None,
        cluster_topology=None,
        cluster_my_sqlis_alived=None,
        cluster_delay=None,
        leader_read_only=None,
    ):
        """
        Initialize CheckStatusResponse instance.

        :param cluster_instance_status: 集群中实例状态检查结果，有两种取值。Yes表示检查通过，No表示检查不通过。
        :type cluster_instance_status: str (optional)

        :param cluster_topology: 集群中实例拓扑信息检查结果，有两种取值。Yes表示检查通过，No表示检查不通过。
        :type cluster_topology: str (optional)

        :param cluster_my_sqlis_alived: 实例探活检查结果，有两种取值。Yes表示检查通过，No表示检查不通过。
        :type cluster_my_sqlis_alived: str (optional)

        :param cluster_delay: 集群延迟状态检查结果，有两种取值。Yes表示检查通过，No表示检查不通过。
        :type cluster_delay: str (optional)

        :param leader_read_only: 若实例属于热活组，检查热活组内leader是否非只读，follower是否只读
        :type leader_read_only: str (optional)
        """
        super().__init__()
        self.cluster_instance_status = cluster_instance_status
        self.cluster_topology = cluster_topology
        self.cluster_my_sqlis_alived = cluster_my_sqlis_alived
        self.cluster_delay = cluster_delay
        self.leader_read_only = leader_read_only

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.cluster_instance_status is not None:
            result['clusterInstanceStatus'] = self.cluster_instance_status
        if self.cluster_topology is not None:
            result['clusterTopology'] = self.cluster_topology
        if self.cluster_my_sqlis_alived is not None:
            result['clusterMySQLIsAlived'] = self.cluster_my_sqlis_alived
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
        :rtype: CheckStatusResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterInstanceStatus') is not None:
            self.cluster_instance_status = m.get('clusterInstanceStatus')
        if m.get('clusterTopology') is not None:
            self.cluster_topology = m.get('clusterTopology')
        if m.get('clusterMySQLIsAlived') is not None:
            self.cluster_my_sqlis_alived = m.get('clusterMySQLIsAlived')
        if m.get('clusterDelay') is not None:
            self.cluster_delay = m.get('clusterDelay')
        if m.get('leaderReadOnly') is not None:
            self.leader_read_only = m.get('leaderReadOnly')
        return self
