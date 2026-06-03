"""
Request entity for AddCacheNodesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class AddCacheNodesResponse(BceResponse):
    """
    AddCacheNodesResponse
    """

    def __init__(self, cache_node_ids=None):
        """
        Initialize AddCacheNodesResponse response.

        :param cache_node_ids: 成功添加的 CacheNode ID 列表
        :type cache_node_ids: List[str] (optional)
        """
        super().__init__()
        self.cache_node_ids = cache_node_ids

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.cache_node_ids is not None:
            result['cacheNodeIds'] = self.cache_node_ids
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AddCacheNodesResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cacheNodeIds') is not None:
            self.cache_node_ids = m.get('cacheNodeIds')
        return self
