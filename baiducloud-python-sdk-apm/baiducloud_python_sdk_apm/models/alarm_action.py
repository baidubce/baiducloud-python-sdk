"""
AlarmAction information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_apm.models.disable_time import DisableTime


class AlarmAction(AbstractModel):
    """
    AlarmAction
    """

    def __init__(self, notify_id=None, alias=None, call_backs=None, disable_times=None, members=None, types=None):
        """
        Initialize AlarmAction instance.

        :param notify_id: 通知模板ID
        :type notify_id: str (optional)

        :param alias: 通知模板名称，仅在查询响应中返回
        :type alias: str (optional)

        :param call_backs: 回调地址列表，仅在查询响应中返回
        :type call_backs: List[str] (optional)

        :param disable_times: 屏蔽时间列表，仅在查询响应中返回
        :type disable_times: List[DisableTime] (optional)

        :param members: 成员列表，仅在查询响应中返回
        :type members: List[str] (optional)

        :param types: 通知类型列表，如EMAIL，仅在查询响应中返回
        :type types: List[str] (optional)
        """
        super().__init__()
        self.notify_id = notify_id
        self.alias = alias
        self.call_backs = call_backs
        self.disable_times = disable_times
        self.members = members
        self.types = types

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
        if self.notify_id is not None:
            result['notifyId'] = self.notify_id
        if self.alias is not None:
            result['alias'] = self.alias
        if self.call_backs is not None:
            result['callBacks'] = self.call_backs
        if self.disable_times is not None:
            result['disableTimes'] = [i.to_dict() for i in self.disable_times]
        if self.members is not None:
            result['members'] = self.members
        if self.types is not None:
            result['types'] = self.types
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
        if m.get('notifyId') is not None:
            self.notify_id = m.get('notifyId')
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('callBacks') is not None:
            self.call_backs = m.get('callBacks')
        if m.get('disableTimes') is not None:
            self.disable_times = [DisableTime().from_dict(i) for i in m.get('disableTimes')]
        if m.get('members') is not None:
            self.members = m.get('members')
        if m.get('types') is not None:
            self.types = m.get('types')
        return self
