"""
CacheClusterNode information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CacheClusterNode(AbstractModel):
    """
    CacheClusterNode
    """

    def __init__(
        self, instance_id=None, flavor_in_gb=None, hash_name=None, domain=None, create_time=None, shard_id=None
    ):
        """
        Initialize CacheClusterNode instance.

        :param instance_id: 分片实例ID
        :type instance_id: str (optional)

        :param flavor_in_gb: 分片规格（GB）
        :type flavor_in_gb: str (optional)

        :param hash_name: 分片名称
        :type hash_name: str (optional)

        :param domain: 社区版集群中独有，绑定了本分片主的IP的域名
        :type domain: str (optional)

        :param create_time: 创建时间（格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC）
        :type create_time: date (optional)

        :param shard_id: 分片ID
        :type shard_id: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.flavor_in_gb = flavor_in_gb
        self.hash_name = hash_name
        self.domain = domain
        self.create_time = create_time
        self.shard_id = shard_id

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
        if self.flavor_in_gb is not None:
            result['flavorInGB'] = self.flavor_in_gb
        if self.hash_name is not None:
            result['hashName'] = self.hash_name
        if self.domain is not None:
            result['domain'] = self.domain
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.shard_id is not None:
            result['shardId'] = self.shard_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CacheClusterNode

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('flavorInGB') is not None:
            self.flavor_in_gb = m.get('flavorInGB')
        if m.get('hashName') is not None:
            self.hash_name = m.get('hashName')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('shardId') is not None:
            self.shard_id = m.get('shardId')
        return self
