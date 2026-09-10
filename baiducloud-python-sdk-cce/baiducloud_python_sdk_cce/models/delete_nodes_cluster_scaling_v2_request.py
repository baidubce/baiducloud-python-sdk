"""
Request entity for DeleteNodesClusterScalingV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_cce.models.delete_option import DeleteOption


class DeleteNodesClusterScalingV2Request(AbstractModel):
    """
    Request entity for DeleteNodesClusterScalingV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, cluster_id, instance_ids, delete_option=None, scale_down=None):
        """
        Initialize DeleteNodesClusterScalingV2Request request entity.

        :param cluster_id: cluster_id parameter
        :type cluster_id: str (required)

        :param delete_option: delete_option parameter
        :type delete_option: DeleteOption (optional)

        :param instance_ids: 要删除的节点 ID 列表
        :type instance_ids: List[str] (required)

        :param scale_down: 是否同时减少被删除节点所在节点组的期望节点数
        :type scale_down: bool (optional)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.delete_option = delete_option
        self.instance_ids = instance_ids
        self.scale_down = scale_down

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
        if self.delete_option is not None:
            result['deleteOption'] = self.delete_option.to_dict()
        if self.instance_ids is not None:
            result['instanceIDs'] = self.instance_ids
        if self.scale_down is not None:
            result['scaleDown'] = self.scale_down
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteNodesClusterScalingV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterID') is not None:
            self.cluster_id = m.get('clusterID')
        if m.get('deleteOption') is not None:
            self.delete_option = DeleteOption().from_dict(m.get('deleteOption'))
        if m.get('instanceIDs') is not None:
            self.instance_ids = m.get('instanceIDs')
        if m.get('scaleDown') is not None:
            self.scale_down = m.get('scaleDown')
        return self
