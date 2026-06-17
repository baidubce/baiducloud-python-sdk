"""
Request entity for CheckServerEventRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CheckServerEventRequest(AbstractModel):
    """
    Request entity for CheckServerEventRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        action,
        check_result,
        server_event_id=None,
        instance_id=None,
        issue_effect=None,
        issue_description=None,
        authorize_maintenance_operation=None,
    ):
        """
        Initialize CheckServerEventRequest request entity.

        :param action: action parameter
        :type action: str (required)

        :param server_event_id: 维修事件ID，serverEventId、instanceId必须选择其中一个请求
        :type server_event_id: str (optional)

        :param instance_id: 实例ID，serverEventId、instanceId必须选择其中一个请求
        :type instance_id: str (optional)

        :param check_result: 非预期事件是否通过验收，通过：Pass；不通过：Reject。
        :type check_result: str (required)

        :param issue_effect: 故障影响，故障验收为Reject时必传
        :type issue_effect: str (optional)

        :param issue_description: 故障影响，故障验收为Reject时必传
        :type issue_description: str (optional)

        :param authorize_maintenance_operation: 故障验收为Reject时授权的运维操作
        :type authorize_maintenance_operation: str (optional)
        """
        super().__init__()
        self.action = action
        self.server_event_id = server_event_id
        self.instance_id = instance_id
        self.check_result = check_result
        self.issue_effect = issue_effect
        self.issue_description = issue_description
        self.authorize_maintenance_operation = authorize_maintenance_operation

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
        if self.server_event_id is not None:
            result['serverEventId'] = self.server_event_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.check_result is not None:
            result['checkResult'] = self.check_result
        if self.issue_effect is not None:
            result['issueEffect'] = self.issue_effect
        if self.issue_description is not None:
            result['issueDescription'] = self.issue_description
        if self.authorize_maintenance_operation is not None:
            result['authorizeMaintenanceOperation'] = self.authorize_maintenance_operation
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CheckServerEventRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('serverEventId') is not None:
            self.server_event_id = m.get('serverEventId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('checkResult') is not None:
            self.check_result = m.get('checkResult')
        if m.get('issueEffect') is not None:
            self.issue_effect = m.get('issueEffect')
        if m.get('issueDescription') is not None:
            self.issue_description = m.get('issueDescription')
        if m.get('authorizeMaintenanceOperation') is not None:
            self.authorize_maintenance_operation = m.get('authorizeMaintenanceOperation')
        return self
