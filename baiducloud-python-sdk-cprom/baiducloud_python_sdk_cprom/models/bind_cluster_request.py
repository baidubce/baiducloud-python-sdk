"""
Request entity for BindClusterRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BindClusterRequest(AbstractModel):
    """
    Request entity for BindClusterRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, action, cluster_id):
        """
        Initialize BindClusterRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param action: action parameter
        :type action: str (required)

        :param cluster_id: CCE 集群 ID。
        :type cluster_id: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.action = action
        self.cluster_id = cluster_id

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
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BindClusterRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        return self
