"""
Request entity for GetInstanceSpecListResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_scs.models.node_type_item import NodeTypeItem
from baiducloud_python_sdk_scs.models.node_type_item import NodeTypeItem
from baiducloud_python_sdk_scs.models.node_type_item import NodeTypeItem


class GetInstanceSpecListResponse(BceResponse):
    """
    GetInstanceSpecListResponse
    """

    def __init__(self, default_node_type_list=None, cluster_node_type_list=None, pega_cluster_node_type_list=None):
        """
        Initialize GetInstanceSpecListResponse response.

        :param default_node_type_list: Redis内存型标准版规格
        :type default_node_type_list: List[NodeTypeItem] (optional)

        :param cluster_node_type_list: Redis内存型集群版规格
        :type cluster_node_type_list: List[NodeTypeItem] (optional)

        :param pega_cluster_node_type_list: Redis容量型（PegaDB）集群版规格
        :type pega_cluster_node_type_list: List[NodeTypeItem] (optional)
        """
        super().__init__()
        self.default_node_type_list = default_node_type_list
        self.cluster_node_type_list = cluster_node_type_list
        self.pega_cluster_node_type_list = pega_cluster_node_type_list

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
        if self.default_node_type_list is not None:
            result['defaultNodeTypeList'] = [i.to_dict() for i in self.default_node_type_list]
        if self.cluster_node_type_list is not None:
            result['clusterNodeTypeList'] = [i.to_dict() for i in self.cluster_node_type_list]
        if self.pega_cluster_node_type_list is not None:
            result['pegaClusterNodeTypeList'] = [i.to_dict() for i in self.pega_cluster_node_type_list]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetInstanceSpecListResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('defaultNodeTypeList') is not None:
            self.default_node_type_list = [NodeTypeItem().from_dict(i) for i in m.get('defaultNodeTypeList')]
        if m.get('clusterNodeTypeList') is not None:
            self.cluster_node_type_list = [NodeTypeItem().from_dict(i) for i in m.get('clusterNodeTypeList')]
        if m.get('pegaClusterNodeTypeList') is not None:
            self.pega_cluster_node_type_list = [NodeTypeItem().from_dict(i) for i in m.get('pegaClusterNodeTypeList')]
        return self
