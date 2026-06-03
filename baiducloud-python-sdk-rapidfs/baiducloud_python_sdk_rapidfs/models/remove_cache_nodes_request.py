"""
Request entity for RemoveCacheNodesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RemoveCacheNodesRequest(AbstractModel):
    """
    Request entity for RemoveCacheNodesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, cache_node_ids, client_token=None, force_remove_on_offline=None):
        """
        Initialize RemoveCacheNodesRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param instance_id: RapidFS 实例 ID
        :type instance_id: str (required)

        :param cache_node_ids: 待移除的 CacheNode ID 列表
        :type cache_node_ids: List[str] (required)

        :param force_remove_on_offline: 节点连接状态离线时，是否强制移除
        :type force_remove_on_offline: bool (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.instance_id = instance_id
        self.cache_node_ids = cache_node_ids
        self.force_remove_on_offline = force_remove_on_offline

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.cache_node_ids is not None:
            result['cacheNodeIds'] = self.cache_node_ids
        if self.force_remove_on_offline is not None:
            result['forceRemoveOnOffline'] = self.force_remove_on_offline
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RemoveCacheNodesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('cacheNodeIds') is not None:
            self.cache_node_ids = m.get('cacheNodeIds')
        if m.get('forceRemoveOnOffline') is not None:
            self.force_remove_on_offline = m.get('forceRemoveOnOffline')
        return self
