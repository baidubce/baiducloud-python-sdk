"""
Request entity for ModifyTheNumberOfNodeReplicasInANodeGroupV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_cce.models.delete_option import DeleteOption


class ModifyTheNumberOfNodeReplicasInANodeGroupV2Request(AbstractModel):
    """
    Request entity for ModifyTheNumberOfNodeReplicasInANodeGroupV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, cluster_id, instance_group_id, replicas, instance_ids=None, delete_instance=None, delete_option=None
    ):
        """
        Initialize ModifyTheNumberOfNodeReplicasInANodeGroupV2Request request entity.

        :param cluster_id: cluster_id parameter
        :type cluster_id: str (required)

        :param instance_group_id: instance_group_id parameter
        :type instance_group_id: str (required)

        :param replicas: 期望的节点组节点的副本数. 取值范围是自然数集.
        :type replicas: int (required)

        :param instance_ids: 指定被添加或是优先被删除的节点 ID 集合
        :type instance_ids: List[str] (optional)

        :param delete_instance: delete_instance parameter
        :type delete_instance: bool (optional)

        :param delete_option: delete_option parameter
        :type delete_option: DeleteOption (optional)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.instance_group_id = instance_group_id
        self.replicas = replicas
        self.instance_ids = instance_ids
        self.delete_instance = delete_instance
        self.delete_option = delete_option

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
        if self.replicas is not None:
            result['replicas'] = self.replicas
        if self.instance_ids is not None:
            result['instanceIDs'] = self.instance_ids
        if self.delete_instance is not None:
            result['deleteInstance'] = self.delete_instance
        if self.delete_option is not None:
            result['deleteOption'] = self.delete_option.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyTheNumberOfNodeReplicasInANodeGroupV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterID') is not None:
            self.cluster_id = m.get('clusterID')
        if m.get('instanceGroupID') is not None:
            self.instance_group_id = m.get('instanceGroupID')
        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')
        if m.get('instanceIDs') is not None:
            self.instance_ids = m.get('instanceIDs')
        if m.get('deleteInstance') is not None:
            self.delete_instance = m.get('deleteInstance')
        if m.get('deleteOption') is not None:
            self.delete_option = DeleteOption().from_dict(m.get('deleteOption'))
        return self
