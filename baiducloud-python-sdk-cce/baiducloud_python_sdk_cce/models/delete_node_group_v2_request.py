"""
Request entity for DeleteNodeGroupV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteNodeGroupV2Request(AbstractModel):
    """
    Request entity for DeleteNodeGroupV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, cluster_id, instance_group_id, delete_instances=None, release_all_resource=None):
        """
        Initialize DeleteNodeGroupV2Request request entity.

        :param cluster_id: cluster_id parameter
        :type cluster_id: str (required)

        :param instance_group_id: instance_group_id parameter
        :type instance_group_id: str (required)

        :param delete_instances: delete_instances parameter
        :type delete_instances: bool (optional)

        :param release_all_resource: release_all_resource parameter
        :type release_all_resource: bool (optional)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.instance_group_id = instance_group_id
        self.delete_instances = delete_instances
        self.release_all_resource = release_all_resource

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
        :rtype: DeleteNodeGroupV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterID') is not None:
            self.cluster_id = m.get('clusterID')
        if m.get('instanceGroupID') is not None:
            self.instance_group_id = m.get('instanceGroupID')
        if m.get('deleteInstances') is not None:
            self.delete_instances = m.get('deleteInstances')
        if m.get('releaseAllResource') is not None:
            self.release_all_resource = m.get('releaseAllResource')
        return self
