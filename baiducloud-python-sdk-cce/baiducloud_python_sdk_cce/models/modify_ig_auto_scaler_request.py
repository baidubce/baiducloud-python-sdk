"""
Request entity for ModifyIGAutoScalerRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyIGAutoScalerRequest(AbstractModel):
    """
    Request entity for ModifyIGAutoScalerRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, cluster_id, instance_group_id, enabled, max_replicas, min_replicas=None, scaling_group_priority=None
    ):
        """
        Initialize ModifyIGAutoScalerRequest request entity.

        :param cluster_id: cluster_id parameter
        :type cluster_id: str (required)

        :param instance_group_id: instance_group_id parameter
        :type instance_group_id: str (required)

        :param enabled: 是否启用Autoscaler
        :type enabled: bool (required)

        :param min_replicas: 最小副本数. 取值范围是自然数集, 默认值为0.
        :type min_replicas: int (optional)

        :param max_replicas: 最大副本数. 取值范围是自然数集, 需大于minReplicas.
        :type max_replicas: int (required)

        :param scaling_group_priority: 伸缩组优先级. 取值范围是自然数集,默认值为0.
        :type scaling_group_priority: int (optional)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.instance_group_id = instance_group_id
        self.enabled = enabled
        self.min_replicas = min_replicas
        self.max_replicas = max_replicas
        self.scaling_group_priority = scaling_group_priority

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
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.min_replicas is not None:
            result['minReplicas'] = self.min_replicas
        if self.max_replicas is not None:
            result['maxReplicas'] = self.max_replicas
        if self.scaling_group_priority is not None:
            result['scalingGroupPriority'] = self.scaling_group_priority
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyIGAutoScalerRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterID') is not None:
            self.cluster_id = m.get('clusterID')
        if m.get('instanceGroupID') is not None:
            self.instance_group_id = m.get('instanceGroupID')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('minReplicas') is not None:
            self.min_replicas = m.get('minReplicas')
        if m.get('maxReplicas') is not None:
            self.max_replicas = m.get('maxReplicas')
        if m.get('scalingGroupPriority') is not None:
            self.scaling_group_priority = m.get('scalingGroupPriority')
        return self
