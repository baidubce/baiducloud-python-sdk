"""
Request entity for CreateNodesClusterExpansionV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_cce.models.instance_set import InstanceSet


class CreateNodesClusterExpansionV2Request(AbstractModel):
    """
    Request entity for CreateNodesClusterExpansionV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, cluster_id, request_body_):
        """
        Initialize CreateNodesClusterExpansionV2Request request entity.

        :param cluster_id: cluster_id parameter
        :type cluster_id: str (required)

        :param request_body_: 为集群增加的节点列表
        :type request_body_: List[InstanceSet] (required)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.request_body_ = request_body_

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
        if self.request_body_ is not None:
            result['无（RequestBody 为数组）'] = [i.to_dict() for i in self.request_body_]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateNodesClusterExpansionV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterID') is not None:
            self.cluster_id = m.get('clusterID')
        if m.get('无（RequestBody 为数组）') is not None:
            self.request_body_ = [InstanceSet().from_dict(i) for i in m.get('无（RequestBody 为数组）')]
        return self
