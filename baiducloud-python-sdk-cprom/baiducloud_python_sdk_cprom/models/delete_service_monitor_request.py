"""
Request entity for DeleteServiceMonitorRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteServiceMonitorRequest(AbstractModel):
    """
    Request entity for DeleteServiceMonitorRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, service_monitor_name, instance_id, agent_id):
        """
        Initialize DeleteServiceMonitorRequest request entity.

        :param service_monitor_name: service_monitor_name parameter
        :type service_monitor_name: str (required)

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param agent_id: agent_id parameter
        :type agent_id: str (required)
        """
        super().__init__()
        self.service_monitor_name = service_monitor_name
        self.instance_id = instance_id
        self.agent_id = agent_id

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
        :rtype: DeleteServiceMonitorRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('serviceMonitorName') is not None:
            self.service_monitor_name = m.get('serviceMonitorName')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        return self
