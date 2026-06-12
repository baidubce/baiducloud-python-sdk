"""
AlarmAction information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AlarmAction(AbstractModel):
    """
    AlarmAction
    """

    def __init__(self, name=None, type=None, executed_time=None, notifications=None, call_backs=None, members=None):
        """
        Initialize AlarmAction instance.

        :param name: 通知模板名称
        :type name: str (optional)

        :param type: 触发类型，可选值：ALERT（报警时触发）/ OK（恢复时触发）
        :type type: str (optional)

        :param executed_time: 触发时间，UNIX时间戳，单位：ms
        :type executed_time: int (optional)

        :param notifications: 通知方式列表，可选值：SMS / EMAIL / PHONE
        :type notifications: List[str] (optional)

        :param call_backs: 回调webhook URL列表
        :type call_backs: List[str] (optional)

        :param members: 通知对象列表
        :type members: List[str] (optional)
        """
        super().__init__()
        self.name = name
        self.type = type
        self.executed_time = executed_time
        self.notifications = notifications
        self.call_backs = call_backs
        self.members = members

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.executed_time is not None:
            result['executedTime'] = self.executed_time
        if self.notifications is not None:
            result['notifications'] = self.notifications
        if self.call_backs is not None:
            result['callBacks'] = self.call_backs
        if self.members is not None:
            result['members'] = self.members
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AlarmAction

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('executedTime') is not None:
            self.executed_time = m.get('executedTime')
        if m.get('notifications') is not None:
            self.notifications = m.get('notifications')
        if m.get('callBacks') is not None:
            self.call_backs = m.get('callBacks')
        if m.get('members') is not None:
            self.members = m.get('members')
        return self
