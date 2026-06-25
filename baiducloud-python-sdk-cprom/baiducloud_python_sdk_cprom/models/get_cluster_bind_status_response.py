"""
Request entity for GetClusterBindStatusResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetClusterBindStatusResponse(BceResponse):
    """
    GetClusterBindStatusResponse
    """

    def __init__(self, binding_status=None, instance_id=None, agent_id=None):
        """
        Initialize GetClusterBindStatusResponse response.

        :param binding_status: binding_status field
        :type binding_status: str (optional)

        :param instance_id: CProm 监控实例 ID。
        :type instance_id: str (optional)

        :param agent_id: Agent ID。
        :type agent_id: str (optional)
        """
        super().__init__()
        self.binding_status = binding_status
        self.instance_id = instance_id
        self.agent_id = agent_id

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.binding_status is not None:
            result['bindingStatus'] = self.binding_status
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.agent_id is not None:
            result['agentId'] = self.agent_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetClusterBindStatusResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('bindingStatus') is not None:
            self.binding_status = m.get('bindingStatus')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        return self
