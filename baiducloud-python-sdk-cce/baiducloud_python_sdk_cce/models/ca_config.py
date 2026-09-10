"""
CAConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CAConfig(AbstractModel):
    """
    CAConfig
    """

    def __init__(
        self,
        replica_count=None,
        scale_down_enabled=None,
        scale_down_utilization_threshold=None,
        scale_down_gpu_utilization_threshold=None,
        scale_down_unneeded_time=None,
        scale_down_delay_after_add=None,
        max_empty_bulk_delete=None,
        skip_nodes_with_local_storage=None,
        skip_nodes_with_system_pods=None,
        expander=None,
        custom_configs=None,
    ):
        """
        Initialize CAConfig instance.

        :param replica_count:
        :type replica_count: int (optional)

        :param scale_down_enabled:
        :type scale_down_enabled: bool (optional)

        :param scale_down_utilization_threshold:
        :type scale_down_utilization_threshold: int (optional)

        :param scale_down_gpu_utilization_threshold:
        :type scale_down_gpu_utilization_threshold: int (optional)

        :param scale_down_unneeded_time:
        :type scale_down_unneeded_time: int (optional)

        :param scale_down_delay_after_add:
        :type scale_down_delay_after_add: int (optional)

        :param max_empty_bulk_delete:
        :type max_empty_bulk_delete: int (optional)

        :param skip_nodes_with_local_storage:
        :type skip_nodes_with_local_storage: bool (optional)

        :param skip_nodes_with_system_pods:
        :type skip_nodes_with_system_pods: bool (optional)

        :param expander:
        :type expander: str (optional)

        :param custom_configs:
        :type custom_configs: Dict[str, str] (optional)
        """
        super().__init__()
        self.replica_count = replica_count
        self.scale_down_enabled = scale_down_enabled
        self.scale_down_utilization_threshold = scale_down_utilization_threshold
        self.scale_down_gpu_utilization_threshold = scale_down_gpu_utilization_threshold
        self.scale_down_unneeded_time = scale_down_unneeded_time
        self.scale_down_delay_after_add = scale_down_delay_after_add
        self.max_empty_bulk_delete = max_empty_bulk_delete
        self.skip_nodes_with_local_storage = skip_nodes_with_local_storage
        self.skip_nodes_with_system_pods = skip_nodes_with_system_pods
        self.expander = expander
        self.custom_configs = custom_configs

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
        if self.replica_count is not None:
            result['replicaCount'] = self.replica_count
        if self.scale_down_enabled is not None:
            result['scaleDownEnabled'] = self.scale_down_enabled
        if self.scale_down_utilization_threshold is not None:
            result['scaleDownUtilizationThreshold'] = self.scale_down_utilization_threshold
        if self.scale_down_gpu_utilization_threshold is not None:
            result['scaleDownGPUUtilizationThreshold'] = self.scale_down_gpu_utilization_threshold
        if self.scale_down_unneeded_time is not None:
            result['scaleDownUnneededTime'] = self.scale_down_unneeded_time
        if self.scale_down_delay_after_add is not None:
            result['scaleDownDelayAfterAdd'] = self.scale_down_delay_after_add
        if self.max_empty_bulk_delete is not None:
            result['maxEmptyBulkDelete'] = self.max_empty_bulk_delete
        if self.skip_nodes_with_local_storage is not None:
            result['skipNodesWithLocalStorage'] = self.skip_nodes_with_local_storage
        if self.skip_nodes_with_system_pods is not None:
            result['skipNodesWithSystemPods'] = self.skip_nodes_with_system_pods
        if self.expander is not None:
            result['expander'] = self.expander
        if self.custom_configs is not None:
            result['customConfigs'] = self.custom_configs
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CAConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('replicaCount') is not None:
            self.replica_count = m.get('replicaCount')
        if m.get('scaleDownEnabled') is not None:
            self.scale_down_enabled = m.get('scaleDownEnabled')
        if m.get('scaleDownUtilizationThreshold') is not None:
            self.scale_down_utilization_threshold = m.get('scaleDownUtilizationThreshold')
        if m.get('scaleDownGPUUtilizationThreshold') is not None:
            self.scale_down_gpu_utilization_threshold = m.get('scaleDownGPUUtilizationThreshold')
        if m.get('scaleDownUnneededTime') is not None:
            self.scale_down_unneeded_time = m.get('scaleDownUnneededTime')
        if m.get('scaleDownDelayAfterAdd') is not None:
            self.scale_down_delay_after_add = m.get('scaleDownDelayAfterAdd')
        if m.get('maxEmptyBulkDelete') is not None:
            self.max_empty_bulk_delete = m.get('maxEmptyBulkDelete')
        if m.get('skipNodesWithLocalStorage') is not None:
            self.skip_nodes_with_local_storage = m.get('skipNodesWithLocalStorage')
        if m.get('skipNodesWithSystemPods') is not None:
            self.skip_nodes_with_system_pods = m.get('skipNodesWithSystemPods')
        if m.get('expander') is not None:
            self.expander = m.get('expander')
        if m.get('customConfigs') is not None:
            self.custom_configs = m.get('customConfigs')
        return self
