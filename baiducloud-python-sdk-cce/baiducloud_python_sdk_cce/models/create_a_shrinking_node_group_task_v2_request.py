"""
Request entity for CreateAShrinkingNodeGroupTaskV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_cce.models.delete_option import DeleteOption


class CreateAShrinkingNodeGroupTaskV2Request(AbstractModel):
    """
    Request entity for CreateAShrinkingNodeGroupTaskV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        cluster_id,
        instance_group_id,
        instances_to_be_removed,
        k8s_nodes_to_be_removed,
        clean_policy,
        delete_option=None,
    ):
        """
        Initialize CreateAShrinkingNodeGroupTaskV2Request request entity.

        :param cluster_id: cluster_id parameter
        :type cluster_id: str (required)

        :param instance_group_id: instance_group_id parameter
        :type instance_group_id: str (required)

        :param instances_to_be_removed: 缩容节点组时计划从节点组移除的节点 ID 列表
        :type instances_to_be_removed: List[str] (required)

        :param k8s_nodes_to_be_removed: k8s_nodes_to_be_removed parameter
        :type k8s_nodes_to_be_removed: List[str] (required)

        :param clean_policy: 缩容节点组时是否保留节点对应的实例, 可选 [Remain,Delete]
        :type clean_policy: str (required)

        :param delete_option: delete_option parameter
        :type delete_option: DeleteOption (optional)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.instance_group_id = instance_group_id
        self.instances_to_be_removed = instances_to_be_removed
        self.k8s_nodes_to_be_removed = k8s_nodes_to_be_removed
        self.clean_policy = clean_policy
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
        if self.instances_to_be_removed is not None:
            result['instancesToBeRemoved'] = self.instances_to_be_removed
        if self.k8s_nodes_to_be_removed is not None:
            result['k8sNodesToBeRemoved'] = self.k8s_nodes_to_be_removed
        if self.clean_policy is not None:
            result['cleanPolicy'] = self.clean_policy
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
        :rtype: CreateAShrinkingNodeGroupTaskV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterID') is not None:
            self.cluster_id = m.get('clusterID')
        if m.get('instanceGroupID') is not None:
            self.instance_group_id = m.get('instanceGroupID')
        if m.get('instancesToBeRemoved') is not None:
            self.instances_to_be_removed = m.get('instancesToBeRemoved')
        if m.get('k8sNodesToBeRemoved') is not None:
            self.k8s_nodes_to_be_removed = m.get('k8sNodesToBeRemoved')
        if m.get('cleanPolicy') is not None:
            self.clean_policy = m.get('cleanPolicy')
        if m.get('deleteOption') is not None:
            self.delete_option = DeleteOption().from_dict(m.get('deleteOption'))
        return self
