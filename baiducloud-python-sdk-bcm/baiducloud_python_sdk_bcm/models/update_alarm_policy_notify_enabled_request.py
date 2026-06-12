"""
Request entity for UpdateAlarmPolicyNotifyEnabledRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateAlarmPolicyNotifyEnabledRequest(AbstractModel):
    """
    Request entity for UpdateAlarmPolicyNotifyEnabledRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, ids, notify_enabled):
        """
        Initialize UpdateAlarmPolicyNotifyEnabledRequest request entity.

        :param ids: 策略ID列表
        :type ids: List[str] (required)

        :param notify_enabled: 是否开启通知
        :type notify_enabled: bool (required)
        """
        super().__init__()
        self.ids = ids
        self.notify_enabled = notify_enabled

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
        if self.ids is not None:
            result['ids'] = self.ids
        if self.notify_enabled is not None:
            result['notifyEnabled'] = self.notify_enabled
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateAlarmPolicyNotifyEnabledRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('notifyEnabled') is not None:
            self.notify_enabled = m.get('notifyEnabled')
        return self
