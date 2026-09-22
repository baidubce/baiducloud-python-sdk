"""
Request entity for ClusterTypeUpgradeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_scs.models.replication_item import ReplicationItem


class ClusterTypeUpgradeRequest(AbstractModel):
    """
    Request entity for ClusterTypeUpgradeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, is_defer=None, node_type=None, shard_num=None, replication_info=None):
        """
        Initialize ClusterTypeUpgradeRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param is_defer: 是否维护时间内执行。默认false。true：维护时间内执行；false：立即执行。
        :type is_defer: bool (optional)

        :param node_type: node_type parameter
        :type node_type: str (optional)

        :param shard_num: 分片数量。<li>可以设置新的分片数量；<li>可以为空，默认为原实例分片数。
        :type shard_num: int (optional)

        :param replication_info: replication_info parameter
        :type replication_info: List[ReplicationItem] (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.is_defer = is_defer
        self.node_type = node_type
        self.shard_num = shard_num
        self.replication_info = replication_info

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
        if self.is_defer is not None:
            result['isDefer'] = self.is_defer
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.shard_num is not None:
            result['shardNum'] = self.shard_num
        if self.replication_info is not None:
            result['replicationInfo'] = [i.to_dict() for i in self.replication_info]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ClusterTypeUpgradeRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isDefer') is not None:
            self.is_defer = m.get('isDefer')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('shardNum') is not None:
            self.shard_num = m.get('shardNum')
        if m.get('replicationInfo') is not None:
            self.replication_info = [ReplicationItem().from_dict(i) for i in m.get('replicationInfo')]
        return self
