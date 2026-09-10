"""
ClusterAutoscalerSpec information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ClusterAutoscalerSpec(AbstractModel):
    """
    ClusterAutoscalerSpec
    """

    def __init__(self, enabled=None, min_replicas=None, max_replicas=None, scaling_group_priority=None):
        """
        Initialize ClusterAutoscalerSpec instance.

        :param enabled:
        :type enabled: bool (optional)

        :param min_replicas:
        :type min_replicas: int (optional)

        :param max_replicas:
        :type max_replicas: int (optional)

        :param scaling_group_priority:
        :type scaling_group_priority: int (optional)
        """
        super().__init__()
        self.enabled = enabled
        self.min_replicas = min_replicas
        self.max_replicas = max_replicas
        self.scaling_group_priority = scaling_group_priority

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
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
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ClusterAutoscalerSpec

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('minReplicas') is not None:
            self.min_replicas = m.get('minReplicas')
        if m.get('maxReplicas') is not None:
            self.max_replicas = m.get('maxReplicas')
        if m.get('scalingGroupPriority') is not None:
            self.scaling_group_priority = m.get('scalingGroupPriority')
        return self
