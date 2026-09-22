"""
ShardBandwidth information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ShardBandwidth(AbstractModel):
    """
    ShardBandwidth
    """

    def __init__(self, shard_name=None, node_bandwidth_in_mb=None):
        """
        Initialize ShardBandwidth instance.

        :param shard_name: 分片hashName
        :type shard_name: str (optional)

        :param node_bandwidth_in_mb: 当前分片带宽大小，不能小于默认带宽。增量带宽额外收费。单位：MB。
        :type node_bandwidth_in_mb: int (optional)
        """
        super().__init__()
        self.shard_name = shard_name
        self.node_bandwidth_in_mb = node_bandwidth_in_mb

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
        if self.shard_name is not None:
            result['shardName'] = self.shard_name
        if self.node_bandwidth_in_mb is not None:
            result['nodeBandwidthInMB'] = self.node_bandwidth_in_mb
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ShardBandwidth

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('shardName') is not None:
            self.shard_name = m.get('shardName')
        if m.get('nodeBandwidthInMB') is not None:
            self.node_bandwidth_in_mb = m.get('nodeBandwidthInMB')
        return self
