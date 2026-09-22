"""
RedisNode information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RedisNode(AbstractModel):
    """
    RedisNode
    """

    def __init__(
        self,
        uuid=None,
        node_show_id=None,
        cache_instance_type=None,
        is_read_only=None,
        in_group=None,
        availability_zone=None,
        subnet_id=None,
        status=None,
        weight=None,
        hash_name=None,
        shard_id=None,
        node_id=None,
    ):
        """
        Initialize RedisNode instance.

        :param uuid: 节点UUID
        :type uuid: str (optional)

        :param node_show_id: 节点展示ID
        :type node_show_id: str (optional)

        :param cache_instance_type: 实例类型：0 proxy代理、2 redis从、3 redis主（还有1、4、5，主要关注 0/2/3）
        :type cache_instance_type: int (optional)

        :param is_read_only: 是否只读实例：0 不是，1 是
        :type is_read_only: int (optional)

        :param in_group: 是否在只读组中：0 不在，1 在
        :type in_group: int (optional)

        :param availability_zone: 可用区
        :type availability_zone: str (optional)

        :param subnet_id: 子网短ID
        :type subnet_id: str (optional)

        :param status: status attribute
        :type status: int (optional)

        :param weight: 权重
        :type weight: int (optional)

        :param hash_name: 分片名称
        :type hash_name: str (optional)

        :param shard_id: 分片ID
        :type shard_id: int (optional)

        :param node_id: 节点ID
        :type node_id: int (optional)
        """
        super().__init__()
        self.uuid = uuid
        self.node_show_id = node_show_id
        self.cache_instance_type = cache_instance_type
        self.is_read_only = is_read_only
        self.in_group = in_group
        self.availability_zone = availability_zone
        self.subnet_id = subnet_id
        self.status = status
        self.weight = weight
        self.hash_name = hash_name
        self.shard_id = shard_id
        self.node_id = node_id

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
        if self.uuid is not None:
            result['uuid'] = self.uuid
        if self.node_show_id is not None:
            result['nodeShowId'] = self.node_show_id
        if self.cache_instance_type is not None:
            result['cacheInstanceType'] = self.cache_instance_type
        if self.is_read_only is not None:
            result['isReadOnly'] = self.is_read_only
        if self.in_group is not None:
            result['inGroup'] = self.in_group
        if self.availability_zone is not None:
            result['availabilityZone'] = self.availability_zone
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.status is not None:
            result['status'] = self.status
        if self.weight is not None:
            result['weight'] = self.weight
        if self.hash_name is not None:
            result['hashName'] = self.hash_name
        if self.shard_id is not None:
            result['shardId'] = self.shard_id
        if self.node_id is not None:
            result['nodeId'] = self.node_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RedisNode

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        if m.get('nodeShowId') is not None:
            self.node_show_id = m.get('nodeShowId')
        if m.get('cacheInstanceType') is not None:
            self.cache_instance_type = m.get('cacheInstanceType')
        if m.get('isReadOnly') is not None:
            self.is_read_only = m.get('isReadOnly')
        if m.get('inGroup') is not None:
            self.in_group = m.get('inGroup')
        if m.get('availabilityZone') is not None:
            self.availability_zone = m.get('availabilityZone')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        if m.get('hashName') is not None:
            self.hash_name = m.get('hashName')
        if m.get('shardId') is not None:
            self.shard_id = m.get('shardId')
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')
        return self
