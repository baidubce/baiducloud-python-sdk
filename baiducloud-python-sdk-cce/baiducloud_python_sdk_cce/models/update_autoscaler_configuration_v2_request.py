"""
Request entity for UpdateAutoscalerConfigurationV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateAutoscalerConfigurationV2Request(AbstractModel):
    """
    Request entity for UpdateAutoscalerConfigurationV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        cluster_id,
        expander,
        instance_groups=None,
        kube_version=None,
        max_empty_bulk_delete=None,
        scale_down_delay_after_add=None,
        scale_down_enabled=None,
        scale_down_gpu_utilization_threshold=None,
        scale_down_unneeded_time=None,
        scale_down_utilization_threshold=None,
        skip_nodes_with_local_storage=None,
        skip_nodes_with_system_pods=None,
        custom_configs=None,
    ):
        """
        Initialize UpdateAutoscalerConfigurationV2Request request entity.

        :param cluster_id: cluster_id parameter
        :type cluster_id: str (required)

        :param expander: expander parameter
        :type expander: str (required)

        :param instance_groups: 节点组的 Autoscaler 配置。用户无需输入此项内容。
        :type instance_groups: List[object] (optional)

        :param kube_version: K8S 版本。为空时，后台会自动查询集群 K8S 版本号。
        :type kube_version: str (optional)

        :param max_empty_bulk_delete: 最大并发缩容数
        :type max_empty_bulk_delete: int (optional)

        :param scale_down_delay_after_add: 扩容后缩容启动时延，单位为分钟
        :type scale_down_delay_after_add: int (optional)

        :param scale_down_enabled: 是否启用缩容。默认值为 false。
        :type scale_down_enabled: bool (optional)

        :param scale_down_gpu_utilization_threshold: GPU 缩容阈值百分比，取值范围为 (0, 100)。
        :type scale_down_gpu_utilization_threshold: int (optional)

        :param scale_down_unneeded_time: 缩容触发时延，单位为分钟。
        :type scale_down_unneeded_time: int (optional)

        :param scale_down_utilization_threshold: 缩容阈值百分比，取值范围为 (0, 100)。
        :type scale_down_utilization_threshold: int (optional)

        :param skip_nodes_with_local_storage: 是否跳过使用本地存储的节点。默认值为 true。
        :type skip_nodes_with_local_storage: bool (optional)

        :param skip_nodes_with_system_pods: 是否跳过有部署系统 Pod 的节点。默认值为 true。
        :type skip_nodes_with_system_pods: bool (optional)

        :param custom_configs: 用户自定义配置。
        :type custom_configs: Dict[str, str] (optional)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.expander = expander
        self.instance_groups = instance_groups
        self.kube_version = kube_version
        self.max_empty_bulk_delete = max_empty_bulk_delete
        self.scale_down_delay_after_add = scale_down_delay_after_add
        self.scale_down_enabled = scale_down_enabled
        self.scale_down_gpu_utilization_threshold = scale_down_gpu_utilization_threshold
        self.scale_down_unneeded_time = scale_down_unneeded_time
        self.scale_down_utilization_threshold = scale_down_utilization_threshold
        self.skip_nodes_with_local_storage = skip_nodes_with_local_storage
        self.skip_nodes_with_system_pods = skip_nodes_with_system_pods
        self.custom_configs = custom_configs

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
        if self.expander is not None:
            result['expander'] = self.expander
        if self.instance_groups is not None:
            result['instanceGroups'] = self.instance_groups
        if self.kube_version is not None:
            result['kubeVersion'] = self.kube_version
        if self.max_empty_bulk_delete is not None:
            result['maxEmptyBulkDelete'] = self.max_empty_bulk_delete
        if self.scale_down_delay_after_add is not None:
            result['scaleDownDelayAfterAdd'] = self.scale_down_delay_after_add
        if self.scale_down_enabled is not None:
            result['scaleDownEnabled'] = self.scale_down_enabled
        if self.scale_down_gpu_utilization_threshold is not None:
            result['scaleDownGPUUtilizationThreshold'] = self.scale_down_gpu_utilization_threshold
        if self.scale_down_unneeded_time is not None:
            result['scaleDownUnneededTime'] = self.scale_down_unneeded_time
        if self.scale_down_utilization_threshold is not None:
            result['scaleDownUtilizationThreshold'] = self.scale_down_utilization_threshold
        if self.skip_nodes_with_local_storage is not None:
            result['skipNodesWithLocalStorage'] = self.skip_nodes_with_local_storage
        if self.skip_nodes_with_system_pods is not None:
            result['skipNodesWithSystemPods'] = self.skip_nodes_with_system_pods
        if self.custom_configs is not None:
            result['customConfigs'] = self.custom_configs
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateAutoscalerConfigurationV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterID') is not None:
            self.cluster_id = m.get('clusterID')
        if m.get('expander') is not None:
            self.expander = m.get('expander')
        if m.get('instanceGroups') is not None:
            self.instance_groups = m.get('instanceGroups')
        if m.get('kubeVersion') is not None:
            self.kube_version = m.get('kubeVersion')
        if m.get('maxEmptyBulkDelete') is not None:
            self.max_empty_bulk_delete = m.get('maxEmptyBulkDelete')
        if m.get('scaleDownDelayAfterAdd') is not None:
            self.scale_down_delay_after_add = m.get('scaleDownDelayAfterAdd')
        if m.get('scaleDownEnabled') is not None:
            self.scale_down_enabled = m.get('scaleDownEnabled')
        if m.get('scaleDownGPUUtilizationThreshold') is not None:
            self.scale_down_gpu_utilization_threshold = m.get('scaleDownGPUUtilizationThreshold')
        if m.get('scaleDownUnneededTime') is not None:
            self.scale_down_unneeded_time = m.get('scaleDownUnneededTime')
        if m.get('scaleDownUtilizationThreshold') is not None:
            self.scale_down_utilization_threshold = m.get('scaleDownUtilizationThreshold')
        if m.get('skipNodesWithLocalStorage') is not None:
            self.skip_nodes_with_local_storage = m.get('skipNodesWithLocalStorage')
        if m.get('skipNodesWithSystemPods') is not None:
            self.skip_nodes_with_system_pods = m.get('skipNodesWithSystemPods')
        if m.get('customConfigs') is not None:
            self.custom_configs = m.get('customConfigs')
        return self
