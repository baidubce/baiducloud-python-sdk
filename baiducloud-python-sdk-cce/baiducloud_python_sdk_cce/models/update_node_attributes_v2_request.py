"""
Request entity for UpdateNodeAttributesV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_cce.models.taint import Taint


class UpdateNodeAttributesV2Request(AbstractModel):
    """
    Request entity for UpdateNodeAttributesV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, cluster_id, instance_id, labels, taints, cce_instance_priority, annotations=None):
        """
        Initialize UpdateNodeAttributesV2Request request entity.

        :param cluster_id: cluster_id parameter
        :type cluster_id: str (required)

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param labels: 节点的标签
        :type labels: Dict[str, str] (required)

        :param annotations: 节点的注解
        :type annotations: Dict[str, str] (optional)

        :param taints: 节点的污点
        :type taints: List[Taint] (required)

        :param cce_instance_priority: 节点的优先级
        :type cce_instance_priority: int (required)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.instance_id = instance_id
        self.labels = labels
        self.annotations = annotations
        self.taints = taints
        self.cce_instance_priority = cce_instance_priority

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
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.taints is not None:
            result['taints'] = [i.to_dict() for i in self.taints]
        if self.cce_instance_priority is not None:
            result['cceInstancePriority'] = self.cce_instance_priority
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateNodeAttributesV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterID') is not None:
            self.cluster_id = m.get('clusterID')
        if m.get('instanceID') is not None:
            self.instance_id = m.get('instanceID')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('taints') is not None:
            self.taints = [Taint().from_dict(i) for i in m.get('taints')]
        if m.get('cceInstancePriority') is not None:
            self.cce_instance_priority = m.get('cceInstancePriority')
        return self
