"""
Request entity for CreateNodeGroupV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_cce.models.instance_template import InstanceTemplate
from baiducloud_python_sdk_cce.models.cluster_autoscaler_spec import ClusterAutoscalerSpec


class CreateNodeGroupV2Request(AbstractModel):
    """
    Request entity for CreateNodeGroupV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        cluster_id,
        instance_group_name,
        instance_template,
        replicas,
        cluster_role=None,
        shrink_policy=None,
        update_policy=None,
        clean_policy=None,
        cluster_autoscaler_spec=None,
    ):
        """
        Initialize CreateNodeGroupV2Request request entity.

        :param cluster_id: cluster_id parameter
        :type cluster_id: str (required)

        :param instance_group_name: 节点组名称，不可为空
        :type instance_group_name: str (required)

        :param cluster_role: 节点在集群中的角色. 目前仅支持Node类型阶段组, 默认值为node
        :type cluster_role: str (optional)

        :param shrink_policy: shrink_policy parameter
        :type shrink_policy: str (optional)

        :param update_policy: update_policy parameter
        :type update_policy: str (optional)

        :param clean_policy: 节点清理规则. 可选 [ Remain, Delete ]. 默认为 Delete.
        :type clean_policy: str (optional)

        :param instance_template: instance_template parameter
        :type instance_template: InstanceTemplate (required)

        :param replicas: 节点组节点要求的副本数. 取值范围是自然数集
        :type replicas: int (required)

        :param cluster_autoscaler_spec: cluster_autoscaler_spec parameter
        :type cluster_autoscaler_spec: ClusterAutoscalerSpec (optional)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.instance_group_name = instance_group_name
        self.cluster_role = cluster_role
        self.shrink_policy = shrink_policy
        self.update_policy = update_policy
        self.clean_policy = clean_policy
        self.instance_template = instance_template
        self.replicas = replicas
        self.cluster_autoscaler_spec = cluster_autoscaler_spec

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
        if self.instance_group_name is not None:
            result['instanceGroupName'] = self.instance_group_name
        if self.cluster_role is not None:
            result['clusterRole'] = self.cluster_role
        if self.shrink_policy is not None:
            result['shrinkPolicy'] = self.shrink_policy
        if self.update_policy is not None:
            result['updatePolicy'] = self.update_policy
        if self.clean_policy is not None:
            result['cleanPolicy'] = self.clean_policy
        if self.instance_template is not None:
            result['instanceTemplate'] = self.instance_template.to_dict()
        if self.replicas is not None:
            result['replicas'] = self.replicas
        if self.cluster_autoscaler_spec is not None:
            result['clusterAutoscalerSpec'] = self.cluster_autoscaler_spec.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateNodeGroupV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterID') is not None:
            self.cluster_id = m.get('clusterID')
        if m.get('instanceGroupName') is not None:
            self.instance_group_name = m.get('instanceGroupName')
        if m.get('clusterRole') is not None:
            self.cluster_role = m.get('clusterRole')
        if m.get('shrinkPolicy') is not None:
            self.shrink_policy = m.get('shrinkPolicy')
        if m.get('updatePolicy') is not None:
            self.update_policy = m.get('updatePolicy')
        if m.get('cleanPolicy') is not None:
            self.clean_policy = m.get('cleanPolicy')
        if m.get('instanceTemplate') is not None:
            self.instance_template = InstanceTemplate().from_dict(m.get('instanceTemplate'))
        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')
        if m.get('clusterAutoscalerSpec') is not None:
            self.cluster_autoscaler_spec = ClusterAutoscalerSpec().from_dict(m.get('clusterAutoscalerSpec'))
        return self
