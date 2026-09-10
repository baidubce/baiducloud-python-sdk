"""
Request entity for CreateExpansionNodeGroupTaskV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateExpansionNodeGroupTaskV2Request(AbstractModel):
    """
    Request entity for CreateExpansionNodeGroupTaskV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, cluster_id, instance_group_id, up_to_replicas=None, up_replicas=None):
        """
        Initialize CreateExpansionNodeGroupTaskV2Request request entity.

        :param cluster_id: cluster_id parameter
        :type cluster_id: str (required)

        :param instance_group_id: instance_group_id parameter
        :type instance_group_id: str (required)

        :param up_to_replicas: up_to_replicas parameter
        :type up_to_replicas: int (optional)

        :param up_replicas: up_replicas parameter
        :type up_replicas: int (optional)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.instance_group_id = instance_group_id
        self.up_to_replicas = up_to_replicas
        self.up_replicas = up_replicas

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateExpansionNodeGroupTaskV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterID') is not None:
            self.cluster_id = m.get('clusterID')
        if m.get('instanceGroupID') is not None:
            self.instance_group_id = m.get('instanceGroupID')
        if m.get('upToReplicas') is not None:
            self.up_to_replicas = m.get('upToReplicas')
        if m.get('upReplicas') is not None:
            self.up_replicas = m.get('upReplicas')
        return self
