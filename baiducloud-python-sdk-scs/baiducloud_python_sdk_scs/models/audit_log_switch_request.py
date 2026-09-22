"""
Request entity for AuditLogSwitchRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AuditLogSwitchRequest(AbstractModel):
    """
    Request entity for AuditLogSwitchRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, action):
        """
        Initialize AuditLogSwitchRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param action: 开关动作。open（开启）、close（关闭）
        :type action: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.action = action

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
        if self.action is not None:
            result['action'] = self.action
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AuditLogSwitchRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('action') is not None:
            self.action = m.get('action')
        return self
