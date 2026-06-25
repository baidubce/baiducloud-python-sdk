"""
Request entity for CreatePodmonitorRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_cprom.models.object_meta import ObjectMeta
from baiducloud_python_sdk_cprom.models.pod_monitor_spec import PodMonitorSpec


class CreatePodmonitorRequest(AbstractModel):
    """
    Request entity for CreatePodmonitorRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, agent_id, api_version, kind, metadata, spec):
        """
        Initialize CreatePodmonitorRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param agent_id: agent_id parameter
        :type agent_id: str (required)

        :param api_version: 固定值：monitoring.coreos.com/v1
        :type api_version: str (required)

        :param kind: 固定值：PodMonitor
        :type kind: str (required)

        :param metadata: metadata parameter
        :type metadata: ObjectMeta (required)

        :param spec: spec parameter
        :type spec: PodMonitorSpec (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.agent_id = agent_id
        self.api_version = api_version
        self.kind = kind
        self.metadata = metadata
        self.spec = spec

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
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_dict()
        if self.spec is not None:
            result['spec'] = self.spec.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreatePodmonitorRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            self.metadata = ObjectMeta().from_dict(m.get('metadata'))
        if m.get('spec') is not None:
            self.spec = PodMonitorSpec().from_dict(m.get('spec'))
        return self
