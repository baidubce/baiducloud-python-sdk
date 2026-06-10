"""
AutoSnapshotPolicyInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AutoSnapshotPolicyInfo(AbstractModel):
    """
    AutoSnapshotPolicyInfo
    """

    def __init__(self, id=None, name=None, time_points=None, repeat_weekdays=None, retention_days=None, status=None):
        """
        Initialize AutoSnapshotPolicyInfo instance.

        :param id: 快照策略ID
        :type id: str (optional)

        :param name: 快照策略名称
        :type name: str (optional)

        :param time_points: 自动快照策略中设置的执行时间点
        :type time_points: List[int] (optional)

        :param repeat_weekdays: 自动快照策略中设置的执行日期
        :type repeat_weekdays: List[int] (optional)

        :param retention_days: 保留天数
        :type retention_days: int (optional)

        :param status: 快照策略状态
        :type status: str (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.time_points = time_points
        self.repeat_weekdays = repeat_weekdays
        self.retention_days = retention_days
        self.status = status

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
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.time_points is not None:
            result['timePoints'] = self.time_points
        if self.repeat_weekdays is not None:
            result['repeatWeekdays'] = self.repeat_weekdays
        if self.retention_days is not None:
            result['retentionDays'] = self.retention_days
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AutoSnapshotPolicyInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('timePoints') is not None:
            self.time_points = m.get('timePoints')
        if m.get('repeatWeekdays') is not None:
            self.repeat_weekdays = m.get('repeatWeekdays')
        if m.get('retentionDays') is not None:
            self.retention_days = m.get('retentionDays')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
