"""
Request entity for UpdatePodMonitorRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_cprom.models.pod_monitor import PodMonitor


class UpdatePodMonitorRequest(AbstractModel):
    """
    Request entity for UpdatePodMonitorRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, pod_monitor_name, instance_id, agent_id, enable, pod_monitor):
        """
        Initialize UpdatePodMonitorRequest request entity.

        :param pod_monitor_name: pod_monitor_name parameter
        :type pod_monitor_name: str (required)

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param agent_id: agent_id parameter
        :type agent_id: str (required)

        :param enable: 是否启用：true/false
        :type enable: str (required)

        :param pod_monitor: pod_monitor parameter
        :type pod_monitor: PodMonitor (required)
        """
        super().__init__()
        self.pod_monitor_name = pod_monitor_name
        self.instance_id = instance_id
        self.agent_id = agent_id
        self.enable = enable
        self.pod_monitor = pod_monitor

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
        if self.enable is not None:
            result['enable'] = self.enable
        if self.pod_monitor is not None:
            result['podMonitor'] = self.pod_monitor.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdatePodMonitorRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('podMonitorName') is not None:
            self.pod_monitor_name = m.get('podMonitorName')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('podMonitor') is not None:
            self.pod_monitor = PodMonitor().from_dict(m.get('podMonitor'))
        return self
