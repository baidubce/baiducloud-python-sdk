"""
Request entity for AuthorizeServerEventRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AuthorizeServerEventRequest(AbstractModel):
    """
    Request entity for AuthorizeServerEventRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, action, server_event_id=None, instance_id=None, authorize_maintenance_operation=None, execute_time=None
    ):
        """
        Initialize AuthorizeServerEventRequest request entity.

        :param action: action parameter
        :type action: str (required)

        :param server_event_id: 维修事件ID，serverEventId、instanceId必须选择其中一个请求
        :type server_event_id: str (optional)

        :param instance_id: 实例ID，serverEventId、instanceId必须选择其中一个请求
        :type instance_id: str (optional)

        :param authorize_maintenance_operation: 授权的运维操作，参考事件返回的运维操作
        :type authorize_maintenance_operation: str (optional)

        :param execute_time: 授权的执行时间，符合BCE规范的日期格式
        :type execute_time: str (optional)
        """
        super().__init__()
        self.action = action
        self.server_event_id = server_event_id
        self.instance_id = instance_id
        self.authorize_maintenance_operation = authorize_maintenance_operation
        self.execute_time = execute_time

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
        if self.authorize_maintenance_operation is not None:
            result['authorizeMaintenanceOperation'] = self.authorize_maintenance_operation
        if self.execute_time is not None:
            result['executeTime'] = self.execute_time
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AuthorizeServerEventRequest

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
        if m.get('authorizeMaintenanceOperation') is not None:
            self.authorize_maintenance_operation = m.get('authorizeMaintenanceOperation')
        if m.get('executeTime') is not None:
            self.execute_time = m.get('executeTime')
        return self
