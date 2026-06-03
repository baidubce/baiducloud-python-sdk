"""
Request entity for AddCacheNodesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_rapidfs.models.add_cache_node_info import AddCacheNodeInfo


class AddCacheNodesRequest(AbstractModel):
    """
    Request entity for AddCacheNodesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, cache_nodes, client_token=None, type=None):
        """
        Initialize AddCacheNodesRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param instance_id: RapidFS 实例 ID
        :type instance_id: str (required)

        :param type: type parameter
        :type type: str (optional)

        :param cache_nodes: 待添加的节点信息列表，见附录 AddCacheNodeInfo
        :type cache_nodes: List[AddCacheNodeInfo] (required)
        """
        super().__init__()
        self.client_token = client_token
        self.instance_id = instance_id
        self.type = type
        self.cache_nodes = cache_nodes

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
        if self.type is not None:
            result['type'] = self.type
        if self.cache_nodes is not None:
            result['cacheNodes'] = [i.to_dict() for i in self.cache_nodes]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AddCacheNodesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('cacheNodes') is not None:
            self.cache_nodes = [AddCacheNodeInfo().from_dict(i) for i in m.get('cacheNodes')]
        return self
