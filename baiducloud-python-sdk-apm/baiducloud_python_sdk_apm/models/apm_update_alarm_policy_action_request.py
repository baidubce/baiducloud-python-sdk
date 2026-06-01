"""
Request entity for ApmUpdateAlarmPolicyActionRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_apm.models.alarm_action import AlarmAction


class ApmUpdateAlarmPolicyActionRequest(AbstractModel):
    """
    Request entity for ApmUpdateAlarmPolicyActionRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id, actions):
        """
        Initialize ApmUpdateAlarmPolicyActionRequest request entity.

        :param id: 策略ID
        :type id: str (required)

        :param actions: 通知模板列表，统一用于异常通知、恢复通知、重复报警通知
        :type actions: List[AlarmAction] (required)
        """
        super().__init__()
        self.id = id
        self.actions = actions

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
        if self.id is not None:
            result['id'] = self.id
        if self.actions is not None:
            result['actions'] = [i.to_dict() for i in self.actions]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ApmUpdateAlarmPolicyActionRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('actions') is not None:
            self.actions = [AlarmAction().from_dict(i) for i in m.get('actions')]
        return self
