"""
Request entity for ManuallyModifyBandwidthRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_scs.models.shard_bandwidth import ShardBandwidth


class ManuallyModifyBandwidthRequest(AbstractModel):
    """
    Request entity for ManuallyModifyBandwidthRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, shard_bandwidth_info):
        """
        Initialize ManuallyModifyBandwidthRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param shard_bandwidth_info: 分片带宽列表。
        :type shard_bandwidth_info: List[ShardBandwidth] (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.shard_bandwidth_info = shard_bandwidth_info

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
        if self.shard_bandwidth_info is not None:
            result['shardBandwidthInfo'] = [i.to_dict() for i in self.shard_bandwidth_info]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ManuallyModifyBandwidthRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('shardBandwidthInfo') is not None:
            self.shard_bandwidth_info = [ShardBandwidth().from_dict(i) for i in m.get('shardBandwidthInfo')]
        return self
